# Project 12: Geography, and the World Wide Web

## Clarifications/Corrections

None yet.

**Find any issues?** Report to us: 

- Liang Shang <lshang6@wisc.edu>
- Ashwin Maran <amaran@wisc.edu>

## Learning Objectives

In this project, you will

- Gain more experience with reading and writing files
- Practice using a linter with your code
- Practice using Pandas with python
- Practice creating DataFrames

## Coding Style Requirements

Remember that coding style matters! **We might deduct points for bad coding style.** Here are a list of coding style requirements:

- Do not use meaningless names for variables or functions (e.g. uuu = "my name").
- Do not write the exact same code in multiple places. Instead, wrap this code into a function and call that function whenever the code should be used.
- Do not call unnecessary functions.
- Avoid using slow functions multiple times within a loop.
- Avoid inappropriate use of data structures. A bad example: use for loop to search for a corresponding value in a dictionary with a given key instead of use `dictname[key]` directly.
- Do not name variables or functions as python keywords or built-in functions. Bad example: str = "23".
- Do not define multiple functions with the same name or define multiple versions of one function with different names. Just keep the best version.
- Put all `import` commands together at the second cell of `main.ipynb`, the first cell should be submission information (netid and etc).
- Think twice before creating a function without any parameters. Defining new functions is unnecessary sometimes. The advantage of writing functions is that we can reuse the same code. If we only use this function once, there is no need to create a new function.
- Do not use absolute path such as `C://Desktop//220`. **You may only use relative path**. When we test your work on a different operating system, all of the test will fail and you will get a 0. Don't panic when you see this, please fix the error and resubmit your assignment. Contact your TA if you need assistance with this task.
- **Avoid using loops to iterate over pandas dataframe and instead use boolean expressions**. More details are in the hints.

## Overview

For this project, you're going to analyze the whole
world!

Specifically, you're going to study various statistics for 174
countries, answering questions such as: *What is the correlation
between a country's literacy rate and GDP?*

To start, download [`test.py`](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p12/test.py) and [`expected.html`](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p12/expected.html).  You'll also need to
download [`lint.py`](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p12/lint.py) (see linter documentation under "Testing" below).
Do not download any data files manually (you must write Python code to
download these automatically).  You'll do all your work in a
`main.ipynb`.

**Warning**: Make sure you use `download` function from lab-p12 to pull the data instead of manually download. Otherwise you may get a zero. More details are in the Setup section.

# Data

For this project, you'll be using one large JSON file with statistics
about 174 countries adapted from
[here](https://www.kaggle.com/fernandol/countries-of-the-world).
and you will also extract data from a snapshot of
[this page](http://techslides.com/list-of-countries-and-capitals).

First check these resources:
* https://raw.githubusercontent.com/msyamkumar/cs220-s21-projects/master/p12/countries.json
* http://techslides.com/list-of-countries-and-capitals

Some of the columns require a little extra explanation:
* Area: measured in square miles
* Coastline: Ratio of coast to area
* Birth-rate: Births per 1000 people per year
* Death-rate: Deaths per 1000 people per year
* Infant-mortality: Deaths per 1000 births per year
* Literacy: (out of 100%)
* Phones: Number of phones per 1000 people

**DISCLAIMER**: This dataset has been taken from the source without any modifications. Any current information in the world affairs, including political implications haven't been represented in this dataset accurately. Please consider this as a synthetic dataset and not a real-world representation of the country information.

# Testing

For answers involving a DataFrame, `test.py` compares your tables to
those in `expected.html`, so take a moment to open that file from Explorer or Finder.

`test.py` doesn't care if you have extra rows or columns, and it
doesn't care about the order of the rows or columns.  However, you
must have the correct values at each index/column location shown in
`expected.html`.

For P12, `test.py` is pickier than it has been. In addition to
checking for incorrect answers, it will also check for a few common
kinds of bad coding style. You should look for linting messages at the bottom
of the output, for example:

```
Linting Summary:
  Warning Messages:
    cell: 1, line: 4 - Redefining built-in 'id'
    cell: 1, line: 3 - Reimport 'numpy' (imported line 2)
    cell: 1, line: 5 - Unnecessary pass statement
    cell: 1, line: 2 - Unused import numpy
```

In this case, `test.py` will deduct 1 point per linter message because of
bad style, and at most deduct 10 points. For more information about the linter
as well as how to run the full linter to see all of the automatically generated
advice and feedback, please check out the [linting README](https://github.com/tylerharter/cs301-projects/tree/master/linter).

# Setup

Use the `download` function from [lab-p12](https://github.com/msyamkumar/cs220-s21-projects/blob/master/lab-p12) to pull the data from here (do not manually download): https://raw.githubusercontent.com/msyamkumar/cs220-s21-projects/master/p12/countries.json
and store it in `countries.json`. Once you have created the file, create a Dataframe `countries` from this file.

**Warning**: 1. Make sure your `download` function does not download the file if it already exists. The TAs will manually deduct points otherwise. 2. Make sure you use `download` function to pull the data instead of manually download. Otherwise you may get a zero. 

*Hint*: `pd.read_json('countries.json')` will return a DataFrame by reading from
 the JSON file. If the file contains lists of dictionaries, each dictionary will be a row in the DataFrame.

## Questions

Before you proceed, make sure that `countries.head()` displays the following:

<img src="imgs/1-1.PNG" width="1000">

#### #Q1: How many countries do we have in our dataset?

#### #Q2: what is the total population across all the countries in our dataset?

*Hint*: Review how to extract a single column as a Series from a
 DataFrame. You can add all the values in a Series with the `.sum()`
 method.

----

Use the `download` function to download https://raw.githubusercontent.com/msyamkumar/cs220-s21-projects/master/p12/capitals.json
and store it in `capitals.json`. Create a DataFrame named `capitals` from this file. Before you proceed, make sure that `capitals.head()` displays the following:

<img src="imgs/1-2.PNG" width="300">

Use `capitals` and `countries` DataFrames to answer the following questions.


#### #Q3: What are the capital names in `capitals.json`?

Answer with an alphabetically-sorted Python list.


#### #Q4: What is the capital of Sweden?

Starting from this question, please avoid using loops to iterate over pandas dataframe and instead use boolean expressions.

*Hint*: Boolean expressions `capitals['country'] == "Sweden"` will return a boolean Series. And such a boolean series can also be used for indexing, where `capitals[capitals['country'] == "Sweden"]` may be a good start.

*Hint*: To extract the first entry of a Series, you may want to use `your_series_name.iloc[0]`.

#### #Q5: Which country's capital is Santiago?

#### #Q6: Which 7 countries have the southern-most capitals?

Produce a Python list of the 7, with southern-most first.

*Hint*: look at the documentation examples of how to sort a
 DataFrame with the [sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) function.

#### #Q7: Which 10 countries have the northern-most capitals?

Produce a Python list of the 10, with northern-most first.

#### #Q8: What is the largest land-locked country in South America?

A "land-locked" country is one that has zero coastline. Largest is in terms of **area**, where the areas are listed in `countries.json`.

#### #Q9: What is the largest coastal country in Africa?

A "coastal" country is one that has non-zero coastline. Largest is in terms of **area**.

#### #Q10: What is coastal country with the least population in Asia?


#### #Q11: What is the distance between Camp Randall Stadium and the Wisconsin State Capital?

This isn't related to countries, but it's a good warmup for the next
problems.  Your answer should be about 1.4339 miles.

Assumptions:
* The latitude/longitude of Randall Stadium is 43.070231, -89.411893
* The latitude/longitude of the Wisconsin Capital is 43.074645, -89.384113
* Use the Haversine formula: [http://www.movable-type.co.uk/scripts/gis-faq-5.1.html](http://www.movable-type.co.uk/scripts/gis-faq-5.1.html)
* The radius of the earth is 3956 miles
* You should answer in miles

If you find code online that computes the Haversine distance for you,
great! You are allowed to use it as long as (1) it works and (2) you
cite the source with a comment. Note that we won't help you
troubleshoot Haversine functions you didn't write yourself during
office hours, so if you want help, you should start from scratch on
this one.

If you decide to implement it yourself (it's fun!), here are some tips:
* Review the formula: [http://www.movable-type.co.uk/scripts/gis-faq-5.1.html](http://www.movable-type.co.uk/scripts/gis-faq-5.1.html)
* Remember that latitude and longitude are in degrees, but sin, cos, and other Python math functions usually expect radians.  Consider [math.radians](https://docs.python.org/3/library/math.html#math.radians)
* This means that before you do anything with the long and latitudes make sure to convert them to radians as your FIRST STEP

#### #Q12: What is the distance between Belgium and France?

For the coordinates of a country, use its capital.

DISCLAIMER: This dataset has been taken from the source without any modifications. Any current information in the world affairs, including political implications haven't been represented in this dataset accurately. Please consider this as a synthetic dataset and not a real-world representation of the country information.

#### #Q13: What are the distances between Belgium, France and Spain?

Your result should be DataFrame with 3 rows (for each country) and 3
columns (again for each country).  The value in each cell should be
the distance between the country of the row and the country of the
column. For a general idea of what this should look like, open the
`expected.html` file you downloaded.  When displaying the distance
between a country and itself, the table should display NaN (instead of
0).

*Hint*: you can use math.nan in your code to represent NAN in your answer.

#### #Q14: What is the distance between every pair of countries in the continent Australia?

Your result should be a table with 12 rows (for each country) and 12
columns (again for each country).  The value in each cell should be
the distance between the country of the row and the country of the
column.  For a general idea of what this should look like, open the
`expected.html` file you downloaded.  When displaying the distance
between a country and itself, the table should display NaN (instead of
0).

#### #Q15: What is the most central country in the continent Australia?

This is the country that has the shortest average distance to other countries in the continent Australia.

*Hint 1*: Check out the following Pandas functions:
* [DataFrame.mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)
* [Series.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html) (note this is not the same as the DataFrame.sort_values function you've used before)

*Hint 2*: A Pandas Series contains indexed values. If you have a
 Series `s` and you want just the values, you can use `s.values`; if
 you want just the index, you can use `s.index`. Both of these
 objects can readily be converted to lists.

#### #Q16: What is the least central country in the continent Australia?

This one has the largest average distance to other countries.

#### #Q17: How close is each country in the continent Australia to its nearest neighbor?

The answer should be in a table with countries as the index and two
columns: `nearest` will contain the name of the nearest country and
`distance` will contain the distance to that nearest country.

*Hint 1*: Find a Series of numerical data you can experiment with
 (perhaps from one of the DataFrames you've been using for this
 project).  If your Series is named `s`, try running `s.min()`.
 Unsurprisingly, this returns the smallest value in the Series.  Now
 try running `s.idxmin()`.  What does it seem to be doing?

*Hint 2*: If you run `df.min()` on a DataFrame, Pandas applies that
 function to every column Series in the DataFrame.  The returned value
 is a Series.  The index of the returned Series contains the columns
 of the DataFrame, and the values of the returned Series contain the
 minimum values.  If you run `df.idxmin()` on a DataFrame, the
 returned values contain indexes from the DataFrame.

*Hint 3*: If you get an error message about dtypes when running
 idxmin, make sure your DataFrame contains only floats (use
 `df.astype(float)` if necessary).

#### #Q18: How far is each country in the Australia continent to its furthest neighbor?

 The answer should be in a table with countries as the index and two
 columns: `furthest` will contain the name of the furthest country and
 `distance` will contain the distance to that furthest country.

 #### #Q19: For `birth-rate` and `death-rate`, what are various summary statistics (e.g., mean, max, standard deviation, etc.)?

*Format*: Use the
 [describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
 method on a DataFrame that contains `birth-rate` and `death-rate`
 columns. You may include summary statistics for other columns in
 your output, as long as your summary table has stats for birth-rate and
 death-rate.

#### #Q20: BeautifulSoup
Very often, you don't have data in nice json format like `capitals.json`. Instead data needs to be scraped from a webpage and requires some cleanup.
This is a long but fun exercise where we will do the same by scraping this webpage: http://techslides.com/list-of-countries-and-capitals.
Our `capitals.json` file was created from this same webpage.
You need to write the code to recreate `capitals.json` file from this table yourself.
Start by installing BeautifulSoup using pip, as discussed in class (learn how to install from **[lecture slides](https://www.msyamkumar.com/cs220/f20/materials/lec_32_F20.pdf))**.

Then call `download('capitals.html', 'https://raw.githubusercontent.com/msyamkumar/cs220-s21-projects/master/p12/techslides-snapshot.html')`
to download the webpage. Note that this code is not downloading the original webpage, but a snapshot of it (this is to avoid creating
excessive load on their servers).  You can open `capitals.html` and make sure that this page looks fine.

Now do the following:
* Read from `capitals.html` and use beautiful soup to convert the html text to soup.
* Find the table containing the data (Hint: .find() or .find_all() methods can be used).
* Find all the rows in the table (Note: rows are inside 'tr' html tag and data is in 'td' tag).
* Create a dictionary containing country name, capital and location coordinate (namely, the column names should be `country`, `capital`, `latitude` and `longitude`) and then create a list of dictionaries for all the countries.
* **Careful!** This web page has more countries than `countries.json`. We will ignore the countries that are not in that file. You need to filter and keep only the 174 countries whose names also appear in `countries.json`. The column names should be consistent with the original `capitals.json`.
* Save this list into file titled `my_capitals.json`. You can use json.dump() method.
* Remember to **close** `capitals.html` at the end.

Finally, copy/paste this code at the end to parse `my_capitals.json`:
```
f = open('my_capitals.json', encoding='utf-8')
my_capitals_data = json.load(f)
f.close()
my_capitals_data
```
This variable `my_capitals_data` should be your answer for this question.

### Before turning in:
Be sure to **delete** all the downloaded files (`countries.json`, `capitals.json`, `my_capitals.json` and `capitals.html`), run test.py again, and make sure there are no errors. If you do not delete the files before testing, your code will pass `test.py` even if your `download` function does not work. If you turn in a version of your code which fails on test.py (i.e. you can't see which questions you got right or not), **we will deduct 5 points**. If the autograder is failing but you still want to turn in, you can see which question it is failing on and comment out the code for that question, essentially leaving it out. 

After you add your name and the name of your partner to the notebook, please remember to **Kernel->Restart and Run All** to check for errors then run the test.py script one more time before submission.  To keep your code concise, please **remove your own testing code that does not influence the correctness of answers.** 
