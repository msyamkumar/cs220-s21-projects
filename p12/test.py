#!/usr/bin/python

import ast, os, sys, subprocess, json, re, collections, math, warnings
from collections import namedtuple, OrderedDict, defaultdict
from bs4 import BeautifulSoup
from datetime import datetime
import nbconvert
import nbformat

# check the python version
if sys.version[:5] < '3.7.0':
    warnings.warn('Your current python version is {}. Please upgrade your python version to at least 3.7.0.'.format(sys.version[:5]))

################################################################################
REL_TOL = 1e-05 # relative tolerance for floats
ABS_TOL = 15e-04 # absolute tolerance for floats
LINTER = True # set to False if linter should be turned off for project
################################################################################

try:
    from lint import lint
except ImportError:
    err_msg = """Please download lint.py and place it in this directory for
    the tests to run correctly. If you haven't yet looked at the linting module,
    it is designed to help you improve your code so take a look at:
    https://github.com/msyamkumar/cs220-projects/tree/master/linter"""
    raise FileNotFoundError(err_msg)

ALLOWED_LINT_ERRS = {
  "W0703": "broad-except",
  "R1716": "chained-comparison",
  "E0601": "used-before-assignment",
  "W0105": "pointless-string-statement",
  "E1135": "unsupported-membership-test",
  "R1711": "useless-return",
  "W0143": "comparison-with-callable",
  "E1102": "not-callable",
  "W0107": "unnecessary-pass",
  "W0301": "unnecessary-semicolon",
  "W0404": "reimported",
  "W0101": "unreachable",
  "R1714": "consider-using-in",
  "W0311": "bad-indentation",
  "E0102": "function-redefined",
  "E0602": "undefined-variable",
  "W0104": "pointless-statement",
  "W0622": "redefined-builtin",
  "W0702": "bare-except",
  "R1703": "simplifiable-if-statement",
  "W0631": "undefined-loop-variable",
}

PASS = "PASS"
TEXT_FORMAT = "text" # question type when expected answer is a str, int, float, or bool
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered" # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered" # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_DICT = "text dict" # question type when the expected answer is a dictionary
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered" # question type when the expected answer is a list of dicts where the order does matter
HTML_FORMAT = "html"

Question = collections.namedtuple("Question", ["number", "weight", "format"])

questions = [
    # stage 1
    Question(number=1, weight=1, format=TEXT_FORMAT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=4, weight=1, format=TEXT_FORMAT),
    Question(number=5, weight=1, format=TEXT_FORMAT),
    Question(number=6, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=7, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=8, weight=1, format=TEXT_FORMAT),
    Question(number=9, weight=1, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT),
    Question(number=12, weight=1, format=TEXT_FORMAT),
    Question(number=13, weight=1, format=HTML_FORMAT),
    Question(number=14, weight=1, format=HTML_FORMAT),
    Question(number=15, weight=1, format=TEXT_FORMAT),
    Question(number=16, weight=1, format=TEXT_FORMAT),
    Question(number=17, weight=1, format=HTML_FORMAT),
    Question(number=18, weight=1, format=HTML_FORMAT),
    Question(number=19, weight=1, format=HTML_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT_ORDERED_LIST)
]
question_nums = set([q.number for q in questions])

# JSON and plaintext values
expected_json = {
    "1": 174,
    "2": 6261901793,
    "3": ['Abu Dhabi',
         'Abuja',
         'Accra',
         'Addis Ababa',
         'Algiers',
         'Amman',
         'Amsterdam',
         'Ankara',
         'Antananarivo',
         'Apia',
         'Ashgabat',
         'Asmara',
         'Astana',
         'Asuncion',
         'Athens',
         'Baghdad',
         'Baku',
         'Bamako',
         'Bangkok',
         'Beijing',
         'Beirut',
         'Belmopan',
         'Berlin',
         'Bern',
         'Bishkek',
         'Bissau',
         'Bogota',
         'Brasilia',
         'Bridgetown',
         'Brussels',
         'Bucharest',
         'Budapest',
         'Buenos Aires',
         'Bujumbura',
         'Cairo',
         'Canberra',
         'Caracas',
         'Castries',
         'Chisinau',
         'Colombo',
         'Conakry',
         'Copenhagen',
         'Dakar',
         'Damascus',
         'Dar es Salaam',
         'Dhaka',
         'Djibouti',
         'Doha',
         'Dublin',
         'Dushanbe',
         'Freetown',
         'Gaborone',
         'George Town',
         'Georgetown',
         'Guatemala City',
         'Hagatna',
         'Hamilton',
         'Hanoi',
         'Harare',
         'Havana',
         'Helsinki',
         'Islamabad',
         'Jakarta',
         'Jamestown',
         'Jerusalem',
         'Kabul',
         'Kampala',
         'Kathmandu',
         'Khartoum',
         'Kigali',
         'Kingston',
         'Kingstown',
         'Kuala Lumpur',
         'Kuwait City',
         'Kyiv',
         'La Paz',
         'Libreville',
         'Lilongwe',
         'Lima',
         'Lisbon',
         'Ljubljana',
         'Lome',
         'London',
         'Lusaka',
         'Luxembourg',
         'Madrid',
         'Majuro',
         'Malabo',
         'Male',
         'Managua',
         'Manama',
         'Manila',
         'Maputo',
         'Maseru',
         'Mbabane',
         'Melekeok',
         'Mexico City',
         'Minsk',
         'Mogadishu',
         'Monaco',
         'Monrovia',
         'Montevideo',
         'Moroni',
         'Moscow',
         'Muscat',
         'Nairobi',
         'New Delhi',
         'Niamey',
         'Nouakchott',
         'Noumea',
         'Nuku’alofa',
         'N’Djamena',
         'Oranjestad',
         'Oslo',
         'Ottawa',
         'Ouagadougou',
         'Panama City',
         'Papeete',
         'Paramaribo',
         'Paris',
         'Phnom Penh',
         'Port Louis',
         'Port Moresby',
         'Port-Vila',
         'Port-au-Prince',
         'Porto-Novo',
         'Prague',
         'Praia',
         'Pretoria',
         'Quito',
         'Rabat',
         'Reykjavik',
         'Riga',
         'Riyadh',
         'Rome',
         'Roseau',
         'Saint George’s',
         'San Jose',
         'San Juan',
         'San Marino',
         'San Salvador',
         'Sanaa',
         'Santiago',
         'Santo Domingo',
         'Singapore',
         'Sofia',
         'Stockholm',
         'Suva',
         'Taipei',
         'Tallinn',
         'Tashkent',
         'Tbilisi',
         'Tegucigalpa',
         'Tehran',
         'The Valley',
         'Thimphu',
         'Tirana',
         'Tokyo',
         'Tripoli',
         'Tunis',
         'Ulaanbaatar',
         'Vaduz',
         'Valletta',
         'Victoria',
         'Vienna',
         'Vientiane',
         'Vilnius',
         'Warsaw',
         'Washington, D.C.',
         'Wellington',
         'Windhoek',
         'Yaounde',
         'Yerevan',
         'Zagreb'],
    "4": 'Stockholm',
    "5": 'Chile',
    "6": ['New Zealand',
         'Australia',
         'Uruguay',
         'Argentina',
         'Chile',
         'Lesotho',
         'Swaziland'],
    "7": ['Iceland',
         'Finland',
         'Norway',
         'Estonia',
         'Sweden',
         'Latvia',
         'Russia',
         'Denmark',
         'Lithuania',
         'Belarus'],
    "8": 'Bolivia',
    "9": 'Sudan',
    "10": 'Maldives',
    "11": 1.433899492072933,
    "12": 162.36419849726036,
    "15": 'Vanuatu',
    "16": 'French Polynesia',
    "20": [{'country': 'Afghanistan',
          'capital': 'Kabul',
          'latitude': 34.51666667,
          'longitude': 69.183333},
         {'country': 'Albania',
          'capital': 'Tirana',
          'latitude': 41.31666667,
          'longitude': 19.816667},
         {'country': 'Algeria',
          'capital': 'Algiers',
          'latitude': 36.75,
          'longitude': 3.05},
         {'country': 'Anguilla',
          'capital': 'The Valley',
          'latitude': 18.21666667,
          'longitude': -63.05},
         {'country': 'Argentina',
          'capital': 'Buenos Aires',
          'latitude': -34.58333333,
          'longitude': -58.666667},
         {'country': 'Armenia',
          'capital': 'Yerevan',
          'latitude': 40.16666667,
          'longitude': 44.5},
         {'country': 'Aruba',
          'capital': 'Oranjestad',
          'latitude': 12.51666667,
          'longitude': -70.033333},
         {'country': 'Australia',
          'capital': 'Canberra',
          'latitude': -35.26666667,
          'longitude': 149.133333},
         {'country': 'Austria',
          'capital': 'Vienna',
          'latitude': 48.2,
          'longitude': 16.366667},
         {'country': 'Azerbaijan',
          'capital': 'Baku',
          'latitude': 40.38333333,
          'longitude': 49.866667},
         {'country': 'Bahrain',
          'capital': 'Manama',
          'latitude': 26.23333333,
          'longitude': 50.566667},
         {'country': 'Bangladesh',
          'capital': 'Dhaka',
          'latitude': 23.71666667,
          'longitude': 90.4},
         {'country': 'Barbados',
          'capital': 'Bridgetown',
          'latitude': 13.1,
          'longitude': -59.616667},
         {'country': 'Belarus',
          'capital': 'Minsk',
          'latitude': 53.9,
          'longitude': 27.566667},
         {'country': 'Belgium',
          'capital': 'Brussels',
          'latitude': 50.83333333,
          'longitude': 4.333333},
         {'country': 'Belize',
          'capital': 'Belmopan',
          'latitude': 17.25,
          'longitude': -88.766667},
         {'country': 'Benin',
          'capital': 'Porto-Novo',
          'latitude': 6.483333333,
          'longitude': 2.616667},
         {'country': 'Bermuda',
          'capital': 'Hamilton',
          'latitude': 32.28333333,
          'longitude': -64.783333},
         {'country': 'Bhutan',
          'capital': 'Thimphu',
          'latitude': 27.46666667,
          'longitude': 89.633333},
         {'country': 'Bolivia',
          'capital': 'La Paz',
          'latitude': -16.5,
          'longitude': -68.15},
         {'country': 'Botswana',
          'capital': 'Gaborone',
          'latitude': -24.63333333,
          'longitude': 25.9},
         {'country': 'Brazil',
          'capital': 'Brasilia',
          'latitude': -15.78333333,
          'longitude': -47.916667},
         {'country': 'Bulgaria',
          'capital': 'Sofia',
          'latitude': 42.68333333,
          'longitude': 23.316667},
         {'country': 'Burkina Faso',
          'capital': 'Ouagadougou',
          'latitude': 12.36666667,
          'longitude': -1.516667},
         {'country': 'Burundi',
          'capital': 'Bujumbura',
          'latitude': -3.366666667,
          'longitude': 29.35},
         {'country': 'Cambodia',
          'capital': 'Phnom Penh',
          'latitude': 11.55,
          'longitude': 104.916667},
         {'country': 'Cameroon',
          'capital': 'Yaounde',
          'latitude': 3.866666667,
          'longitude': 11.516667},
         {'country': 'Canada',
          'capital': 'Ottawa',
          'latitude': 45.41666667,
          'longitude': -75.7},
         {'country': 'Cape Verde',
          'capital': 'Praia',
          'latitude': 14.91666667,
          'longitude': -23.516667},
         {'country': 'Cayman Islands',
          'capital': 'George Town',
          'latitude': 19.3,
          'longitude': -81.383333},
         {'country': 'Chad',
          'capital': 'N’Djamena',
          'latitude': 12.1,
          'longitude': 15.033333},
         {'country': 'Chile',
          'capital': 'Santiago',
          'latitude': -33.45,
          'longitude': -70.666667},
         {'country': 'China',
          'capital': 'Beijing',
          'latitude': 39.91666667,
          'longitude': 116.383333},
         {'country': 'Colombia',
          'capital': 'Bogota',
          'latitude': 4.6,
          'longitude': -74.083333},
         {'country': 'Comoros',
          'capital': 'Moroni',
          'latitude': -11.7,
          'longitude': 43.233333},
         {'country': 'Costa Rica',
          'capital': 'San Jose',
          'latitude': 9.933333333,
          'longitude': -84.083333},
         {'country': 'Croatia',
          'capital': 'Zagreb',
          'latitude': 45.8,
          'longitude': 16.0},
         {'country': 'Cuba',
          'capital': 'Havana',
          'latitude': 23.11666667,
          'longitude': -82.35},
         {'country': 'Czech Republic',
          'capital': 'Prague',
          'latitude': 50.08333333,
          'longitude': 14.466667},
         {'country': 'Denmark',
          'capital': 'Copenhagen',
          'latitude': 55.66666667,
          'longitude': 12.583333},
         {'country': 'Djibouti',
          'capital': 'Djibouti',
          'latitude': 11.58333333,
          'longitude': 43.15},
         {'country': 'Dominica',
          'capital': 'Roseau',
          'latitude': 15.3,
          'longitude': -61.4},
         {'country': 'Dominican Republic',
          'capital': 'Santo Domingo',
          'latitude': 18.46666667,
          'longitude': -69.9},
         {'country': 'Ecuador',
          'capital': 'Quito',
          'latitude': -0.216666667,
          'longitude': -78.5},
         {'country': 'Egypt',
          'capital': 'Cairo',
          'latitude': 30.05,
          'longitude': 31.25},
         {'country': 'El Salvador',
          'capital': 'San Salvador',
          'latitude': 13.7,
          'longitude': -89.2},
         {'country': 'Equatorial Guinea',
          'capital': 'Malabo',
          'latitude': 3.75,
          'longitude': 8.783333},
         {'country': 'Eritrea',
          'capital': 'Asmara',
          'latitude': 15.33333333,
          'longitude': 38.933333},
         {'country': 'Estonia',
          'capital': 'Tallinn',
          'latitude': 59.43333333,
          'longitude': 24.716667},
         {'country': 'Ethiopia',
          'capital': 'Addis Ababa',
          'latitude': 9.033333333,
          'longitude': 38.7},
         {'country': 'Fiji',
          'capital': 'Suva',
          'latitude': -18.13333333,
          'longitude': 178.416667},
         {'country': 'Finland',
          'capital': 'Helsinki',
          'latitude': 60.16666667,
          'longitude': 24.933333},
         {'country': 'France',
          'capital': 'Paris',
          'latitude': 48.86666667,
          'longitude': 2.333333},
         {'country': 'French Polynesia',
          'capital': 'Papeete',
          'latitude': -17.53333333,
          'longitude': -149.566667},
         {'country': 'Gabon',
          'capital': 'Libreville',
          'latitude': 0.383333333,
          'longitude': 9.45},
         {'country': 'Georgia',
          'capital': 'Tbilisi',
          'latitude': 41.68333333,
          'longitude': 44.833333},
         {'country': 'Germany',
          'capital': 'Berlin',
          'latitude': 52.51666667,
          'longitude': 13.4},
         {'country': 'Ghana',
          'capital': 'Accra',
          'latitude': 5.55,
          'longitude': -0.216667},
         {'country': 'Greece',
          'capital': 'Athens',
          'latitude': 37.98333333,
          'longitude': 23.733333},
         {'country': 'Grenada',
          'capital': 'Saint George’s',
          'latitude': 12.05,
          'longitude': -61.75},
         {'country': 'Guam',
          'capital': 'Hagatna',
          'latitude': 13.46666667,
          'longitude': 144.733333},
         {'country': 'Guatemala',
          'capital': 'Guatemala City',
          'latitude': 14.61666667,
          'longitude': -90.516667},
         {'country': 'Guinea',
          'capital': 'Conakry',
          'latitude': 9.5,
          'longitude': -13.7},
         {'country': 'Guinea-Bissau',
          'capital': 'Bissau',
          'latitude': 11.85,
          'longitude': -15.583333},
         {'country': 'Guyana',
          'capital': 'Georgetown',
          'latitude': 6.8,
          'longitude': -58.15},
         {'country': 'Haiti',
          'capital': 'Port-au-Prince',
          'latitude': 18.53333333,
          'longitude': -72.333333},
         {'country': 'Honduras',
          'capital': 'Tegucigalpa',
          'latitude': 14.1,
          'longitude': -87.216667},
         {'country': 'Hungary',
          'capital': 'Budapest',
          'latitude': 47.5,
          'longitude': 19.083333},
         {'country': 'Iceland',
          'capital': 'Reykjavik',
          'latitude': 64.15,
          'longitude': -21.95},
         {'country': 'India',
          'capital': 'New Delhi',
          'latitude': 28.6,
          'longitude': 77.2},
         {'country': 'Indonesia',
          'capital': 'Jakarta',
          'latitude': -6.166666667,
          'longitude': 106.816667},
         {'country': 'Iran',
          'capital': 'Tehran',
          'latitude': 35.7,
          'longitude': 51.416667},
         {'country': 'Iraq',
          'capital': 'Baghdad',
          'latitude': 33.33333333,
          'longitude': 44.4},
         {'country': 'Ireland',
          'capital': 'Dublin',
          'latitude': 53.31666667,
          'longitude': -6.233333},
         {'country': 'Israel',
          'capital': 'Jerusalem',
          'latitude': 31.76666667,
          'longitude': 35.233333},
         {'country': 'Italy',
          'capital': 'Rome',
          'latitude': 41.9,
          'longitude': 12.483333},
         {'country': 'Jamaica',
          'capital': 'Kingston',
          'latitude': 18.0,
          'longitude': -76.8},
         {'country': 'Japan',
          'capital': 'Tokyo',
          'latitude': 35.68333333,
          'longitude': 139.75},
         {'country': 'Jordan',
          'capital': 'Amman',
          'latitude': 31.95,
          'longitude': 35.933333},
         {'country': 'Kazakhstan',
          'capital': 'Astana',
          'latitude': 51.16666667,
          'longitude': 71.416667},
         {'country': 'Kenya',
          'capital': 'Nairobi',
          'latitude': -1.283333333,
          'longitude': 36.816667},
         {'country': 'Kuwait',
          'capital': 'Kuwait City',
          'latitude': 29.36666667,
          'longitude': 47.966667},
         {'country': 'Kyrgyzstan',
          'capital': 'Bishkek',
          'latitude': 42.86666667,
          'longitude': 74.6},
         {'country': 'Laos',
          'capital': 'Vientiane',
          'latitude': 17.96666667,
          'longitude': 102.6},
         {'country': 'Latvia',
          'capital': 'Riga',
          'latitude': 56.95,
          'longitude': 24.1},
         {'country': 'Lebanon',
          'capital': 'Beirut',
          'latitude': 33.86666667,
          'longitude': 35.5},
         {'country': 'Lesotho',
          'capital': 'Maseru',
          'latitude': -29.31666667,
          'longitude': 27.483333},
         {'country': 'Liberia',
          'capital': 'Monrovia',
          'latitude': 6.3,
          'longitude': -10.8},
         {'country': 'Libya',
          'capital': 'Tripoli',
          'latitude': 32.88333333,
          'longitude': 13.166667},
         {'country': 'Liechtenstein',
          'capital': 'Vaduz',
          'latitude': 47.13333333,
          'longitude': 9.516667},
         {'country': 'Lithuania',
          'capital': 'Vilnius',
          'latitude': 54.68333333,
          'longitude': 25.316667},
         {'country': 'Luxembourg',
          'capital': 'Luxembourg',
          'latitude': 49.6,
          'longitude': 6.116667},
         {'country': 'Madagascar',
          'capital': 'Antananarivo',
          'latitude': -18.91666667,
          'longitude': 47.516667},
         {'country': 'Malawi',
          'capital': 'Lilongwe',
          'latitude': -13.96666667,
          'longitude': 33.783333},
         {'country': 'Malaysia',
          'capital': 'Kuala Lumpur',
          'latitude': 3.166666667,
          'longitude': 101.7},
         {'country': 'Maldives',
          'capital': 'Male',
          'latitude': 4.166666667,
          'longitude': 73.5},
         {'country': 'Mali',
          'capital': 'Bamako',
          'latitude': 12.65,
          'longitude': -8.0},
         {'country': 'Malta',
          'capital': 'Valletta',
          'latitude': 35.88333333,
          'longitude': 14.5},
         {'country': 'Marshall Islands',
          'capital': 'Majuro',
          'latitude': 7.1,
          'longitude': 171.383333},
         {'country': 'Mauritania',
          'capital': 'Nouakchott',
          'latitude': 18.06666667,
          'longitude': -15.966667},
         {'country': 'Mauritius',
          'capital': 'Port Louis',
          'latitude': -20.15,
          'longitude': 57.483333},
         {'country': 'Mexico',
          'capital': 'Mexico City',
          'latitude': 19.43333333,
          'longitude': -99.133333},
         {'country': 'Moldova',
          'capital': 'Chisinau',
          'latitude': 47.0,
          'longitude': 28.85},
         {'country': 'Monaco',
          'capital': 'Monaco',
          'latitude': 43.73333333,
          'longitude': 7.416667},
         {'country': 'Mongolia',
          'capital': 'Ulaanbaatar',
          'latitude': 47.91666667,
          'longitude': 106.916667},
         {'country': 'Morocco',
          'capital': 'Rabat',
          'latitude': 34.01666667,
          'longitude': -6.816667},
         {'country': 'Mozambique',
          'capital': 'Maputo',
          'latitude': -25.95,
          'longitude': 32.583333},
         {'country': 'Namibia',
          'capital': 'Windhoek',
          'latitude': -22.56666667,
          'longitude': 17.083333},
         {'country': 'Nepal',
          'capital': 'Kathmandu',
          'latitude': 27.71666667,
          'longitude': 85.316667},
         {'country': 'Netherlands',
          'capital': 'Amsterdam',
          'latitude': 52.35,
          'longitude': 4.916667},
         {'country': 'New Caledonia',
          'capital': 'Noumea',
          'latitude': -22.26666667,
          'longitude': 166.45},
         {'country': 'New Zealand',
          'capital': 'Wellington',
          'latitude': -41.3,
          'longitude': 174.783333},
         {'country': 'Nicaragua',
          'capital': 'Managua',
          'latitude': 12.13333333,
          'longitude': -86.25},
         {'country': 'Niger',
          'capital': 'Niamey',
          'latitude': 13.51666667,
          'longitude': 2.116667},
         {'country': 'Nigeria',
          'capital': 'Abuja',
          'latitude': 9.083333333,
          'longitude': 7.533333},
         {'country': 'Norway',
          'capital': 'Oslo',
          'latitude': 59.91666667,
          'longitude': 10.75},
         {'country': 'Oman',
          'capital': 'Muscat',
          'latitude': 23.61666667,
          'longitude': 58.583333},
         {'country': 'Pakistan',
          'capital': 'Islamabad',
          'latitude': 33.68333333,
          'longitude': 73.05},
         {'country': 'Palau',
          'capital': 'Melekeok',
          'latitude': 7.483333333,
          'longitude': 134.633333},
         {'country': 'Panama',
          'capital': 'Panama City',
          'latitude': 8.966666667,
          'longitude': -79.533333},
         {'country': 'Papua New Guinea',
          'capital': 'Port Moresby',
          'latitude': -9.45,
          'longitude': 147.183333},
         {'country': 'Paraguay',
          'capital': 'Asuncion',
          'latitude': -25.26666667,
          'longitude': -57.666667},
         {'country': 'Peru',
          'capital': 'Lima',
          'latitude': -12.05,
          'longitude': -77.05},
         {'country': 'Philippines',
          'capital': 'Manila',
          'latitude': 14.6,
          'longitude': 120.966667},
         {'country': 'Poland',
          'capital': 'Warsaw',
          'latitude': 52.25,
          'longitude': 21.0},
         {'country': 'Portugal',
          'capital': 'Lisbon',
          'latitude': 38.71666667,
          'longitude': -9.133333},
         {'country': 'Puerto Rico',
          'capital': 'San Juan',
          'latitude': 18.46666667,
          'longitude': -66.116667},
         {'country': 'Qatar',
          'capital': 'Doha',
          'latitude': 25.28333333,
          'longitude': 51.533333},
         {'country': 'Romania',
          'capital': 'Bucharest',
          'latitude': 44.43333333,
          'longitude': 26.1},
         {'country': 'Russia',
          'capital': 'Moscow',
          'latitude': 55.75,
          'longitude': 37.6},
         {'country': 'Rwanda',
          'capital': 'Kigali',
          'latitude': -1.95,
          'longitude': 30.05},
         {'country': 'Saint Helena',
          'capital': 'Jamestown',
          'latitude': -15.93333333,
          'longitude': -5.716667},
         {'country': 'Saint Lucia',
          'capital': 'Castries',
          'latitude': 14.0,
          'longitude': -61.0},
         {'country': 'Saint Vincent and the Grenadines',
          'capital': 'Kingstown',
          'latitude': 13.13333333,
          'longitude': -61.216667},
         {'country': 'Samoa',
          'capital': 'Apia',
          'latitude': -13.81666667,
          'longitude': -171.766667},
         {'country': 'San Marino',
          'capital': 'San Marino',
          'latitude': 43.93333333,
          'longitude': 12.416667},
         {'country': 'Saudi Arabia',
          'capital': 'Riyadh',
          'latitude': 24.65,
          'longitude': 46.7},
         {'country': 'Senegal',
          'capital': 'Dakar',
          'latitude': 14.73333333,
          'longitude': -17.633333},
         {'country': 'Seychelles',
          'capital': 'Victoria',
          'latitude': -4.616666667,
          'longitude': 55.45},
         {'country': 'Sierra Leone',
          'capital': 'Freetown',
          'latitude': 8.483333333,
          'longitude': -13.233333},
         {'country': 'Singapore',
          'capital': 'Singapore',
          'latitude': 1.283333333,
          'longitude': 103.85},
         {'country': 'Slovenia',
          'capital': 'Ljubljana',
          'latitude': 46.05,
          'longitude': 14.516667},
         {'country': 'Somalia',
          'capital': 'Mogadishu',
          'latitude': 2.066666667,
          'longitude': 45.333333},
         {'country': 'South Africa',
          'capital': 'Pretoria',
          'latitude': -25.7,
          'longitude': 28.216667},
         {'country': 'Spain',
          'capital': 'Madrid',
          'latitude': 40.4,
          'longitude': -3.683333},
         {'country': 'Sri Lanka',
          'capital': 'Colombo',
          'latitude': 6.916666667,
          'longitude': 79.833333},
         {'country': 'Sudan',
          'capital': 'Khartoum',
          'latitude': 15.6,
          'longitude': 32.533333},
         {'country': 'Suriname',
          'capital': 'Paramaribo',
          'latitude': 5.833333333,
          'longitude': -55.166667},
         {'country': 'Swaziland',
          'capital': 'Mbabane',
          'latitude': -26.31666667,
          'longitude': 31.133333},
         {'country': 'Sweden',
          'capital': 'Stockholm',
          'latitude': 59.33333333,
          'longitude': 18.05},
         {'country': 'Switzerland',
          'capital': 'Bern',
          'latitude': 46.91666667,
          'longitude': 7.466667},
         {'country': 'Syria',
          'capital': 'Damascus',
          'latitude': 33.5,
          'longitude': 36.3},
         {'country': 'Taiwan',
          'capital': 'Taipei',
          'latitude': 25.03333333,
          'longitude': 121.516667},
         {'country': 'Tajikistan',
          'capital': 'Dushanbe',
          'latitude': 38.55,
          'longitude': 68.766667},
         {'country': 'Tanzania',
          'capital': 'Dar es Salaam',
          'latitude': -6.8,
          'longitude': 39.283333},
         {'country': 'Thailand',
          'capital': 'Bangkok',
          'latitude': 13.75,
          'longitude': 100.516667},
         {'country': 'Togo',
          'capital': 'Lome',
          'latitude': 6.116666667,
          'longitude': 1.216667},
         {'country': 'Tonga',
          'capital': 'Nuku’alofa',
          'latitude': -21.13333333,
          'longitude': -175.2},
         {'country': 'Tunisia',
          'capital': 'Tunis',
          'latitude': 36.8,
          'longitude': 10.183333},
         {'country': 'Turkey',
          'capital': 'Ankara',
          'latitude': 39.93333333,
          'longitude': 32.866667},
         {'country': 'Turkmenistan',
          'capital': 'Ashgabat',
          'latitude': 37.95,
          'longitude': 58.383333},
         {'country': 'Uganda',
          'capital': 'Kampala',
          'latitude': 0.316666667,
          'longitude': 32.55},
         {'country': 'Ukraine',
          'capital': 'Kyiv',
          'latitude': 50.43333333,
          'longitude': 30.516667},
         {'country': 'United Arab Emirates',
          'capital': 'Abu Dhabi',
          'latitude': 24.46666667,
          'longitude': 54.366667},
         {'country': 'United Kingdom',
          'capital': 'London',
          'latitude': 51.5,
          'longitude': -0.083333},
         {'country': 'United States',
          'capital': 'Washington, D.C.',
          'latitude': 38.883333,
          'longitude': -77.0},
         {'country': 'Uruguay',
          'capital': 'Montevideo',
          'latitude': -34.85,
          'longitude': -56.166667},
         {'country': 'Uzbekistan',
          'capital': 'Tashkent',
          'latitude': 41.31666667,
          'longitude': 69.25},
         {'country': 'Vanuatu',
          'capital': 'Port-Vila',
          'latitude': -17.73333333,
          'longitude': 168.316667},
         {'country': 'Venezuela',
          'capital': 'Caracas',
          'latitude': 10.48333333,
          'longitude': -66.866667},
         {'country': 'Vietnam',
          'capital': 'Hanoi',
          'latitude': 21.03333333,
          'longitude': 105.85},
         {'country': 'Yemen',
          'capital': 'Sanaa',
          'latitude': 15.35,
          'longitude': 44.2},
         {'country': 'Zambia',
          'capital': 'Lusaka',
          'latitude': -15.41666667,
          'longitude': 28.283333},
         {'country': 'Zimbabwe',
          'capital': 'Harare',
          'latitude': -17.81666667,
          'longitude': 31.033333}]
}
expected_files = ['expected.html']

def parse_df_html_table(html, question=None):
    soup = BeautifulSoup(html, 'html.parser')

    if question == None:
        tables = soup.find_all('table')
        assert(len(tables) == 1)
        table = tables[0]
    else:
        # find a table that looks like this:
        # <table data-question="6"> ...
        table = soup.find('table', {"data-question": str(question)})

    rows = []
    for tr in table.find_all('tr'):
        rows.append([])
        for cell in tr.find_all(['td', 'th']):
            rows[-1].append(cell.get_text())

    cells = {}
    for r in range(1, len(rows)):
        for c in range(1, len(rows[0])):
            rname = rows[r][0]
            cname = rows[0][c]
            cells[(rname,cname)] = rows[r][c]
    return cells


# find a comment something like this: #q10
def extract_question_num(cell):
    for line in cell.get('source', []):
        line = line.strip().replace(' ', '').lower()
        m = re.match(r'\#q(\d+)', line)
        if m:
            return int(m.group(1))
    return None


# find correct python command based on version
def get_python_cmd():
    cmds = ['python3', 'python', 'py']
    for cmd in cmds:
        try:
            out = subprocess.check_output(cmd + ' -V', shell=True, universal_newlines=True)
            m = re.match(r'Python\s+(\d+\.\d+)\.*\d*', out)
            if m:
                if float(m.group(1)) >= 3.6:
                    return cmd
        except subprocess.CalledProcessError:
            pass
    else:
        return ''

# rerun notebook and return parsed JSON
def rerun_notebook(orig_notebook):
    new_notebook = 'cs-220-test.ipynb'

    # re-execute it from the beginning
    py_cmd = get_python_cmd()
    cmd = 'jupyter nbconvert --execute "{orig}" --to notebook --output="{new}" --ExecutePreprocessor.timeout=120'
    cmd = cmd.format(orig=os.path.abspath(orig_notebook), new=os.path.abspath(new_notebook))
    if py_cmd:
        cmd = py_cmd + ' -m ' + cmd
    subprocess.check_output(cmd, shell=True)

    # parse notebook
    with open(new_notebook, encoding='utf-8') as f:
        nb = json.load(f)
    return nb


def normalize_json(orig):
    try:
        return json.dumps(json.loads(orig.strip("'")), indent=2, sort_keys=True)
    except:
        return 'not JSON'


def check_cell_text(qnum, cell, format):
    outputs = cell.get('outputs', [])
    if len(outputs) == 0:
        return 'no outputs in an Out[N] cell'
    actual_lines = None
    for out in outputs:
        lines = out.get('data', {}).get('text/plain', [])
        if lines:
            actual_lines = lines
            break
    if actual_lines == None:
        return 'no Out[N] output found for cell (note: printing the output does not work)'
    actual = ''.join(actual_lines)
    actual = ast.literal_eval(actual)
    expected = expected_json[str(qnum)]

    try:
        if format == TEXT_FORMAT:
            return simple_compare(expected, actual)
        elif format == TEXT_FORMAT_ORDERED_LIST:
            return list_compare_ordered(expected, actual)
        elif format == TEXT_FORMAT_UNORDERED_LIST:
            return list_compare_unordered(expected, actual)
        elif format == TEXT_FORMAT_DICT:
            return dict_compare(expected, actual)
        elif format == TEXT_FORMAT_LIST_DICTS_ORDERED:
            return list_compare_ordered(expected, actual)
        else:
            if expected != actual:
                return "found %s but expected %s" % (repr(actual), repr(expected))
    except:
        if expected != actual:
            return "expected %s" % (repr(expected))
    return PASS

def simple_compare(expected, actual, complete_msg=True):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
    elif type(expected) == float:
        if not math.isclose(actual, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL):
            msg = "expected %s"  % (repr(expected))
            if complete_msg:
                msg = msg + " but found %s" % (repr(actual))
    else:
        if expected != actual:
            msg = "expected %s"  % (repr(expected))
            if complete_msg:
                msg = msg + " but found %s" % (repr(actual))
    return msg

def list_compare_ordered(expected, actual, obj="list"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    for i in range(len(expected)):
        if i >= len(actual):
            msg = "expected missing %s in %s" % (repr(expected[i]), obj)
            break
        if type(expected[i]) in [int, float, bool, str]:
            val = simple_compare(expected[i], actual[i])
        elif type(expected[i]) in [list]:
            val = list_compare_ordered(expected[i], actual[i], "sub"+obj)
        elif type(expected[i]) in [dict]:
            val = dict_compare(expected[i], actual[i])
        if val != PASS:
            msg = "at index %d of the %s, " % (i, obj) + val
            break
    if len(actual) > len(expected) and msg == PASS:
        msg = "found unexpected %s in %s" % (repr(actual[len(expected)]), obj)
    if len(expected) != len(actual):
        msg = msg + " (found %d entries in %s, but expected %d)" % (len(actual), obj, len(expected))

    if len(expected) > 0 and type(expected[0]) in [int, float, bool, str]:
        if msg != PASS and list_compare_unordered(expected, actual, obj) == PASS:
            try:
                msg = msg + " (list may not be ordered as required)"
            except:
                pass

    return msg

def list_compare_helper(larger, smaller):
    msg = PASS
    j = 0
    for i in range(len(larger)):
        if i == len(smaller):
            msg = "expected %s" % (repr(larger[i]))
            break
        found = False
        while not found:
            if j == len(smaller):
                val = simple_compare(larger[i], smaller[j - 1], False)
                break
            val = simple_compare(larger[i], smaller[j], False)
            j += 1
            if val == PASS:
                found = True
                break
        if not found:
            msg = val
            break
    return msg


def list_compare_unordered(expected, actual, obj="list"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    try:
        sort_expected = sorted(expected)
        sort_actual = sorted(actual)
    except:
        msg = "unexpected datatype found in list; expect a list of entries of type %s" % (type(expected[0]).__name__)
        return msg

    if len(expected) > len(actual):
        msg = "in the %s, missing " % (obj) + list_compare_helper(sort_expected, sort_actual)
    elif len(expected) < len(actual):
        msg = "in the %s, found un" % (obj) + list_compare_helper(sort_actual, sort_expected)
    if len(expected) != len(actual):
        msg = msg + " (found %d entries in %s, but expected %d)" % (len(actual), obj, len(expected))
        return msg
    else:
        val = list_compare_helper(sort_expected, sort_actual)
        if val != PASS:
            msg = "in the %s, missing " % (obj) + val + ", but found un" + list_compare_helper(sort_actual, sort_expected)

    return msg

def dict_compare(expected, actual, obj="dict"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    try:
        expected_keys = sorted(list(expected.keys()))
        actual_keys = sorted(list(actual.keys()))
    except:
        msg = "unexpected datatype found in keys of dict; expect a dict with keys of type %s" % (type(expected_keys[0]).__name__)
        return msg
    val = list_compare_unordered(expected_keys, actual_keys, "dict")
    if val != PASS:
        msg = "bad keys in %s: " % (obj) + val
    if msg == PASS:
        for key in expected:
            if type(expected[key]) in [int, float, bool, str]:
                val = simple_compare(expected[key], actual[key])
            elif type(expected[key]) in [list]:
                val = list_compare_ordered(expected[key], actual[key], "value")
            elif type(expected[key]) in [dict]:
                val = dict_compare(expected[key], actual[key], "sub"+obj)
            if val != PASS:
                msg = "incorrect val for key %s in %s: " % (repr(key), obj) + val
                break
    return msg


def check_cell_html(qnum, cell):
    outputs = cell.get('outputs', [])
    if len(outputs) == 0:
        return 'no outputs in an Out[N] cell'
    actual_lines = outputs[0].get('data', {}).get('text/html', [])
    try:
        actual_cells = parse_df_html_table(''.join(actual_lines))
    except Exception as e:
        print("ERROR!  Could not find table in notebook")
        raise e

    try:
        with open('expected.html') as f:
            expected_cells = parse_df_html_table(f.read(), qnum)
    except Exception as e:
        print("ERROR!  Could not find table in expected.html")
        raise e

    return diff_df_cells(actual_cells, expected_cells)


def diff_df_cells(actual_cells, expected_cells):
    for location, expected in expected_cells.items():
        location_name = "column {} at index {}".format(location[1], location[0])
        actual = actual_cells.get(location, None)
        if actual == None:
            return 'value missing for ' + location_name
        try:
            actual_float = float(actual)
            expected_float = float(expected)
            if math.isnan(actual_float) and math.isnan(expected_float):
                return PASS
            if not math.isclose(actual_float, expected_float, rel_tol=1e-02, abs_tol=1e-02):
                print(type(actual_float), actual_float)
                return "found {} in {} but it was not close to expected {}".format(actual, location_name, expected)
        except Exception as e:
            if actual != expected:
                return "found '{}' in {} but expected '{}'".format(actual, location_name, expected)
    return PASS


def check_cell(question, cell):
    print('Checking question %d' % question.number)
    if question.format.split()[0] == TEXT_FORMAT:
        return check_cell_text(question.number, cell, question.format)
    elif question.format == HTML_FORMAT:
        return check_cell_html(question.number, cell)

    raise Exception("invalid question type")


def grade_answers(cells):
    results = {'score':0, 'tests': []}

    for question in questions:
        cell = cells.get(question.number, None)
        status = "not found"

        if question.number in cells:
            status = check_cell(question, cells[question.number])

        row = {"test": question.number, "result": status, "weight": question.weight}
        results['tests'].append(row)

    return results

def check_expected_files():
    for file in expected_files:
        if file not in os.listdir("."):
            err_msg = """Please download %s and place it in this directory for
            the tests to run correctly. You can find the file at:
            https://github.com/msyamkumar/cs220-s21-projects/tree/main/p12""" % (file)
            raise FileNotFoundError(err_msg)
    return PASS

def linter_severe_check(nb):
    issues = []
    func_names = set()
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        code = "\n".join(cell.get('source', []))
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    name = node.name
                    if name in func_names:
                        issues.append('name <%s> reused for multiple functions' % name)
                    func_names.add(name)
        except Exception as e:
            print('Linter error: ' + str(e))

    return issues


def main():
    if (sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win")):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # check if all required files are there
    check_expected_files()

    # rerun everything
    orig_notebook = 'main.ipynb'
    if len(sys.argv) > 2:
        print("Usage: test.py main.ipynb")
        return
    elif len(sys.argv) == 2:
        orig_notebook = sys.argv[1]
    if not os.path.exists(orig_notebook):
        print("File not found: " + orig_notebook)
        print("\nIf your file is named something other than main.ipynb, you can specify that by replacing '<notebook.ipynb>' with the name you chose:\n")
        print("python test.py <notebook.ipynb>")
        sys.exit(1)

    nb = rerun_notebook(orig_notebook)

    if LINTER:
        # check for sever linter errors
        issues = linter_severe_check(nb)
        if issues:
            print("\nPlease fix the following, then rerun the tests:")
            for issue in issues:
                print(' - ' + issue)
            print("")
            sys.exit(1)

    # extract cells that have answers
    answer_cells = {}
    for cell in nb['cells']:
        q = extract_question_num(cell)
        if q == None:
            continue
        if not q in question_nums:
            print('no question %d' % q)
            continue
        answer_cells[q] = cell

    # do grading on extracted answers and produce results.json
    results = grade_answers(answer_cells)
    passing = sum(t['weight'] for t in results['tests'] if t['result'] == PASS)
    total = sum(t['weight'] for t in results['tests'])

    lint_msgs = lint(orig_notebook, verbose=1, show=False)
    lint_msgs = filter(lambda msg: msg.msg_id in ALLOWED_LINT_ERRS, lint_msgs)
    lint_msgs = list(lint_msgs)
    results["lint"] = [str(l) for l in lint_msgs]

    functionality_score = 100.0 * passing / total
    linting_score = min(10.0, len(lint_msgs))
    results['score'] = max(functionality_score - linting_score, 0.0)

    print("\nSummary:")
    for test in results["tests"]:
        print("  Test %d: %s" % (test["test"], test["result"]))

    if len(lint_msgs) > 0:
        msg_types = defaultdict(list)
        for msg in lint_msgs:
            msg_types[msg.category].append(msg)
        print("\nLinting Summary:")
        for msg_type, msgs in msg_types.items():
            print('  ' + msg_type.title() + ' Messages:')
            for msg in msgs:
                print('    ' + str(msg))

    print('\nTOTAL SCORE: %.2f%%' % results['score'])
    with open('result.json', 'w') as f:
        f.write(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
