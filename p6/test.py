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
    "1": ['Entire home/apt', 'Shared room', 'Private room'],
    "2": 152.721,
    "3": 70,
    "4": ['UWS MANHATTAN APT FOR SUPERBOWL WE',
         'SuperBowl West Village Apartment',
         'SUPERBOWL!! 2 Bd, 2 Ba w Roof Deck!',
         '1500 sq ft apt sleeps 8 - SuperBowl',
         'Superbowl Studio Upper West Side',
         '1BR Superbowl rental Hells Kitchen',
         'Superbowl - NYC Apartment',
         'Tribeca Loft for Superbowl Wknd',
         'NYC SuperBowl Wk 5 Bdrs River View ',
         'Downtown NY Apt - SuperBowl Weekend',
         'SuperBowl Penthouse Loft 3,000 sqft',
         'Superbowl in the West Village',
         'SUPERBOWLSUNDAY! 3BLOCK FROM TIMESQ',
         'Super Apt for Superbowl',
         'PERFECT SUPERBOWL STAY',
         'MANHATTAN SUPERBOWL ACCOMODATION',
         'SuperBowl Weekend Rental! 3 BR/1ba'],
    "5": ['Historic Turret Retreat (Smart TV/Cable/Wifi)',
         'Explore NYC From Our Private Studio w/Free Wifi',
         'One Bedroom Mini studio - Free WIFI',
         'Huge 1bdrm w pt Doorman, WiFi/Cable, Bottled Water',
         'Cozy,budget friendly, cable inc, private entrance!',
         'Coney Island  Amphitheat  MCU 1 br  Wifi Cable **',
         'Impeccable Private one&half bedroom and full bath',
         'Luxury condo- private room + bath w cable TV/W/D',
         'BIG BEDROOM CLOSE TO LA GUARDIA AIRPORT FREE WIFI',
         'J- **LUXURY SHARED ROOM 2PPL FREE WIFI+CABLE+AC',
         'J- HOTEL STYLE SHARE ROOM FOR 2PPL FREE WIFI CABLE',
         'Coney Island MCU Park Wi fi Cable Apt****',
         '5min walk to L train - Free WiFi & Cleaning',
         'J- HOTEL STYLE SHARE ROOM FOR 2PPL FREE CABLE WIFI',
         'Private Studio: Landmark Dt (Smart TV/Wifi/Cable)',
         'J- COZY ROOM FOR 1 FEMALE FREE WIFI & COFFEE',
         'Private Bedroom in MANHATTAN (Free Wifi)',
         'Landmark 1 Bedroom has 2 beds, Free WiFi',
         'Modern and Safe Place,Free Wifi',
         'Staten Island - Free Wifi, Parking Space, Near NYC',
         'Sunny Hudson Yards/ Chelsea Studio, Free WiFi',
         '1 bedroom furnished with WIFI and cable. Murr Hill',
         'Cable and wfi, L/G included.',
         '2Bed/ 2Bath Impeccable Stylish Brooklyn Home',
         'ROOM AC WI-FI PARKING CABLE FOR 2',
         'Great Chelsea Location, Couch/2nd bed, Free WiFi',
         '*NO GUEST SERVICE FEE* Beekman Tower One Bedroom Suite with Queen Bed & Free Wifi',
         'J- LUXURY SHARED ROOM, AC FREE WIFI+CABLE GARDEN',
         'Newly renovated 2 bedroom with FREE WIFI',
         'Cozy, impeccable, sunlit West Village studio',
         'Pvt entrance lower level apt w/cable-wi-fi pvt bth',
         'J- *LUXURY SHARED ROOM AC FREE WIFI CABLE, GARDEN',
         'PRIVATE 1BR APT: Free WIFI & DIRECT TV',
         '*NO GUEST SERVICE FEE* Beekman Tower Studio with Queen Bed & Free Wifi',
         'Private 2 BR APT: Free WIFI & JACUZZI',
         'Tudor Studio (Wifi/Premium Cable) w Private Entry'],
    "6": ['Ronaldo', 'Rolando', 'Orlando'],
    "7": ['568684',
         '1615764',
         '4204302',
         '5431845',
         '6169897',
         '8341919',
         '8668115',
         '10053943',
         '11096888',
         '12888849',
         '20990053',
         '27362309',
         '30378211',
         '35834935'],
    "8": ['16098958',
         '7503643',
         '12243051',
         '200380610',
         '219517861',
         '61391963',
         '137358866',
         '22541573',
         '1475015',
         '30283594',
         '107434423'],
    "9": 2.372,
    "10": ['Huge Brooklyn Brownstone Living, Close to it all.',
         'MARTIAL LOFT 3: REDEMPTION (upstairs, 2nd room)',
         'Sunny, Quiet Room in Greenpoint',
         'Modern apartment in the heart of Williamsburg',
         'Spacious comfortable master bedroom with nice view',
         'Contemporary bedroom in brownstone with nice view',
         'Cozy yet spacious private brownstone bedroom',
         'Coliving in Brooklyn! Modern design / Shared room',
         'Best Coliving space ever! Shared room.'],
    "11": ['the best you can find'],
    "12": 1.022,
    "13": ['22463977'],
    "14": ['16276632'],
    "15": ['32363', '59121', '479285', '679633', '766964'],
    "16": 105.515,
    "17": 6.41,
    "18": 30.57,
    "19": 48.921,
    "20": 180
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
