# Project 9: Analyzing the Movies

# WARNING: Unless you took a time portal to become my student in the past, this is not the correct repository :) Please go to the correct github repository for the current semester. If you are a Spring'21 semester student though, you are in the right place.

## Clarifications/Corrections

None yet.

**Find any issues?** Report to us:  

- Wenxuan Zhao [wzhao78@wisc.edu](mailto:wzhao78@wisc.edu)
- Tim Ossowski [ossowski@wisc.edu](mailto:ossowski@wisc.edu)

## Learning Objectives

In this project, you will
- Use matplotlib to plot bar graphs and visualize statistics
- Reinforce your knowledge even further about dictionaries and lists
- Apply the idea of binning by creating dictionaries to group similar movies 
- Begin using custom sorting for lists

## Coding Style Requirements

Remember that coding style matters! **We might deduct points for bad coding style.** Please refer to [requirements in p8](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8). 

## Introduction

In p8, you created very useful helper functions to help parse the raw movie IMDb dataset. In this project, we will be using the work you
did in p8 to load the movie data and analyze the data even further. Please make sure that your **get_movies(movie_path, mapping_path)** is correct before doing this project. **For the questions asking you to plot, our test.py is unable to check whether your plot is correct. As long as you have any output for these questions, you will pass the tests. So make sure compare your plots with the expected pngs ([Q4.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q4.png), [Q5.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/Q5.png), [Q6.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q6.png), [Q7.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q7.png), [Q8.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q8.png), [Q12.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q12.png)) before submitting your notebook.**

As usual, hand in the `main.ipynb` file (use the `#qN` format).  Start by downloading the following files: [`test.py`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/test.py), [`mapping.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/mapping.csv), and [`movies.csv`](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8/movies.csv). We are using the same `mapping.csv` and the same `movies.csv` as we did in [p8](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p8). 

In `main.ipynb`, make sure to include a new cell with the following code:

```python
import csv
import copy 
import matplotlib
import pandas

# Allows you to render matplotlib graphs in the same notebook
%matplotlib inline 

def plot_dict(d, label="Please Label Me!!!"):
    ax = pandas.Series(d).sort_index().plot.bar(color="black", fontsize=16)
    ax.set_ylabel(label, fontsize=16)
```

[**Lab-p9**](https://github.com/msyamkumar/cs220-s21-projects/tree/main/lab-p9) goes over the installation and the basic usage of **matplotlib** and **pandas**. Please make sure to go over the lab before dive into the project. 

Finally, copy all the functions you wrote from p8 to `main.ipynb`. As a reminder, the functions you should include are `get_mapping`, `get_raw_movies`, `get_movies`, along with any helper functions you used to write these.

If you are ready, let's get started!

<h2> Analyzing the Movie Data </h2>

For all these questions, we will be looking at the movies in `mapping.csv` and `movies.csv`. You can load the list of movies using the function
you wrote in the last project (Note you should only have to do this once):

```python
movies = get_movies("movies.csv", "mapping.csv")
```

This will result on a list of movies, which we can loop over and answer interesting questions about. Each entry in the list should be
a dictionary that looks something like this:

```python
{'title': 'Moneyball',
 'year': 2011,
 'genres': ['Biography', 'Drama', 'Sport'],
 'duration': 133,
 'directors': ['Bennett Miller'],
 'actors': ['Brad Pitt',
  'Jonah Hill',
  'Philip Seymour Hoffman',
  'Robin Wright'],
 'rating': 7.6}
```

---

The first few questions can be answered using similar methods to earlier projects. They should help familiarize yourself with the data
and understand how to traverse it with loops:

### #q1 Find the average rating for movies with less than 5 actors/actresses?

Hint/Suggestion: Go through the movies and find ones where the length of the actor list < 5.


### #q2 Find the average rating for movies with at least 5 actors/actresses?


### #q3 What is the average rating of movies which start with the letter 'a' (case insensitive)?

---

For questions 4-8, your answers should be plots. Use the `plot_dict()` function to answer these questions Make sure to label the vertical axis with an informative name for all your graphs! **For all plotting questions, if either the horizontal axis or vertical axis for your graphs aren't labelled, you will lose points.**

### #q4 Plot the title vs rating of movies featuring "Emma Stone".

Comments: The horizontal axis (the x-axis) should be the names of movies Emma Stone was in. The vertical axis should be the corresponding rating of these movies. Make sure you name the vertical axis (i.e. `rating`). 

The expected dictionary to be plotted is:

```python
{'The House Bunny': 5.5,
 'Easy A': 7.0,
 'La La Land': 8.0,
 'Aloha': 5.4,
 'The Amazing Spider-Man 2': 6.6,
 'The Favourite': 7.5,
 'The Help': 8.0,
 'The Croods': 7.2,
 'Irrational Man': 6.6,
 'Battle of the Sexes': 6.7,
 'Marmaduke': 4.3,
 'The Amazing Spider-Man': 6.9,
 'Birdman or (The Unexpected Virtue of Ignorance)': 7.7}
```

The expected dictionary here is for verification use. Don't directly copy this to your notebook!


### #q5 Plot the title vs rating of movies directed by "Quentin Tarantino".

The expected dictionary to be plotted is:

```python
{'Death Proof': 7.0,
 'Kill Bill: Vol. 1': 8.1,
 'Kill Bill: Vol. 2': 8.0,
 'Reservoir Dogs': 8.3,
 'Sin City': 8.0,
 'Once Upon a Time... in Hollywood': 7.6,
 'Inglourious Basterds': 8.3,
 'The Hateful Eight': 7.8,
 'Jackie Brown': 7.5,
 'Pulp Fiction': 8.9,
 'Django Unchained': 8.4,
 "My Best Friend's Birthday": 5.6}
```

### #q6 Plot the number of movies played by ["John Wayne", "Edward Norton", "Danny Glover"].

Comments: The graph should have 3 bars, one for each of these actors. On the horizontal axis, each bar should be labelled with an actor name. The height of each bar should be the number of movies the actor played in.

The expected dictionary to be plotted is:

```python
{'John Wayne': 128, 'Edward Norton': 19, 'Danny Glover': 37}
```

### #q7 Plot the number of movies that start with each letter of the alphabet.

Comments: The graph should have 26 bars, one for each letter of the alphabet. The x-axis should be in alphabetical order. The height of each bar should be the number of movies which start with that letter. Remember to use `.lower()` when checking if a movie title starts with a letter.

The expected dictionary to be plotted is:

```python
{'a': 2135,
 'b': 2147,
 'c': 1732,
 'd': 1655,
 'e': 638,
 'f': 1216,
 'g': 878,
 'h': 1349,
 'i': 879,
 'j': 506,
 'k': 452,
 'l': 1215,
 'm': 1733,
 'n': 719,
 'o': 551,
 'p': 1126,
 'q': 59,
 'r': 1086,
 's': 2850,
 't': 7912,
 'u': 279,
 'v': 258,
 'w': 1011,
 'x': 22,
 'y': 175,
 'z': 106}
```

### #q8: Plot the number of movies there are for each genre.

Comments: The graph should have 1 bar for each unique genre. The height of each bar should be the number of movies that contain that genre in its list of genres.

Hint: A movie might have multiple genres. Make sure you count all of the genres in the list for each movie:

```python
genre_buckets = {}

for movie in movies:
    for genre in movie['genres']:
        ...

```

The expected dictionary to be plotted is:

```python
{'Action': 5611,
 'Adventure': 3849,
 'Drama': 16410,
 'Biography': 1009,
 'Sport': 565,
 'Horror': 5175,
 'Mystery': 2479,
 'Thriller': 5340,
 'Comedy': 11130,
 'Family': 1585,
 'Romance': 5753,
 'Crime': 5078,
 'Western': 1177,
 'Fantasy': 1537,
 'Animation': 676,
 'Sci-Fi': 2148,
 'Film-Noir': 647,
 'History': 627,
 'War': 779,
 'Musical': 941,
 'Music': 908,
 'News': 1,
 'Documentary': 1,
 'Reality-TV': 1}
```

### #q9 For each letter of the alphabet, what is the average rating of movies that start with that letter (case insensitive)?

Comments: Your answer should be a dictionary mapping each letter of the alphabet to the average rating of movies that start with that letter.

Hint: Since this question asks for an average, consider having a dictionary mapping a letter in the alphabet to a **list** of ratings of movies which start with that letter. Recall the average of entries in a list `numbers` can be computed with `sum(numbers)/len(numbers)`

### #q10 What is the average movie rating for each genre?

Comments: Your answer should be a dictionary mapping each genre to a number.


### #q11 How many movies in each genre have a rating of above 8? (rating > 8)

Comments: Your answer should be a dictionary mapping each genre to a number.


Hint: Use a similar strategy to q8, but only include movies with rating above 8.

### #q12 Plot the number of movies that were released each year in the last decade (2010<= year <=2020)

Comments: Your answer should be a dictionary mapping each year to a number. See [Q12.png](https://github.com/msyamkumar/cs220-s21-projects/tree/main/p9/Q12.png) for reference.

The expected dictionary to be plotted is:

```python
{2012: 862,
 2011: 785,
 2016: 1056,
 2010: 706,
 2015: 981,
 2014: 976,
 2018: 1043,
 2013: 980,
 2017: 1052,
 2019: 849,
 2020: 300}
```


### #q13 Which year (or years) had the highest number of movie releases?

Comments: Your answer should be a list. If there is a tie, the list should contain multiple years in it (the order of the list doesn't matter). Otherwise, the list should only have 1 year in it.

---

For the rest of the questions, **custom sorting** will be important.

### #q14 Which 3 genres have the least number of movies? (the lowest first)

The list should be in increasing order, with the genre with the least number of movies being the first. 

Hint: Create a dictionary which maps genre name to the number of movies in that genre. Also create a list of all unique genres. Define a custom sorting function:

```python
"""
This function returns the number of movies in this genre
"""
def genre_sort(genre_name):
  	return ????
```

Finally, sort the list of all unique genres according to this custom function:

```python
sorted(????, key = genre_sort)
```

### #q15 Which 3 genres have the most number of movies? 

The list should be in decreasing order, with the genre with the most number of movies being the first. 

Hint: Use your answer from q14.

### #q16 Which actor/actress has been featured in the most number of  movies?

Comments: The output should be a single string.

### #q17 Which 10 actors/actresses are featured in the most number of movies? (The actor/actress featured in the most movies should be outputted first)

The list should be in decreasing order, with the name of the actor/actress featured in the most movies being the first. 

### #q18 How many actors/actresses have only acted in only 1 movie?

### #q19 What are the titles of the top 5 rated movies in the dataset?

The list should be in decreasing order, with the title of the highest-rated movie being the first. 

### #q20 What are the titles of the bottom 13 rated movies in the dataset?

The list should be in increasing order, with the title of the lowest-rated movie being the first. 

### Before turning in:
Be sure to run test.py and make sure there are no errors. If you turn in a version of your code which fails on test.py (i.e. you can't see which questions you got right or not), **we will deduct 5 points**. If the autograder is failing but you still want to turn in, you can see which question it is failing on and comment out the code for that question, essentially leaving it out. 

After you add your name and the name of your partner to the notebook, please remember to **Kernel->Restart and Run All** to check for errors then run the test.py script one more time before submission.  To keep your code concise, please **remove your own testing code that does not influence the correctness of answers.** 


