import ast
import os
import re
import sys
import json
import math
import collections
import nbconvert
import nbformat
import warnings
import asyncio
# Resolves asyncio problem for windows users
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# check the python version
if sys.version[:5] < '3.7.0':
    warnings.warn('Your current python version is {}. Please upgrade your python version to at least 3.7.0.'.format(sys.version[:5]))


PASS = "PASS"
TEXT_FORMAT = "text"

Question = collections.namedtuple("Question", ["number", "weight", "format"])

questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT),
    Question(number=4, weight=1, format=TEXT_FORMAT),
    Question(number=5, weight=1, format=TEXT_FORMAT),
    Question(number=6, weight=1, format=TEXT_FORMAT),
    Question(number=7, weight=1, format=TEXT_FORMAT),
    Question(number=8, weight=1, format=TEXT_FORMAT),
    Question(number=9, weight=1, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT),
    Question(number=12, weight=1, format=TEXT_FORMAT),
    Question(number=13, weight=1, format=TEXT_FORMAT),
    Question(number=14, weight=1, format=TEXT_FORMAT),
    Question(number=15, weight=1, format=TEXT_FORMAT),
    Question(number=16, weight=1, format=TEXT_FORMAT),
    Question(number=17, weight=1, format=TEXT_FORMAT),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT),
]
question_nums = set([q.number for q in questions])

# JSON and plaintext values
expected_json = {
    "1": 'Norway',
    "2": 'Qatar',
    "3": 'Europe',
    "4": 196,
    "5": ['2021-02-10',
          '2021-02-11',
          '2021-02-12',
          '2021-02-13',
          '2021-02-14',
          '2021-02-15',
          '2021-02-16'],
    "6": 27684220,
    "7": [1439323774, 1380004385, 331002647, 273523621, 220892331],
    "8": [116935.6, 94277.965, 85535.383, 71809.251, 67335.293],
    "9": ['Covaxin',
         'Moderna',
         'Oxford/AstraZeneca',
         'Pfizer/BioNTech',
         'Sinopharm/Beijing',
         'Sinovac',
         'Sputnik V'],
    "10": {'Afghanistan': 0,
          'Albania': 0,
          'Algeria': 0,
          'Andorra': 1291,
          'Angola': 0,
          'Anguilla': 1341,
          'Antigua and Barbuda': 0,
          'Argentina': 611169,
          'Armenia': 0,
          'Australia': 0,
          'Austria': 378205,
          'Azerbaijan': 0,
          'Bahamas': 0,
          'Bahrain': 252990,
          'Bangladesh': 1359613,
          'Barbados': 0,
          'Belarus': 0,
          'Belgium': 573774,
          'Belize': 0,
          'Benin': 0,
          'Bermuda': 13155,
          'Bhutan': 0,
          'Bolivia': 10167,
          'Bosnia and Herzegovina': 0,
          'Botswana': 0,
          'Brazil': 5609937,
          'Brunei': 0,
          'Bulgaria': 81338,
          'Burkina Faso': 0,
          'Burundi': 0,
          'Cambodia': 1492,
          'Cameroon': 0,
          'Canada': 1306784,
          'Cape Verde': 0,
          'Cayman Islands': 15543,
          'Central African Republic': 0,
          'Chad': 0,
          'Chile': 2375725,
          'China': 0,
          'Colombia': 0,
          'Comoros': 0,
          'Congo': 0,
          'Costa Rica': 96948,
          "Cote d'Ivoire": 0,
          'Croatia': 120603,
          'Cuba': 0,
          'Cyprus': 55673,
          'Czechia': 466578,
          'Democratic Republic of Congo': 0,
          'Denmark': 421827,
          'Djibouti': 0,
          'Dominica': 0,
          'Dominican Republic': 0,
          'Ecuador': 0,
          'Egypt': 0,
          'El Salvador': 0,
          'Equatorial Guinea': 0,
          'Eritrea': 0,
          'Estonia': 69313,
          'Eswatini': 0,
          'Ethiopia': 0,
          'Faeroe Islands': 5355,
          'Fiji': 0,
          'Finland': 283926,
          'France': 3014973,
          'Gabon': 0,
          'Gambia': 0,
          'Georgia': 0,
          'Germany': 4284554,
          'Ghana': 0,
          'Gibraltar': 26379,
          'Greece': 575766,
          'Grenada': 0,
          'Guatemala': 0,
          'Guinea': 0,
          'Guinea-Bissau': 0,
          'Guyana': 668,
          'Haiti': 0,
          'Honduras': 0,
          'Hungary': 483751,
          'Iceland': 20031,
          'India': 8999230,
          'Indonesia': 1658110,
          'Iran': 0,
          'Iraq': 0,
          'Ireland': 268551,
          'Isle of Man': 14272,
          'Israel': 6758861,
          'Italy': 3122631,
          'Jamaica': 0,
          'Japan': 0,
          'Jordan': 0,
          'Kazakhstan': 0,
          'Kenya': 0,
          'Kosovo': 0,
          'Kuwait': 137000,
          'Kyrgyzstan': 0,
          'Laos': 0,
          'Latvia': 39299,
          'Lebanon': 0,
          'Lesotho': 0,
          'Liberia': 0,
          'Libya': 0,
          'Liechtenstein': 1165,
          'Lithuania': 157304,
          'Luxembourg': 24024,
          'Madagascar': 0,
          'Malawi': 0,
          'Malaysia': 0,
          'Maldives': 50047,
          'Mali': 0,
          'Malta': 53647,
          'Marshall Islands': 0,
          'Mauritania': 0,
          'Mauritius': 0,
          'Mexico': 915383,
          'Micronesia (country)': 0,
          'Moldova': 0,
          'Monaco': 0,
          'Mongolia': 0,
          'Montenegro': 0,
          'Morocco': 1904169,
          'Mozambique': 0,
          'Myanmar': 0,
          'Namibia': 0,
          'Nepal': 0,
          'Netherlands': 623539,
          'New Zealand': 0,
          'Nicaragua': 0,
          'Niger': 0,
          'Nigeria': 0,
          'North Macedonia': 0,
          'Norway': 304780,
          'Oman': 109014,
          'Pakistan': 27228,
          'Palestine': 0,
          'Panama': 12441,
          'Papua New Guinea': 0,
          'Paraguay': 0,
          'Peru': 109498,
          'Philippines': 0,
          'Poland': 2159146,
          'Portugal': 539786,
          'Qatar': 0,
          'Romania': 1197089,
          'Russia': 3900000,
          'Rwanda': 0,
          'Saint Kitts and Nevis': 0,
          'Saint Lucia': 0,
          'Saint Vincent and the Grenadines': 0,
          'Samoa': 0,
          'San Marino': 0,
          'Sao Tome and Principe': 0,
          'Saudi Arabia': 462812,
          'Senegal': 0,
          'Serbia': 817000,
          'Seychelles': 55980,
          'Sierra Leone': 0,
          'Singapore': 256000,
          'Slovakia': 311299,
          'Slovenia': 119346,
          'Solomon Islands': 0,
          'Somalia': 0,
          'South Africa': 0,
          'South Korea': 0,
          'South Sudan': 0,
          'Spain': 2624512,
          'Sri Lanka': 196163,
          'Sudan': 0,
          'Suriname': 0,
          'Sweden': 505898,
          'Switzerland': 540066,
          'Syria': 0,
          'Taiwan': 0,
          'Tajikistan': 0,
          'Tanzania': 0,
          'Thailand': 0,
          'Timor': 0,
          'Togo': 0,
          'Trinidad and Tobago': 0,
          'Tunisia': 0,
          'Turkey': 4630784,
          'Uganda': 0,
          'Ukraine': 0,
          'United Arab Emirates': 5198725,
          'United Kingdom': 16122272,
          'United States': 55220364,
          'Uruguay': 0,
          'Uzbekistan': 0,
          'Vanuatu': 0,
          'Vatican': 0,
          'Venezuela': 0,
          'Vietnam': 0,
          'Yemen': 0,
          'Zambia': 0,
          'Zimbabwe': 0},
    "11": 'United States',
    "12": ['Afghanistan',
           'Albania',
           'Algeria',
           'Angola',
           'Antigua and Barbuda',
           'Armenia',
           'Australia',
           'Azerbaijan',
           'Bahamas',
           'Barbados',
           'Belarus',
           'Belize',
           'Benin',
           'Bhutan',
           'Bosnia and Herzegovina',
           'Botswana',
           'Brunei',
           'Burkina Faso',
           'Burundi',
           'Cameroon',
           'Cape Verde',
           'Central African Republic',
           'Chad',
           'China',
           'Colombia',
           'Comoros',
           'Congo',
           "Cote d'Ivoire",
           'Cuba',
           'Democratic Republic of Congo',
           'Djibouti',
           'Dominica',
           'Dominican Republic',
           'Ecuador',
           'Egypt',
           'El Salvador',
           'Equatorial Guinea',
           'Eritrea',
           'Eswatini',
           'Ethiopia',
           'Fiji',
           'Gabon',
           'Gambia',
           'Georgia',
           'Ghana',
           'Grenada',
           'Guatemala',
           'Guinea',
           'Guinea-Bissau',
           'Haiti',
           'Honduras',
           'Iran',
           'Iraq',
           'Jamaica',
           'Japan',
           'Jordan',
           'Kazakhstan',
           'Kenya',
           'Kosovo',
           'Kyrgyzstan',
           'Laos',
           'Lebanon',
           'Lesotho',
           'Liberia',
           'Libya',
           'Madagascar',
           'Malawi',
           'Malaysia',
           'Mali',
           'Marshall Islands',
           'Mauritania',
           'Mauritius',
           'Micronesia (country)',
           'Moldova',
           'Monaco',
           'Mongolia',
           'Montenegro',
           'Mozambique',
           'Myanmar',
           'Namibia',
           'Nepal',
           'New Zealand',
           'Nicaragua',
           'Niger',
           'Nigeria',
           'North Macedonia',
           'Palestine',
           'Papua New Guinea',
           'Paraguay',
           'Philippines',
           'Qatar',
           'Rwanda',
           'Saint Kitts and Nevis',
           'Saint Lucia',
           'Saint Vincent and the Grenadines',
           'Samoa',
           'San Marino',
           'Sao Tome and Principe',
           'Senegal',
           'Sierra Leone',
           'Solomon Islands',
           'Somalia',
           'South Africa',
           'South Korea',
           'South Sudan',
           'Sudan',
           'Suriname',
           'Syria',
           'Taiwan',
           'Tajikistan',
           'Tanzania',
           'Thailand',
           'Timor',
           'Togo',
           'Trinidad and Tobago',
           'Tunisia',
           'Uganda',
           'Ukraine',
           'Uruguay',
           'Uzbekistan',
           'Vanuatu',
           'Vatican',
           'Venezuela',
           'Vietnam',
           'Yemen',
           'Zambia',
           'Zimbabwe'],
    "13": {'country': 'United States',
           'continent': 'North America',
           'date': '2021-02-16',
           'new_vaccinations': 0,
           'total_vaccinations': 55220364,
           'people_fully_vaccinated': 15015434,
           'vaccine_used': 'Moderna',
           'population': 331002647,
           'population_density': 35.608,
           'gdp_per_capita': 54225.446,
           'human_development_index': 0.926},
    "14": {'country': 'India',
           'continent': 'Asia',
           'date': '2021-02-14',
           'new_vaccinations': 21437,
           'total_vaccinations': 8285295,
           'people_fully_vaccinated': 0,
           'vaccine_used': 'Covaxin',
           'population': 1380004385,
           'population_density': 450.419,
           'gdp_per_capita': 6426.674,
           'human_development_index': 0.645},
    "15": 'Moderna',
    "16": {'2021-02-10': 4611211,
           '2021-02-11': 4638600,
           '2021-02-12': 5429665,
           '2021-02-13': 4715774,
           '2021-02-14': 3383538,
           '2021-02-15': 2465118,
           '2021-02-16': 2440314},
    "17": {'Afghanistan': 0.0,
           'Albania': 0.0,
           'Algeria': 0.0,
           'Andorra': 0.0,
           'Angola': 0.0,
           'Anguilla': 0.0,
           'Antigua and Barbuda': 0.0,
           'Argentina': 0.5264120141136195,
           'Armenia': 0.0,
           'Australia': 0.0,
           'Austria': 1.6818817729614497,
           'Azerbaijan': 0.0,
           'Bahamas': 0.0,
           'Bahrain': 0.0,
           'Bangladesh': 0.0,
           'Barbados': 0.0,
           'Belarus': 0.0,
           'Belgium': 1.7580824075620796,
           'Belize': 0.0,
           'Benin': 0.0,
           'Bermuda': 0.0,
           'Bhutan': 0.0,
           'Bolivia': 0.0,
           'Bosnia and Herzegovina': 0.0,
           'Botswana': 0.0,
           'Brazil': 0.1343718451908191,
           'Brunei': 0.0,
           'Bulgaria': 0.32778556928924385,
           'Burkina Faso': 0.0,
           'Burundi': 0.0,
           'Cambodia': 0.0,
           'Cameroon': 0.0,
           'Canada': 0.0,
           'Cape Verde': 0.0,
           'Cayman Islands': 9.694157029823494,
           'Central African Republic': 0.0,
           'Chad': 0.0,
           'Chile': 0.28786042253461447,
           'China': 0.0,
           'Colombia': 0.0,
           'Comoros': 0.0,
           'Congo': 0.0,
           'Costa Rica': 0.8353366257606328,
           "Cote d'Ivoire": 0.0,
           'Croatia': 1.285616432349849,
           'Cuba': 0.0,
           'Cyprus': 1.5983578015273452,
           'Czechia': 1.6179782541421772,
           'Democratic Republic of Congo': 0.0,
           'Denmark': 2.961343033039415,
           'Djibouti': 0.0,
           'Dominica': 0.0,
           'Dominican Republic': 0.0,
           'Ecuador': 0.0,
           'Egypt': 0.0,
           'El Salvador': 0.0,
           'Equatorial Guinea': 0.0,
           'Eritrea': 0.0,
           'Estonia': 1.7016461634373359,
           'Eswatini': 0.0,
           'Ethiopia': 0.0,
           'Faeroe Islands': 2.498720965926532,
           'Fiji': 0.0,
           'Finland': 1.2175858796639714,
           'France': 1.0982816429426994,
           'Gabon': 0.0,
           'Gambia': 0.0,
           'Georgia': 0.0,
           'Germany': 1.7554938478965152,
           'Ghana': 0.0,
           'Gibraltar': 30.405746341752995,
           'Greece': 1.707042541074326,
           'Grenada': 0.0,
           'Guatemala': 0.0,
           'Guinea': 0.0,
           'Guinea-Bissau': 0.0,
           'Guyana': 0.0,
           'Haiti': 0.0,
           'Honduras': 0.0,
           'Hungary': 1.3956430150046324,
           'Iceland': 1.741831501831502,
           'India': 0.0,
           'Indonesia': 0.19638048006098896,
           'Iran': 0.0,
           'Iraq': 0.0,
           'Ireland': 1.8555849613876314,
           'Isle of Man': 4.226644086931978,
           'Israel': 31.047961069100126,
           'Italy': 2.142697372629885,
           'Jamaica': 0.0,
           'Japan': 0.0,
           'Jordan': 0.0,
           'Kazakhstan': 0.0,
           'Kenya': 0.0,
           'Kosovo': 0.0,
           'Kuwait': 0.0,
           'Kyrgyzstan': 0.0,
           'Laos': 0.0,
           'Latvia': 0.8703203580528491,
           'Lebanon': 0.0,
           'Lesotho': 0.0,
           'Liberia': 0.0,
           'Libya': 0.0,
           'Liechtenstein': 0.0,
           'Lithuania': 2.022267274145196,
           'Luxembourg': 0.9535509348601223,
           'Madagascar': 0.0,
           'Malawi': 0.0,
           'Malaysia': 0.0,
           'Maldives': 0.0,
           'Mali': 0.0,
           'Malta': 3.873270537823386,
           'Marshall Islands': 0.0,
           'Mauritania': 0.0,
           'Mauritius': 0.0,
           'Mexico': 0.0668550061907078,
           'Micronesia (country)': 0.0,
           'Moldova': 0.0,
           'Monaco': 0.0,
           'Mongolia': 0.0,
           'Montenegro': 0.0,
           'Morocco': 0.0,
           'Mozambique': 0.0,
           'Myanmar': 0.0,
           'Namibia': 0.0,
           'Nepal': 0.0,
           'Netherlands': 0.0,
           'New Zealand': 0.0,
           'Nicaragua': 0.0,
           'Niger': 0.0,
           'Nigeria': 0.0,
           'North Macedonia': 0.0,
           'Norway': 1.3173733989369965,
           'Oman': 0.37243798346539064,
           'Pakistan': 0.0,
           'Palestine': 0.0,
           'Panama': 0.0,
           'Papua New Guinea': 0.0,
           'Paraguay': 0.0,
           'Peru': 0.0,
           'Philippines': 0.0,
           'Poland': 1.7392180883859991,
           'Portugal': 1.993643634165422,
           'Qatar': 0.0,
           'Romania': 2.5020737945455176,
           'Russia': 1.1649064929558104,
           'Rwanda': 0.0,
           'Saint Kitts and Nevis': 0.0,
           'Saint Lucia': 0.0,
           'Saint Vincent and the Grenadines': 0.0,
           'Samoa': 0.0,
           'San Marino': 0.0,
           'Sao Tome and Principe': 0.0,
           'Saudi Arabia': 0.0,
           'Senegal': 0.0,
           'Serbia': 2.6746628308278697,
           'Seychelles': 14.420378279438681,
           'Sierra Leone': 0.0,
           'Singapore': 0.10255808932912139,
           'Slovakia': 1.27105380333476,
           'Slovenia': 2.301710686063806,
           'Solomon Islands': 0.0,
           'Somalia': 0.0,
           'South Africa': 0.0,
           'South Korea': 0.0,
           'South Sudan': 0.0,
           'Spain': 2.3461171876254885,
           'Sri Lanka': 0.0,
           'Sudan': 0.0,
           'Suriname': 0.0,
           'Sweden': 1.4038440402128074,
           'Switzerland': 0.0,
           'Syria': 0.0,
           'Taiwan': 0.0,
           'Tajikistan': 0.0,
           'Tanzania': 0.0,
           'Thailand': 0.0,
           'Timor': 0.0,
           'Togo': 0.0,
           'Trinidad and Tobago': 0.0,
           'Tunisia': 0.0,
           'Turkey': 0.766147911026808,
           'Uganda': 0.0,
           'Ukraine': 0.0,
           'United Arab Emirates': 0.0,
           'United Kingdom': 0.8045325513636065,
           'United States': 4.536348617175863,
           'Uruguay': 0.0,
           'Uzbekistan': 0.0,
           'Vanuatu': 0.0,
           'Vatican': 0.0,
           'Venezuela': 0.0,
           'Vietnam': 0.0,
           'Yemen': 0.0,
           'Zambia': 0.0,
           'Zimbabwe': 0.0},
    "18": ['Austria',
           'Belgium',
           'Bulgaria',
           'Canada',
           'Czechia',
           'Denmark',
           'Estonia',
           'Finland',
           'France',
           'Germany',
           'Greece',
           'Iceland',
           'Ireland',
           'Israel',
           'Italy',
           'Latvia',
           'Liechtenstein',
           'Lithuania',
           'Luxembourg',
           'Netherlands',
           'Norway',
           'Poland',
           'Portugal',
           'Romania',
           'Spain',
           'Switzerland',
           'United States'],
    "19": {'Pfizer/BioNTech': ['Albania',
            'Andorra',
            'Bahrain',
            'Bermuda',
            'Cayman Islands',
            'Chile',
            'Costa Rica',
            'Croatia',
            'Cyprus',
            'Ecuador',
            'Faeroe Islands',
            'Gibraltar',
            'Hungary',
            'Kuwait',
            'Malta',
            'Mexico',
            'Monaco',
            'Panama',
            'Qatar',
            'Saudi Arabia',
            'Serbia',
            'Singapore',
            'Slovakia'],
           'Sputnik V': ['Algeria', 'Argentina', 'Bolivia', 'Iran', 'Russia'],
           'Oxford/AstraZeneca': ['Anguilla',
            'Azerbaijan',
            'Bangladesh',
            'Brazil',
            'Guyana',
            'Isle of Man',
            'Maldives',
            'Mauritius',
            'Morocco',
            'Myanmar',
            'Nepal',
            'Oman',
            'Pakistan',
            'Seychelles',
            'Slovenia',
            'Sri Lanka',
            'Sweden',
            'United Arab Emirates',
            'United Kingdom'],
           'Moderna': ['Austria',
            'Belgium',
            'Bulgaria',
            'Canada',
            'Czechia',
            'Denmark',
            'Estonia',
            'Finland',
            'France',
            'Germany',
            'Greece',
            'Iceland',
            'Ireland',
            'Israel',
            'Italy',
            'Latvia',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Netherlands',
            'Norway',
            'Poland',
            'Portugal',
            'Romania',
            'Spain',
            'Switzerland',
            'United States'],
           'Sinopharm/Beijing': ['Cambodia', 'China', 'Egypt', 'Peru'],
           'Covaxin': ['India'],
           'Sinovac': ['Indonesia', 'Turkey']},
    "20": 'Moderna',
}

# find a comment something like this: #q10
def extract_question_num(cell):
    for line in cell.get('source', []):
        line = line.strip().replace(' ', '').lower()
        m = re.match(r'\#q(\d+)', line)
        if m:
            return int(m.group(1))
    return None


# rerun notebook and return parsed JSON
def rerun_notebook(orig_notebook):
    new_notebook = 'cs-220-test.ipynb'

    # re-execute it from the beginning
    with open(orig_notebook, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    ep = nbconvert.preprocessors.ExecutePreprocessor(timeout=120, kernel_name='python3')
    try:
        out = ep.preprocess(nb, {'metadata': {'path': os.getcwd()}})
    except nbconvert.preprocessors.CellExecutionError:
        out = None
        msg = 'Error executing the notebook "%s".\n\n' % orig_notebook
        msg += 'See notebook "%s" for the traceback.' % new_notebook
        print(msg)
        raise
    finally:
        with open(new_notebook, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)

    # Note: Here we are saving and reloading, this isn't needed but can help student's debug

    # parse notebook
    with open(new_notebook, encoding='utf-8') as f:
        nb = json.load(f)
    return nb


def normalize_json(orig):
    try:
        return json.dumps(json.loads(orig.strip("'")), indent=2, sort_keys=True)
    except:
        return 'not JSON'


def check_cell_text(qnum, cell):
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

    expected_mismatch = False

    if type(expected) != type(actual):
        return "expected an answer of type %s but found one of type %s" % (type(expected), type(actual))
    elif type(expected) == float:
        if not math.isclose(actual, expected, rel_tol=1e-06, abs_tol=1e-06):
            expected_mismatch = True
    elif type(expected) == list:
        extra = set(actual) - set(expected)
        missing = set(expected) - set(actual)
        if extra:
            return "found unexpected entry in list: %s" % repr(list(extra)[0])
        elif missing:
            return "missing %d entries list, such as: %s" % (len(missing), repr(list(missing)[0]))
        elif len(actual) != len(expected):
            return "expected %d entries in the list but found %d" % (len(expected), len(actual))
    else:
        if expected != actual:
            expected_mismatch = True

    if expected_mismatch:
        return "found {} in cell {} but expected {}".format(actual, qnum, expected)

    return PASS


def check_cell(question, cell):
    print('Checking question %d' % question.number)
    if question.format == TEXT_FORMAT:
        return check_cell_text(question.number, cell)

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


def main():
    # rerun everything
    orig_notebook = 'main.ipynb'
    if len(sys.argv) > 2:
        print("Usage: test.py main.ipynb")
        return
    elif len(sys.argv) == 2:
        orig_notebook = sys.argv[1]
    nb = rerun_notebook(orig_notebook)

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
    results['score'] = 100.0 * passing / total

    print("\nSummary:")
    for test in results["tests"]:
        print("  Test %d: %s" % (test["test"], test["result"]))

    print('\nTOTAL SCORE: %.2f%%' % results['score'])
    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
