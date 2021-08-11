# Project 5: Hurricane Study

# WARNING: Unless you took a time portal to become my student in the past, this is not the correct repository :) Please go to the correct github repository for the current semester. If you are a Spring'21 semester student though, you are in the right place.

## Corrections/Clarifications
Feb 25: we updated test.py to avoid some installation issues for Windows user; corrected the expected output of q20.
Feb 26: clarification of q13: both 1901 and 2000 are inclusive.

**Find any issues?** Report to us: 

- Sayali Alatkar <alatkar@wisc.edu>
- Ashish Hooda <ahooda@wisc.edu>

## Learning Objectives

In this project, you will 

* Write fundamental loop structures
* Learn basic string manipulations 
* Creating your own helper functions as outlined in [Lab P5](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p5)

**Please go through [Lab P5](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p5) before working on this project.** The lab introduces some useful techniques related to this project.

## Overview
This project will focus on **loops** and **strings**.

Hurricanes often count among the worst natural disasters, both in terms of
monetary costs and, more importantly, human life.  Data Science can
help us better understand these storms.  For example, take a quick
look at this FiveThirtyEight analysis by Maggie Koerth-Baker:
[Why We're Stuck With An Inadequate Hurricane Rating System](https://fivethirtyeight.com/features/why-were-stuck-with-an-inadequate-hurricane-rating-system/)
(you should all read FiveThirtyEight, btw!).

For this project, you'll be analyzing data in the `hurricanes.csv`
file.  We generated this data file by writing a Python program to
extract stats from this page:
https://en.wikipedia.org/wiki/List_of_United_States_hurricanes.  By
the end of this semester, we'll teach you to extract data from
websites like Wikipedia for yourself.

Before you start to work on p5, please complete [lab-p5](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p5) first.

 To start,
download `project.py`, `test.py` and `hurricanes.csv`.  You'll do your
work in Jupyter Notebooks this week, producing a `main.ipynb` file.
You'll test as usual by running `python test.py` to test a
`main.ipynb` file (or `python test.py other.ipynb` to test a notebook
with a different name). If needed, you may only use standard Python modules such as `math`. Please don't use `pip` to install any additional modules as these are not considered standard modules.

We won't explain how to use the `project` module here (the code in the
`project.py` file).  The lab this week is designed to teach you how it
works.

This project consists of writing code to answer 20 questions.  If
you're answering a particular question in a cell in your notebook, you
need to put a comment in the cell so we know what you're answering.
For example, if you're answering question 13, the first line of your
cell should contain `#q13`.

## Questions and Functions

For the first three questions, you don't have to define
any functions of your own. Instead you should just make use of the
functions provided in the file `project.py` by calling the corresponding
function that you need to solve a particular problem.

* Please note, for questions asking you to get a value at a particular **index**, you should not confuse it with the **actual** location of that value in the dataset. Indexing in python begins from 0.
<!-- For example, consider the table below:

<img src="table.png" width="150">

The **index** for the pokemon Charmander is 3 but its **actual** location is 4. Therefore, you must follow this convention for all the questions asking for the value at a particular index.-->

### #Q1: How many records are in the dataset?

### #Q2: What is the name of the hurricane at index 20?

### #Q3: How many deaths were caused by the hurricane at the last index?
Note - the code should work even if the number of hurricanes in the dataset later changes.

### #Q4: How many hurricanes named Florence are in the dataset?

Write your code such that it counts all the variants (e.g., "Florence",
"FLORENCE", "fLoReNce", etc.).

Hint: check String [`lower()`](https://www.w3schools.com/python/ref_string_lower.asp) method.

### #Q5: What is the name of the slowest hurricane?

If you find multiple hurricanes with the same speed, you should return the first one you find.

### #Q6: What is the fastest MPH ever achieved by a hurricane?

### #Q7: What is the average damage (in dollars) caused by all hurricanes?

You should answer this question with an integer. Therefore, you should convert your result to an integer. Be careful! In the data, the number was formatted with a suffix (one out of "K", "M" or "B"), but you'll need to do some processing to convert it.<!-- to this: `13500000` (an integer). -->

You need to write a general function that handles "K", "M", and "B" suffixes (it will be handy later).
Remember that "K" stands for thousand, "M" stands for million, and "B" stands for billion! For e.g. your function should convert a string from "13.5M" to 13500000, "6.9K" to 6900 and so on. 

Hint: use `float()` in the `format_damage` function for the numbers with decimal points before multiplying by `1000`, `1,000,000` and `1,000,000,000`. 

```python
def format_damage(damage):
  # TODO check the last character of the string
  # and then convert it to appropriate integer by slicing and type casting
  pass
```

<!-- ### Q9: How much faster was the fastest hurricane compared to the average speed of all the hurricanes in the dataset?

You need to calculate the average mph speed of all hurricanes and subtract it from fastest mph speed. -->

<!-- ### Q10: How much damage (in dollars) was done by the hurricane Sandy? -->

### #Q8: How many deaths did hurricane 'Gustav' cause?

### #Q9: What is the total deaths caused by hurricanes with names starting with the letter C?

This question is case insensitive.

### Function Suggestion:

We suggest you complete a function something like the following to
answer the next several questions (this is not a requirement if you
prefer to solve the problem another way):

```python
# return index of deadliest hurricane over the given date range
def deadliest_in_range(year1, year2):
    worst_idx = None
    for i in range(project.count()):
        if ????:  # TODO: check if year is in range
            if worst_idx == None or ????:  # TODO: it is worse than previous?
                # TODO: finish this code!
    return worst_idx
```

Hint: You can copy the `get_month`, `get_day`, and `get_year`
functions you created in lab to your project notebook if you like.

### #Q10: What was the deadliest hurricane of the 20th century (1901 to 2000, both inclusive)?

For this and the following, count a hurricane as being in the year it
was formed (not dissipated).

### #Q11: What is the deadliest hurricane ever recorded?

### #Q12: Between the years 1800 and 2016 (both inclusive), which year witnessed the deadliest hurricane?

### #Q13: How much damage (in dollars) was done by the deadliest hurricane between 1901 and 2000 (both inclusive)?

### #Q14: How many hurricanes were formed in the month of February?

### Function Suggestion:

We suggest you complete a function something like the following to
answer the next several questions (this is not a requirement if you
prefer to solve the problem another way):

```python
# return number of huricanes formed in month mm
def hurricanes_in_month(mm):
    num_of_hurricanes = 0
    for i in range(project.count()):
        pass # TODO: finish this code!
    return num_of_hurricanes
```


### #Q15: How many hurricanes formed between June and October (inclusive)?

We suggest using a for loop to get the hurricanes formed between two months mm1 and mm2. For example,

```python
for mm in range(mm1, mm2+1):
    # TODO: get the number of hurricanes for month mm 
    # TODO: finish this code!
```

### #Q16: Which month experienced the formation of most number of hurricanes? 

Please answer with an integer. e.g. January = `1`, February = `2`. If there is a tie, answer with the smaller number. For example, if both January and March tied the formation of the most number of hurricanes, your answer should be `1`.

### #Q17: What is the total damage across all hurricanes that formed in the month of January, in dollars?

### #Q18: How many hurricanes were formed in the decade 2001-2010 (inclusive)?

### #Q19: How many hurricanes were active on 31st December?
Hint: you can compare the year the hurricane formed and the year it dissipated. 

### #Q20: What year experienced the formation of most number of hurricanes?
Hint: similar as `q16`. 
If two years tied for the most number of hurricanes, your answer should be the earlier year.

### ####Please remember to Kernel->Restart and Run All to check for errors then run the test.py script one more time. Good luck with your hurricanes project! :) 
