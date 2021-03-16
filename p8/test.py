import ast, os, sys, subprocess, json, re, collections, math, warnings
import asyncio
# Resolves asyncio problem for windows users
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# check the python version
if sys.version[:5] < '3.7.0':
    warnings.warn('Your current python version is {}. Please upgrade your python version to at least 3.7.0.'.format(sys.version[:5]))

PASS = "PASS"
TEXT_FORMAT = "text" # use when expected answer is a str, int, float, or bool
TEXT_FORMAT_DICT = "text dict" # use when the expected answer is a dictionary
TEXT_FORMAT_UNORDERED_LIST = "text unordered_list" # use when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text ordered_list" # use when the expected answer is a list where the order does matter
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered" # use when the expected answer is a list of dicts where the order does matter

Question = collections.namedtuple("Question", ["number", "weight", "format"])

questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT_DICT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=4, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=5, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
    Question(number=6, weight=1, format=TEXT_FORMAT),
    Question(number=7, weight=1, format=TEXT_FORMAT),
    Question(number=8, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
    Question(number=9, weight=1, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=11, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=12, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
    Question(number=13, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
    Question(number=14, weight=1, format=TEXT_FORMAT),
    Question(number=15, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
    Question(number=16, weight=1, format=TEXT_FORMAT),
    Question(number=17, weight=1, format=TEXT_FORMAT),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT_LIST_DICTS_ORDERED),
]
question_nums = set([q.number for q in questions])

# JSON and plaintext values
expected_json = {
    "1": {'tt1233301': 'Ironclad',
             'tt0090605': 'Aliens',
             'nm0257646': 'Jonathan English',
             'nm0000299': 'Michael Biehn',
             'nm0000116': 'James Cameron',
             'nm9696871': 'Brian Cox',
             'nm0001343': 'Carrie Henn',
             'nm0700856': 'James Purefoy',
             'nm0544718': 'Kate Mara',
             'nm0000244': 'Sigourney Weaver'},
    "2": "Sigourney Weaver",
    "3": ['Jonathan English',
             'Michael Biehn',
             'James Cameron',
             'Brian Cox',
             'Carrie Henn',
             'James Purefoy',
             'Kate Mara',
             'Sigourney Weaver'],
    "4": ['nm0000116', 'nm0700856'],
    "5": [{'title': 'tt0090605',
              'year': 1986,
              'genres': ['Action', 'Adventure', 'Sci-Fi'],
              'duration': 137,
              'directors': ['nm0000116'],
              'actors': ['nm0000244', 'nm0001343', 'nm0000299'],
              'rating': 8.3},
             {'title': 'tt1233301',
              'year': 2011,
              'genres': ['Action', 'Drama', 'History'],
              'duration': 121,
              'directors': ['nm0257646'],
              'actors': ['nm0700856', 'nm9696871', 'nm0544718'],
              'rating': 6.1}],
    "6": 3,
    "7": "nm0000244",
    "8": [{'title': 'Aliens',
              'year': 1986,
              'genres': ['Action', 'Adventure', 'Sci-Fi'],
              'duration': 137,
              'directors': ['James Cameron'],
              'actors': ['Sigourney Weaver', 'Carrie Henn', 'Michael Biehn'],
              'rating': 8.3},
             {'title': 'Ironclad',
              'year': 2011,
              'genres': ['Action', 'Drama', 'History'],
              'duration': 121,
              'directors': ['Jonathan English'],
              'actors': ['James Purefoy', 'Brian Cox', 'Kate Mara'],
              'rating': 6.1}],
    "9": "Ironclad",
    "10": ['Sigourney Weaver', 'Carrie Henn', 'Michael Biehn'],
    "11": ['Jonathan English'],
    "12": [{'title': 'Evolution',
              'year': 2001,
              'genres': ['Comedy', 'Sci-Fi'],
              'duration': 101,
              'directors': ['Ivan Reitman'],
              'actors': ['David Duchovny', 'Julianne Moore'],
              'rating': 6.1},
             {'title': "Everybody's Fine",
              'year': 2009,
              'genres': ['Drama'],
              'duration': 100,
              'directors': ['Kirk Jones'],
              'actors': ['Robert De Niro',
               'Drew Barrymore',
               'Kate Beckinsale',
               'Sam Rockwell',
               'Lucian Maisel'],
              'rating': 7.1},
             {'title': 'Tales of Poe',
              'year': 2014,
              'genres': ['Fantasy', 'Horror', 'Thriller'],
              'duration': 120,
              'directors': ['Bart Mastronardi', 'Alan Rowe Kelly'],
              'actors': ['Caroline Williams', 'Debbie Rochon', 'Adrienne King'],
              'rating': 4.1},
             {'title': 'Ghostbusters II',
              'year': 1989,
              'genres': ['Action', 'Comedy', 'Fantasy'],
              'duration': 108,
              'directors': ['Ivan Reitman'],
              'actors': ['Bill Murray', 'Dan Aykroyd', 'Sigourney Weaver'],
              'rating': 6.6},
             {'title': 'Inevitable Grace',
              'year': 1994,
              'genres': ['Thriller'],
              'duration': 103,
              'directors': ['Alex Monty Canawati'],
              'actors': ['Maxwell Caulfield', 'Stephanie Knights', 'Jennifer Nicholson'],
              'rating': 4.8},
             {'title': 'Heavy Times',
              'year': 2010,
              'genres': ['Comedy'],
              'duration': 90,
              'directors': ['Benjamin Mark', 'Ryan McKenna'],
              'actors': ['Melina Bartzokis', 'Jay Brunner', 'Brian D. Evans'],
              'rating': 4.0}],
    "13": [{'title': 'Front Cover',
              'year': 2015,
              'genres': ['Comedy', 'Drama', 'Romance'],
              'duration': 87,
              'directors': ['Ray Yeung'],
              'actors': ['Jake Choi', 'James Chen', 'Jennifer Neala Page'],
              'rating': 6.3},
             {'title': 'The Ape',
              'year': 2005,
              'genres': ['Comedy', 'Drama'],
              'duration': 92,
              'directors': ['James Franco'],
              'actors': ['James Franco', 'Brian Lally', 'Allison Bibicoff'],
              'rating': 4.5},
             {'title': 'Eastside',
              'year': 1999,
              'genres': ['Drama', 'Crime'],
              'duration': 94,
              'directors': ['Lorena David'],
              'actors': ['Mario Lopez', 'Elizabeth Bogush', 'Mark D. Espinoza'],
              'rating': 4.4}],
    "14": 849,
    "15": [{'title': 'Oh! Calcutta!',
              'year': 1972,
              'genres': ['Comedy', 'Musical'],
              'duration': 123,
              'directors': ['Jacques Levy'],
              'actors': ['Raina Barrett', 'Mark Dempsey', 'Samantha Harper'],
              'rating': 5.3},
             {'title': 'The Cowboys',
              'year': 1972,
              'genres': ['Adventure', 'Drama', 'Western'],
              'duration': 134,
              'directors': ['Mark Rydell'],
              'actors': ['John Wayne', 'Roscoe Lee Browne', 'Bruce Dern'],
              'rating': 7.4},
             {'title': 'Sleuth',
              'year': 1972,
              'genres': ['Mystery', 'Thriller'],
              'duration': 138,
              'directors': ['Joseph L. Mankiewicz'],
              'actors': ['Laurence Olivier', 'Michael Caine', 'Alec Cawthorne'],
              'rating': 8.0},
             {'title': 'The Great Waltz',
              'year': 1972,
              'genres': ['Biography', 'Drama', 'Music'],
              'duration': 135,
              'directors': ['Andrew L. Stone'],
              'actors': ['Horst Buchholz',
               'Mary Costa',
               'Nigel Patrick',
               'Yvonne Mitchell'],
              'rating': 5.2},
             {'title': 'Bluebeard',
              'year': 1972,
              'genres': ['Crime', 'Drama', 'Thriller'],
              'duration': 125,
              'directors': ['Edward Dmytryk'],
              'actors': ['Richard Burton', 'Raquel Welch', 'Virna Lisi'],
              'rating': 5.7},
             {'title': 'Cabaret',
              'year': 1972,
              'genres': ['Drama', 'Musical'],
              'duration': 124,
              'directors': ['Bob Fosse'],
              'actors': ['Liza Minnelli', 'Michael York', 'Helmut Griem', 'Joel Grey'],
              'rating': 7.8},
             {'title': 'Man of La Mancha',
              'year': 1972,
              'genres': ['Drama', 'Fantasy', 'Musical'],
              'duration': 132,
              'directors': ['Arthur Hiller'],
              'actors': ["Peter O'Toole", 'Sophia Loren', 'James Coco'],
              'rating': 6.7},
             {'title': 'The Godfather',
              'year': 1972,
              'genres': ['Crime', 'Drama'],
              'duration': 175,
              'directors': ['Francis Ford Coppola'],
              'actors': ['Marlon Brando', 'Al Pacino', 'James Caan'],
              'rating': 9.2},
             {'title': 'The Getaway',
              'year': 1972,
              'genres': ['Action', 'Crime', 'Thriller'],
              'duration': 123,
              'directors': ['Sam Peckinpah'],
              'actors': ['Steve McQueen',
               'Ali MacGraw',
               'Ben Johnson',
               'Sally Struthers',
               'Al Lettieri'],
              'rating': 7.4},
             {'title': 'Lady Sings the Blues',
              'year': 1972,
              'genres': ['Biography', 'Drama', 'Music'],
              'duration': 144,
              'directors': ['Sidney J. Furie'],
              'actors': ['Diana Ross', 'Billy Dee Williams', 'Richard Pryor'],
              'rating': 7.1},
             {'title': 'Avanti!',
              'year': 1972,
              'genres': ['Comedy', 'Romance'],
              'duration': 144,
              'directors': ['Billy Wilder'],
              'actors': ['Jack Lemmon', 'Juliet Mills'],
              'rating': 7.2},
             {'title': 'Hungry Wives',
              'year': 1972,
              'genres': ['Drama'],
              'duration': 130,
              'directors': ['George A. Romero'],
              'actors': ['Jan White', 'Raymond Laine', 'Ann Muffly'],
              'rating': 5.5},
             {'title': '1776',
              'year': 1972,
              'genres': ['Drama', 'Family', 'History'],
              'duration': 141,
              'directors': ['Peter H. Hunt'],
              'actors': ['William Daniels',
               'Howard Da Silva',
               'Ken Howard',
               'Donald Madden'],
              'rating': 7.6}],
    "16": 24,
    "17": 38756,
    "18": 14233,
    "19": 94.6424,
    "20": [{'title': 'The Tourist',
              'year': 2010,
              'genres': ['Action', 'Adventure', 'Crime'],
              'duration': 103,
              'directors': ['Florian Henckel von Donnersmarck'],
              'actors': ['Johnny Depp', 'Angelina Jolie', 'Paul Bettany'],
              'rating': 6.0}],
    }

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
    cmds = ['py', 'python3', 'python']
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
    actual_lines = outputs[0].get('data', {}).get('text/plain', [])
    actual = ''.join(actual_lines)
    actual = ast.literal_eval(actual)
    expected = expected_json[str(qnum)]

    if type(expected) != type(actual):
        return "expected an answer of type %s but found one of type %s" % (type(expected), type(actual))

    if format == TEXT_FORMAT:
        if type(expected) == float:
            if not math.isclose(actual, expected, rel_tol=1e-06, abs_tol=15e-05):
                return "expected %s but found %s" % (str(expected), str(actual))
        else:
            if expected != actual:
                return "expected %s but found %s" % (str(expected), repr(actual))
    elif format == TEXT_FORMAT_UNORDERED_LIST:
        try:
            extra = set(actual) - set(expected)
            missing = set(expected) - set(actual)
            if missing:
                return "missing %d entries from list, such as: %s" % (len(missing), repr(list(missing)[0]))
            elif extra:
                return "found unexpected entry in list: %s" % repr(list(extra)[0])
            elif len(actual) != len(expected):
                return "expected %d entries in the list but found %d" % (len(expected), len(actual))
        except TypeError:
            # Just do a simple comparison
            if actual != expected:
                return "expected %s" % repr(expected)
    elif format == TEXT_FORMAT_ORDERED_LIST:
        try:
            extra = set(actual) - set(expected)
            missing = set(expected) - set(actual)
            if missing:
                return "missing %d entries from list, such as: %s" % (len(missing), repr(list(missing)[0]))
            elif extra:
                return "found unexpected entry in list: %s" % repr(list(extra)[0])
            elif len(actual) != len(expected):
                return "expected %d entries in the list but found %d" % (len(expected), len(actual))
            elif expected != actual:
                if sorted(expected) == sorted(actual):
                    return "list not sorted as expected"
                for i in range(len(expected)):
                    if type(expected[i]) != type(actual[i]):
                        return "expected an element of type %s at index %d of the list, but found one of type %s" % (type(expected[i]), i, type(actual[i]))
                    elif expected[i] != actual[i]:
                        return "expected %s at index %d of the list, but found %s" % (repr(expected[i]), i, repr(actual[i]))
        except TypeError:
            # Just do a simple comparison
            if actual != expected:
                return "expected %s" % repr(expected)
    elif format == TEXT_FORMAT_DICT:
        missing_keys = set(expected.keys()) - set(actual.keys())
        extra_keys = set(actual.keys()) - set(expected.keys())
        if missing_keys:
            key = list(missing_keys)[0]
            return "missing %d key value pairs (%s: %s) from dict" % (len(missing_keys), repr(key), repr(expected[key]))
        elif extra_keys:
            key = list(extra_keys)[0]
            return "found unexpected key value pair (%s: %s) in dict" % (repr(key), repr(actual[key]))
        for key in expected:
            if type(expected[key]) != type(actual[key]):
                return "expected a value of type %s for the key %s, but found %s" % (type(expected[key]), repr(key), type(actual[key]))
            elif expected[key] != actual[key]:
                if type(expected[key]) == list:
                    extra = set(actual[key]) - set(expected[key])
                    missing = set(expected[key]) - set(actual[key])
                    if missing:
                        return "missing %d entries from value for key %s, such as: %s" % (len(missing), repr(key), repr(list(missing)[0]))
                    elif extra:
                        return "found unexpected entry %s in the value for key %s" % (repr(list(extra)[0]), repr(key))
                    elif len(actual[key]) != len(expected[key]):
                        return "expected %d entries in the value for key %s, but found %d" % (len(expected[key]), repr(key), len(actual[key]))
                    elif sorted(expected[key]) == sorted(actual[key]):
                        return "value of key %s not sorted as expected" % (repr(key))
                return "expected value %s for the key %s, but found %s" % (repr(expected[key]), repr(key), repr(actual[key]))
    elif format == TEXT_FORMAT_LIST_DICTS_ORDERED:
        try:
            if len(expected) < len(actual):
                for extra in actual:
                    if extra not in expected:
                        return "found unexpected entry in list: %s" % repr(extra)
                return "expected %d entries in the list but found %d" % (len(expected), len(actual))
            elif len(expected) > len(actual):
                for missing in expected:
                    if missing not in actual:
                        return "missing entries from list, such as %s" % repr(missing)
                return "expected %d entries in the list but found %d" % (len(expected), len(actual))
            for i in range(len(expected)):
                expected_dict = expected[i]
                actual_dict = actual[i]
                if type(actual_dict) != type(expected_dict):
                    return "expected a list of %s but found one of type %s at index %d" % (type(expected_dict), type(actual_dict), i)
                missing_keys = set(expected_dict.keys()) - set(actual_dict.keys())
                extra_keys = set(actual_dict.keys()) - set(expected_dict.keys())
                if missing_keys:
                    key = list(missing_keys)[0]
                    return "missing %d key value pairs (%s: %s) from dict at index %d of the list" % (len(missing_keys), repr(key), repr(expected_dict[key]), i)
                elif extra_keys:
                    key = list(extra_keys)[0]
                    return "found unexpected key value pair (%s: %s) in dict at index %d of the list" % (repr(key), repr(actual_dict[key]), i)
                for key in expected_dict:
                    if type(expected_dict[key]) != type(actual_dict[key]):
                        return "expected a value of type %s for the key %s in dict at index %d of the list, but found %s" % (type(expected_dict[key]), repr(key), i, type(actual_dict[key]))
                    if expected_dict[key] != actual_dict[key]:
                        if type(expected_dict[key]) == list:
                            extra = set(actual_dict[key]) - set(expected_dict[key])
                            missing = set(expected_dict[key]) - set(actual_dict[key])
                            if missing:
                                return "missing %d entries from value for key %s, such as %s, at index %d of the list" % (len(missing), repr(key), repr(list(missing)[0]), i)
                            elif extra:
                                return "found unexpected entry %s in the value for key %s at index %d of the list" % (repr(list(extra)[0]), repr(key), i)
                            elif len(actual_dict[key]) != len(expected_dict[key]):
                                return "expected %d entries in the value for key %s but found %d, at index %d of the list" % (len(expected_dict[key]), repr(key), len(actual_dict[key]), i)
                            elif sorted(expected_dict[key]) == sorted(actual_dict[key]):
                                return "value of key %s not sorted as expected" % (repr(key))
                        return "expected value %s for the key %s in dict at index %d of the list, but found %s" % (repr(expected_dict[key]), repr(key), i, repr(actual_dict[key]))
        except:
            # Just do a simple comparison
            if actual != expected:
                return "expected %s" % repr(expected)
    else:
        if expected != actual:
            return "expected %s" % repr(expected)
    return PASS


def check_cell(question, cell):
    print('Checking question %d' % question.number)
    if question.format.split()[0] == TEXT_FORMAT:
        return check_cell_text(question.number, cell, question.format)

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

    if (
        sys.version_info[0] == 3
        and sys.version_info[1] >= 8
        and sys.platform.startswith("win")
        ):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
    results['score'] = 100.0 * passing / total

    print("\nSummary:")
    for test in results["tests"]:
        print("  Test %d: %s" % (test["test"], test["result"]))

    print('\nTOTAL SCORE: %.2f%%' % results['score'])
    with open('result.json', 'w') as f:
        f.write(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
