# Project 3 (p3)

## Clarifications/Corrections

None yet.

**Find any issues?** Report to us: 

- LIANG SHANG <lshang6@wisc.edu>
- TIMOTHY OSSOWSKI <ossowski@wisc.edu>

## Learning Objectives

In this project, you will walk through how to

* Import a module and use its functions
* Practice writing functions
* practice doing some basic statistical analysis on the dataset

**Please go through [lab-p3](https://github.com/msyamkumar/cs220-s21-projects/blob/master/lab-p4) before working on this project.** The lab introduces some useful techniques related to this project.

## Description

In this project, you'll analyze spending data from
2017 to 2020 for five agencies in Madison: governments, gyms, restaurants,
schools, and stores.  You'll get practice calling functions from a
`project` module, which we'll provide, and practice writing your own
functions.

Start by downloading `project.py`, `test.py` and `madison.csv`.
Double check that these files don't get renamed by your browser (by
running `ls` in the terminal from your `p3` project directory).
You'll do all your work in a new `main.ipynb` notebook that you'll
create also in `p3` project directory and hand in when you're done (please do not write your
functions in a separate .py file).  You'll test as usual by running
`python test.py` (or similar, depending on your laptop setup).  Before
handing in, please put the project, submitter, and partner info in a
comment in the first cell, in the same format you used for previous
projects (please continue doing so for all projects this semester).

The first cell should contain and only contain information like this:
```python
# project: p3
# submitter: NETID1
# partner: NETID2
# hours: ????
```

We won't explain how to use the `project` module here (the code is in the
`project.py` file).  Refer to lab-p3 to understand the functions in project.py and use those. 
Feel free to take a look at the `project.py` code if you are curious about how it works.

This project consists of writing code to answer 20 questions.  If
you're answering a particular question in a cell in your notebook, you
need to put a comment in the cell so we know what you're answering.
For example, if you're answering question 13, the first line of your
cell should contain `#q13`.

## Dataset

The data looks like this:

agency_id|agency|2017|2018|2019|2020
------|------|------|------|------|------
3|schools|68.06346877|71.32575615000002|73.24794765999998|77.87553504
6|gyms|49.73757877|51.96834048|53.14405332|55.215007260000014
7|restaurants|16.96543425|18.12552139|19.13634773|19.845065799999997
122|stores|180.371421039999998|19.159243279999995|19.316837019999994|19.7607100000000
15|governments|25.368879940000006|28.2286218|26.655754419999994|27.798933740000003

The dataset is in the `madison.csv` file.  We'll learn about CSV files
later in the semester.  For now, you should know this about them:
* it's easy to create them by exporting from Excel
* it's easy to use them in Python programs
* we'll give you a `project.py` module to help you extract data from CSV files until we teach you to do it directly yourself

All the numbers in the dataset are in millions of dollars.  Answer
questions in millions of dollars unless we specify otherwise.

## Requirements

You may not hardcode agency IDs in your code.  For example, if we ask
how much was spent on stores in 2020, you could obtain the answer
with this code: `get_spending(get_id("schools"), 2020)`.  If you don't
use `get_id` and instead use `get_spending(3, 2020)`, we'll deduct
points.

For some of the questions, we'll ask you to write (then use) a
function to compute the answer.  If you compute the answer without
creating the function we ask you to, we'll manually deduct points from
the `test.py` score when recording your final grade, even if the way
you did it produced the correct answer.

## Questions and Functions

### #Q1: What is the agency ID of the gyms agency?


### #Q2: How much did the agency with ID 122 spend in 2018?

It is OK to hardcode `122` for Q2 in this case since we asked directly about
agency 122 (instead of about "stores"). Please do not hardcode the IDs for Q3 onwards.

### #Q3: How much did "stores" spend in 2020?

Hint: instead of repeatedly calling `project.get_id("streets")` (or
similar) for each question, you may wish to make these calls once at
the beginning of your notebook and save the results in variables,
something like this:

```python
schools_id = project.get_id("schools")
gyms_id = project.get_id("gyms")
restaurants_id = project.get_id("restaurants")
...
```

### Function 1: `year_min(year)`

This function will compute the minimum spending of any one agency in a
given year.  We'll give this one to you directly (you'll have to write
the code for the subsequent functions yourself).  Copy/paste this into
a cell in your notebook:

```python
def year_min(year):
    # grab the spending by each agency in the given year
    governments_spending = project.get_spending(project.get_id("governments"), year)
    gyms_spending = project.get_spending(project.get_id("gyms"), year)
    restaurants_spending = project.get_spending(project.get_id("restaurants"), year)
    schools_spending = project.get_spending(project.get_id("schools"), year)
    stores_spending = project.get_spending(project.get_id("stores"), year)

    # use builtin min function to get the largest of the five values
    return min(governments_spending, gyms_spending, restaurants_spending, schools_spending, stores_spending)
```

### #Q4: What was the least spent by a single agency in 2018?

Use `year_min` to answer this.

### #Q5: What was the least spent by a single agency in 2020?

### Function 2: `agency_max(agency)`

We'll help you start this one, but you need to fill in the rest
yourself.

```python
def agency_max(agency):
    agency_id = project.get_id(agency)
    y17 = project.get_spending(agency_id, 2017)
    y18 = project.get_spending(agency_id, 2018)
    # grab the other years

    # use the max function (similar to the min function)
    # to get the maximum across the four years
    # and return that value
```

This function will compute the maximum the given agency ever spent
over the course of a year.

### #Q6: What was the most that schools ever spent in a year?

Use your `agency_max` function.

### #Q7: What was the most that governments ever spent in a year?


### Function 3: `agency_avg(agency)`

This function will compute the average (over the four datapoints) that
the given agency spends per year.

Hint: start by copy/pasting `agency_max` and renaming your copy to
`agency_avg`.  Instead of computing the minimum of `y17`, `y18`, etc.,
compute the average of these by adding, then dividing by 4.

**Note: for consistency issues, we ask you round the average spending to 2 decimal places by using `round()` function. An example
is shown below:**
```python
pi = 3.1415926
approximation = round(pi, 2) # approximation is 3.14
```

### #Q8: How much is spent per year on stores on average?

Use your `agency_avg` function.

### #Q9: How much is spent per year on gyms, on average?

### #Q10: How much did the restaurants spend above their average in 2019?

You should answer by giving a percent between 0 and 100, with no
percent sign.  

And please round your answer to 2 decimal places.

In this case, your code should produce a number like `3.33 `.

### Function 4: `year_avg(year)`

This function will compute the average spending (over the five agencies) in a given year.

You can start from the following code:

```python
def year_avg(year=2018):
     pass # TODO: replace this line with your code
```

And please round the output of function to 2 decimal places.

Python requires all functions to have at least one line of code.  When
you don't have some code, yet, it's common for that line to be `pass`,
which does nothing.  Note the default arguments above.


### #Q11: How much is the average spending in 2018?

Use the default arguments (your call to `year_avg` should not pass any argument). **If you do not use default arguments,
you will lose points.**

### #Q12: How much is the average spending in 2020?


### Function 5: `change_per_year(agency, start_year, end_year)`

This function returns the average increase in spending (could be
negative if there's a decrease) over the period from `start_year` to
`end_year` for the specified `agency`.

You can start from the following code:

```python
def change_per_year(agency, start_year=2017, end_year=2020):
     pass # TODO: replace this line with your code
```

We're not asking you to assume exponential growth or do anything fancy
here; you just need to compute the difference between spending in the
last year and the first year, then divide by the number of elapsed
years. 

Also, please round the output of function to 2 decimal places.

### #Q13: how much has spending increased per year (on average) for governments from 2017 to 2020?

Use the default arguments (your call to `change_per_year` should only
pass one argument explicitly). **If you do not use the default arguments and only pass one argument explicitly, you will lose points.**

### #Q14: how much has spending increased per year (on average) for gyms from 2017 to 2019?
**As with Q13, if you do not use the default arguments and only pass one argument explicitly, you will lose points.**

### Function 6: `extrapolate(agency, year1, year2, year3)`

This function should compute the average change per year from the data
from `year1` to `year2` for `agency`, using your previous function for
finding average change.  It then returns the predicted spending in
`year3` from `year2` (i.e. extrapolate `year3` from `year2`), assuming spending continues increasing (or decreasing) by the
same constant amount each year.  We don't have anything for you to
copy for this one (you need to write it from scratch).

As an example, suppose spending in 2018 (year1) is 100 and spending in
2020 (year2) is 120.  The average increase is 10 per year.  So we
would extrapolate to 130 for 2021, 140 for 2022, etc.  This kind of
prediction is a simple *linear extrapolation*.

Please round the output of function to 2 decimal places.

### #Q15: how much will schools spend in 2021?

Extrapolate to 2021 from the data between 2018 and 2019.

### #Q16: how much will stores spend in 2099?

Extrapolate from the data between 2018 and 2020.

### #Q17: how much will restaurants spend in 2400?

Extrapolate from the data between 2017 and 2020.

### Function 7: `extrapolate_error`

We can't know how well our simple extrapolations will perform in the
future (unless we wait 80 years), but we can do shorter extrapolations
to years for which we DO know the result.  For example, we can
extrapolate to 2020 from the 2017-to-2019 data, then compare our
extrapolation to the actual spending in 2020.

Write a function named `extrapolate_error` that does an extrapolation
using the `extrapolate` function and compares the extrapolation to the
actual result, returning the error (i.e., how much `extrapolate`
overestimated).  For example, if the extrapolation is 105 and the
actual is 110, then the function should return -5.

What parameters should `extrapolate_error` have?  That's your
decision!

Please round the return value to 2 decimal places.

### #Q18: what is the error if we extrapolate to 2020 from the 2017-to-2018 data for governments?

### #Q19: what is the percent error if we extrapolate to 2020 from the 2017-to-2019 data for schools?

Percent error = extrapolate_error*100/actual_spending_of_the_agency_for_the_extrapolated_year

Please round your answer to 2 decimal places.

### #Q20: what is the standard deviation for restaurants spending over the 4 years?

Compute the population standard devation, as in [this example](https://en.wikipedia.org/wiki/Standard_deviation#Population_standard_deviation_of_grades_of_eight_students).

Remember to round your answer to 2 decimal places.

#### READ ME: Please remember to `Kernel->Restart and Run All` to check for errors, save your notebook, then run the test.py script one more time before submitting the project. To keep your code concise, please remove your own testing code that does not influence the correctness of answers. 

Cheers!
