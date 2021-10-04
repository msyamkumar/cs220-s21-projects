# Project 8: Going to the Movies

# WARNING: Unless you took a time portal to become my student in the past, this is not the correct repository :) Please go to the correct github repository for the current semester. If you are a Spring'21 semester student though, you are in the right place.

## Clarifications/Corrections

* Mar 17: updated the test.py

**Find any issues?** Report to us:  
- Ashwin Maran [amaran@wisc.edu](mailto:amaran@wisc.edu)
- Ashish Hooda [ahooda@wisc.edu](mailto:ahooda@wisc.edu)

## Learning Objectives

In this project, you will:
- integrate relevant information from various sources (e.g. multiple csv files)  
- reinforce your knowledge about dictionaries and lists
- use appropriate data structures for organized and informative presentation (e.g. list of dictionaries)
- continue practicing good coding style

## Coding Style Requirements

Remember that coding style matters! **We may deduct points for bad coding style.** In addition to the [requirements from p7](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p7), here are several other common bad coding habits to avoid:

- Do not use meaningless names for variables or functions (e.g. uuu = "my name").
- Do not write the exact same code in multiple places. Instead, wrap this code into a function and call that function whenever the code should be used.
- Do not call unnecessary functions (i.e. functions with no parameters).
- Avoid using slow functions multiple times within a loop.
- Avoid calling functions that iterate over the entire dataset within another loop; instead, call the function before the loop and store the result in a variable.

## Introduction

In this project and the next, we will be working on the [IMDb Movies Dataset](https://www.imdb.com/interfaces/). A very exciting fortnight lies ahead where we find out some cool facts about our favorite movies, actors, and directors.

In this project, you will combine the data from the movie and mapping files into a more useful format. As usual, hand in the `main.ipynb` file (use the `#qN` format).  Start by downloading the following files: [`test.py`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/test.py), [`small_mapping.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/small_mapping.csv), [`small_movies.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/small_movies.csv), [`mapping.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/mapping.csv), and [`movies.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/movies.csv).

## The Data

Open `movies.csv` and `mapping.csv` in any Spreadsheet viewer, and see what the data looks like. `movies.csv` has ~33000 rows and `mapping.csv` has ~84000 rows. Before we start working with these very large datasets, let us start with some much smaller datasets. `small_movies.csv` and `small_mapping.csv` have been provided to help you get your core logic right with a smaller dataset. `small_movies.csv` has the same columns (but fewer rows) than `movies.csv`, and the same applies to `small_mapping.csv` and `mapping.csv`. In the next project (p9), you will be mostly working mainly with `movies.csv` and `mapping.csv`.

`small_movies.csv` and `movies.csv` have 7 columns: `title`, `year`, `genres`, `duration`, `directors`, `actors`, and `rating`.

Here are a few rows from `movies.csv`:
```
title,year,genres,duration,directors,actors,rating
tt1735898,2012,"Action, Adventure, Drama",127,nm2782185,"nm0829576, nm1165110, nm0000234, nm3510471",6.1
tt1210166,2011,"Biography, Drama, Sport",133,nm0587955,"nm0000093, nm1706767, nm0000450, nm0000705",7.6
tt0058079,1964,Horror,60,"nm0554924, nm0692414","nm0001033, nm0067280, nm0593360, nm0388885",3.0
```

The `year` column refers to the year the movie was released in, `duration` refers to the duration of the movie (in minutes), `genres` refers to the genres that the movie belongs to, and `rating` refers to the IMDb rating of that movie. The weird alphanumeric sequences used for the columns `title`, `actors`, and `directors` are the unique identifiers that IMDb uses for identifying either an actor or a director or a movie title. The IDs that begin with `tt` refer to a movie title, and the IDs that begin with `nm` refer to a person (either an actor or a director).

`small_mapping.csv` and `mapping.csv` have 2 columns: `id` and `name`, mapping these IDs to their names.

Here are a few rows from `mapping.csv`:

```
tt0110991,Ring of Steel
tt0037244,San Diego I Love You
tt10003008,The Rental
nm0364744,Hank Harris
nm0563220,Zola Maseko
```

If you are ready, let's get started with data plumbing!


# Data Plumbing

A lot of data science work often involves *plumbing*, the process of
getting messy data into a more useful format.  Data plumbing is the
focus of this project.  We'll develop and test three functions that will be
helpful in p9:

1. `get_mapping(path)`: this loads a mapping file that can be used to lookup names from IDs
2. `get_raw_movies(path)`: this loads movie data with info represented using IDs
3. `get_movies(movies_path, mapping_path)`: this uses the other two functions to load movie data, then replace the IDs with names

Note - the variable `path` is of type string

---

Start by writing a function that starts like this:

```python
def get_mapping(path):
```

When called, the `path` should refer to one of the mapping files
(e.g., "small_mapping.csv").  The function should return a dictionary
that maps IDs (as keys) to names (as values), based on the file
referenced by `path`.  For example, this code:

```python
mapping = get_mapping("small_mapping.csv")
mapping
```

should output this (order doesn't matter):

```python
{'tt1233301': 'Ironclad',
 'tt0090605': 'Aliens',
 'nm0257646': 'Jonathan English',
 'nm0000299': 'Michael Biehn',
 'nm0000116': 'James Cameron',
 'nm9696871': 'Brian Cox',
 'nm0001343': 'Carrie Henn',
 'nm0700856': 'James Purefoy',
 'nm0544718': 'Kate Mara',
 'nm0000244': 'Sigourney Weaver'}
```

Note that the mapping files DO NOT have a CSV header.

The following questions pertain to `small_mapping.csv` unless
otherwise specified.

---

#### \#Q1: What is returned by your `get_mapping("small_mapping.csv")` function?

You shouldn't be surprised to see the results are exactly the dictionary shown above if your function works correctly. Please (1) store the result in a variable for use in subsequent questions, and (2) display the result in the Out [N] area so the grading script can find your answer. By storing the result in a variable, you can avoid having to call this time-consuming function in the future.

Hint: The `process_csv` function from the previous projects might come in handy.

#### \#Q2: What is the value associated with the key "nm0000244"?

Hint: Use the dictionary returned earlier.

#### \#Q3: What are the values in the mapping (dictionary) associated with keys that begin with "nm"?

The answer should be a Python list. The order does not matter.

#### \#Q4: For people with "James" as their first name in the above mapping, which keys do they correspond to?

The answer should be a Python list. The order does not matter.

**Warning**: Make sure that you only consider the people whose first name is "James". To get full credit for this problem, given a larger dataset, your code should **not** return any of the following:
1. IDs of any movie titles,
2. IDs of people whose first name is not "James", but the last or middle name is "James"
3. IDs of people whose first name is not "James", but starts with the string "James" (such as "Jameson").

---

Now, let's move on to read movie files! Build a function named `get_raw_movies` that takes the path to a
CSV file (e.g., "small_movies.csv" or "movies.csv") as the only parameter and
returns a list of dictionaries where each dictionary represents a
movie as follows:

```python
{
    'title': "movie-id",
    'year': <the year as an integer>,
    'genres': ["genre1", "genre2", ...],
    'duration': <the duration as an integer>,
    'directors': ["director-id1", "director-id2", ...],
    'actors': ["actor-id1", "actor-id2", ....],
    'rating': <the rating as a float>
}
```

Note that unlike `small_mapping.csv`, the movie files DO have a CSV header.

To be consistent, the values for `directors`, `actors`, and `genres`
are always of type \<list\>, even if some lists might only contain a single item.

---

#### \#Q5: What does `get_raw_movies("small_movies.csv")` return?

The result should be this (the order of the movies *does* matter):
```python
[{'title': 'tt0090605',
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
  'rating': 6.1}]
```
If your answer looks correct, but does not pass `test.py`, make sure that the datatypes are all correct. Also make sure that the actors and directors are in the same order, as here.

As with `get_mapping`, keep the result returned by `get_raw_movies` in a variable for use in answering future questions. Do not call `get_raw_movies` every time you need data from the movies file.



#### \#Q6: How many actors does the movie at index 1 have?

Hint: Use the dictionary from Q5.

#### \#Q7: What is the ID of the first actor listed for the movie at index 0?

Hint: use the dictionary from Q5.

---
You may have noticed that `actors`, `directors`, and `title` are represented by IDs instead of actual names. Write a function named
`get_movies(movies_path, mapping_path)` that loads data from the
`movies_path` file using `get_raw_movies` and converts the IDs to
names using a mapping based on the `mapping_path` file, which you
should load using your `get_mapping` function.

Each dictionary in the list should look like this:

```python
{
    'title': "the movie name",
    'year': <the year as an integer>,
    'genres': ["genre1", "genre2", ...],
    'duration': <the duration as an integer>,
    'directors': ["director-name1", "director-name2", ...],
    'actors': ["actor-name1", "actor-name2", ....],
    'rating': <the rating as a float>
}
```

Notice the difference between the previous one and this (IDs are replaced by names). This list of dictionaries is essential for almost all of the following questions.

We recommend you break this down into several steps.  Start with the simple case the `title`: try to translate from the ID code to the name of the movie. Then work on translating for actors and directors after you get the title working. The `actors` and `directors` are more complicated because they are lists.

After you implement your function, call it and store the result as a variable named `small_data`:

```python
small_data = get_movies("small_movies.csv", "small_mapping.csv")
```

#### \#Q8: What is `small_data`?

The result should look something like this :

```python
[{'title': 'Aliens',
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
  'rating': 6.1}]
```

#### \#Q9: What is `small_data[1]["title"]`?

Just paste `small_data[1]["title"]` into a cell and run it.  We're doing
this to check that the structures in `small_data` (as returned by
`get_movies` above) contain the correct data.

#### \#Q10: What is `small_data[0]["actors"]`?

#### \#Q11: What is `small_data[-1]["directors"]`?

---

If you've gotten this far, your functions must be working pretty well
with small datasets.  So let's try the full dataset!

```python
movies = get_movies("movies.csv", "mapping.csv")
```

**Warning**: You are **not** allowed to call `get_movies` more than once for the
"movies.csv" file in your notebook.  Reuse the `movies` variable
instead, which is more efficient. Otherwise, we will deduct points for bad coding style.

---

#### \#Q12: What are the 500th to 505th (inclusive) rows in movies?

Please return a list of dictionaries whose **format** is like this:

```python
[{'title': 'Evolution',
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
  'rating': 4.0}]
```

------



#### \#Q13: What are the last 3 rows in movies?

Please return a list of dictionaries whose **format** is like this:

```python
[{'title': 'Front Cover',
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
  'rating': 4.4}]
```

------

Copy the following function to your notebook, but don't change it in any way.

```python
# you are *not* allowed to change this function
def filter_movies_by_year(movies, year):
    i = 0
    while i < len(movies):
        if movies[i]["year"] != year:
            movies.pop(i)
        else:
            i += 1
    return movies
```

The `movies` parameter is for a list of movie dictionaries (similar to what is returned by `get_movies`) and `year` is a year to filter on. The function returns the movies in `movies` that were in the given year.

------

####

#### \#Q14: What are the total number of movies from 2019?

Note that the `filter_movies_by_year` function has an **undesirable** side effect that we will fix in Q15 and you may need restart the kernel and run all. For this problem you are required to follow these requirements:
1. Answer using `filter_movies_by_year`
2. Do **not** call `get_movies` on "movies.csv" more than once in your notebook

#### \#Q15: What are the movies from 1972 with duration greater than 120 minutes?

**Hint:** we've set you up a bit to encounter a bug.  Review the copy functions in the `copy` module and see if you can use one of them to overcome the shortcomings of the `filter_movies_by_year` function we're forcing you to use. You can call one of the copy functions outside of the  `filter_movies_by_year` function to copy the dataset. You might need to go back and tweak your q14 answer and potentially do a "Restart & Run All" on your notebook after you've fixed the bug. Remember that you need to follow the requirements below:
1. Answer using `filter_movies_by_year`
2. Do **not** call `get_movies` on "movies.csv" more than once in your notebook
3. Do **not** change `filter_movies_by_year`

Return a list of movie dictionaries.

#### \#Q16: How many unique genres are there in the dataset?

Think about whether you can write a function that can also help you with Q17 and Q18 at the same time.

Make sure you have completed Q15 before attempting Q16-Q20. Otherwise, `test.py` will flag your answers as incorrect.

#### \#Q17: How many unique actor names are there in the dataset?

#### \#Q18: How many unique director names are there in the dataset?

#### \#Q19: What is the average duration for all movies?

#### \#Q20: List the movies directed by the director with the longest name in the dataset.

Longest name refers to the director whose name has the most number of characters (inclusive of spaces). There is a unique director in the dataset with the longest name. So, you don't have to worry about breaking ties.

####

As before, please remember to **Kernel->Restart and Run All** to check for errors then run the test.py script one more time before submission. (Make sure to remove any unnecessary or extra lines of code from your submission)
