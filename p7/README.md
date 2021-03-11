# Project 7: COVID-19 Vaccination 

## Corrections/ Clarifications

Mar 10: updated test.py for q10-q12 and covid19.csv. If you have already finished p7, the new test.py will still work. You don't need to do any modification to your code except cross-checking one more time before submitting.

Mar 11: updated test.py to make it work for both pythob 3.8 and 3.9; make the coding style requirement more clear.

**Find any issues?** Report to us, 

- ABHAY KUMAR <abhay.kumar@wisc.edu> 
- ASHWIN MARAN <amaran@wisc.edu>.

<h2>Learing objectives </h2>

 In this project, you will

* use dictionaries to answer questions about provided data;
* gain more experience with using lists in Python; using `sorted` method
* write programs to interpret data present in csv files;
* **develop good coding styling habits (points may be deducted for bad coding styles)**.


## Intro

Let's track COVID-19 vaccination, Python style!  In this project, you will get more practice with lists and start using dictionaries.  Start by downloading `test.py` and `covid19.csv` (which was adapted from [this dataset](https://ourworldindata.org/covid-vaccinations)). This dataset is too large to preview on GitHub (>18K rows), but you can view the [raw version](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p7/covid19.csv) or using a program such as [Excel](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p7/excel.md). You can also preview an example with 100 rows [here](https://github.com/msyamkumar/cs220-s21-projects/blob/master/p7/preview.csv). For this project, you'll create a new `main.ipynb` and answer questions in the usual format. **Please go through the [lab-p7](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p7) before working on this project.** The lab will help you to make helper functions and introduce some useful techniques related to this project.

<h2> Coding style requirements</h2>

* Don't name the variables and functions as python keywords or built-in functions. Bad example: str = "23".
* Don't define functions with the same name or define one function multiple times. Just keep the best version.
* Put all `import` commands together at the second cell of `main.ipynb`, the first cell should be submission information (netid and etc).
* Think twice before creating a function without any parameters. Defining a new functions is unnecessary sometimes. The advantage of writing functions is that we can reuse the same code. If we only use this function once, there is no need to create a new function. But feel free to create helper functions with one or more parameters that can be used for multiple questions.
* Avoid redundant logic.
* Please don't import any additional modules that we didn't ask you to import, **TAs will deduct points for that.**

## The Data

Try to familiarize yourself with the data before starting the analysis. We have vaccination and demographic details of countries. As you can see the data includes `country`, `continent`, `new_vaccinations` (on a particular date), `total_vaccinations` (the total number of vaccines administered till that date), `people_fully_vaccinated` (people who have got both vaccine doses), `vaccine_used`, and demographic details like `population`, `population_density`, `gdp_per_capita`, `human_development_index`. For instance, United States administered 1563780 new doses leading to 44769970 total vaccination doses till 2021-02-10 (YYYY-MM-DD format) and used the Moderna vaccine. 

To ingest the data to your notebook, paste the following in an early cell:

```python
import csv

covid_file = open('covid19.csv', encoding='utf-8')
file_reader = csv.reader(covid_file)
covid_data = list(file_reader)
covid_file.close()
header = covid_data[0]
covid_data = covid_data[1:]

# convert str to float/int types in columns having numerical values.
for row in covid_data:
    for idx in [3, 4, 5, 7, 8, 9, 10]:
        # Fill empty cell with 0 values.
        if row[idx] == '':
            row[idx] = 0
        if idx in [3, 4, 5, 7]:
            row[idx] = int(row[idx])
        elif idx in [8, 9, 10]:
            row[idx] = float(row[idx])
```
Note: We have added 0 value to fill the missing values in the dataset (`covid19.csv`) to make things easier.


Consider peeking at the first few rows:
```python
print(header)

for row in covid_data[:5]:
    print(row)
```

It's up to you to write any functions that will make it more convenient to access this data. 

## Let's Start! 
#### Please don't hardcode the column index

#### #Q1: Which country has the highest human_development_index?


#### #Q2: Which country has the highest gdp_per_capita?


#### #Q3: Which continent contains the country with the highest population_density?

Note: Did you solve Q1-Q3 by using the same function? If not, try to define a single function that can solve all of them. You are **not** obligated to use a function here, but it would be a good habit to get into. Try it!

Hint: Consider passing column_name as an argument 

---

Complete the following function in your notebook:

```python
def get_column(col_name):
    pass # replace this
```

The function extracts an entire column from `covid_data` to a list, which it returns.  For example, imagine `covid_data` contained this:

```python
[
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
```

And `header` contains this:

```python
["X", "Y", "Z"],
```

Then column "X" is `["a", "d", "g"]`, column "Y" is `["b", "e", "h"]`, and column "Z" is `["c", "f", "i"]`.  A call to `get_column("Y")` should therefore return `["b", "e", "h"]`, and so on.

----

**You should be able to solve Q4 to Q9 efficiently using `get_column` function.**

#### #Q4: How many UNIQUE countries are listed in the dataset?
Hint: Use `get_column`, then use set() to remove duplicates .

#### #Q5: What are the different dates for which we have data in the dataset? You should return a list (order of the values in the list doesn't matter).


#### #Q6: How many new vaccinations were done across the whole world on the dates included in the dataset (i.e. `2021-02-10` to `2021-02-16`)?
Hint: Think about if we really need to consder the `date` column as we are considering all possible dates in the dataset.

#### #Q7: What are the population counts of top 5 populous countries (Having the highest population)? 
The answer should be a list of population values in decreasing order. Please note that population count of a country remains same for all dates mentioned in the dataset. You can refer back to [lab 6](https://github.com/msyamkumar/cs220-s21-projects/tree/main/lab-p6) to make use of `sort` or `sorted`.

#### #Q8: What the are gdp_per_capita values for top 5 gdp_per_capita countries? 
The answer should be a list of `gdp_per_capita` values in decreasing order.


#### #Q9: What are the different vaccines used? You should output a list (order of the values in the list doesn't matter).
Note: Some countries may have no vaccine used, you will get an empty string `''` in the `vaccine_used` column for those countries. Remove empty string from the answer.

----

#### #Q10: How many total vaccination doses were administered by 2021-02-16 for each country? You should output a dictionary.
Hint: Use `total_vaccinations` column of the dataset.

Answer in the form of a dictionary mapping the countries to the total_vaccinations. The form of the dictionary should look like (there should be more elements in your output, and elements with 0 value is fine):

```python
{
  'Afghanistan': 0,
  'Bangladesh': 1359613,
  'Italy': 3122631,
  'Sweden': 505898,
  'United States': 55220364,
}
```

Use the dictionary from Q10 to answer the next two questions.

#### #Q11: Which country has administered the maximum number of total_vaccinations by 2021-02-16?


#### #Q12: Which countries hadn't started vaccination according to the dataset?
Hint: Return a sorted list of all countries with 0 `total_vaccinations` by `2021-02-16`.

----

Define a function `country_stats_to_dict` that takes two parameter: `country` and `date`, and returns a dict containing all the statistics about the country for the given date. 
Find the suitable row by matching country and date columns in the data.

---

#### #Q13: What were the stats for the United States as on 2021-02-16?

Use your `country_stats_to_dict` function.  For instance, the function call `country_stats_to_dict("Italy")` should output the following dictionary: 

```python
{'country': 'Italy',
 'continent': 'Europe',
 'date': '2021-02-16',
 'new_vaccinations': 60736.0,
 'total_vaccinations': 3122631.0,
 'people_fully_vaccinated': 1295514.0,
 'vaccine_used': ['Moderna'],
 'population': 60461828.0,
 'population_density': 205.859,
 'gdp_per_capita': 35220.084,
 'human_development_index': 0.892}
```

#### #Q14: What were the stats for India as on 2021-02-14? 


#### #Q15: Which vaccine was used in the United States on 2021-02-16?
Hint: You can use the results of Q13


#### #Q16: How many new vaccination doses (refer `new_vaccinations` column) were administered from 2021-02-10 to 2021-02-16? You should output a dictionary with (key, value) pair as (date, sum of new_vaccinations on that particular date) 



#### #Q17: What percentage of people have been fully vaccinated in each country as per the latest (`2021-02-16`) details? You should return a dict with (country, percentage_fully_vaccinated) pair. For example, if US has fully vaccinated 1% people and Canada has vaccinated 0.5% people, your output dictionary should look like this (No `%` sign in the output) 
```python
{'US': 1,
 'Canada': 0.5,
}
```
Note: You need to use `people_fully_vaccinated` column in the datset, this is different from `total_vaccinations` column. `people_fully_vaccinated` are those who have received both required vaccine doses.

Hint: percentage = (`people_fully_vaccinated` / `population`) * 100



#### #Q18: Which countries did use `Moderna` vaccine on `2021-02-16`? You should return a list (order of the values in the list doesn't matter).
Hint: Try defining a function with parameters: `vaccine_name`, `date`


#### #Q19: Which countries use a given vaccine? You should output a dictionary with (key, value) pair as (vaccine_name, list of countries using that vaccine) 
Hint1: You can use the result from q9 and the functions defined for q18.  The output list (from Q9) containing all vaccine names can be used.
Hint2: Also use the fact that vaccines used by a country is same for all dates. You can fix date, say `2021-02-16`. The answer will remain same for any date.



#### #Q20: You want to rely on collective judgement and you would prefer to take vaccine that has been used by maximum number of countries. Which vaccine is used by most countries?
Hint: You can count the number of countries in q19 output dictionary



### Please remember to Kernel->Restart and Run All to check for errors then run the test.py script one more time.



## Cheers! To getting vaccinated! 

