# Project 6: Airbnb

## Corrections/ Clarifications

Mar 3: clarification of q5: please remove the duplicates in your list.

Mar 6: clarification of q18: please don't remove any duplicates in your list.

**Find any issues?** Report to us:
- Ashish Hooda <ahooda@wisc.edu>
- Tarun Anand <tanand3@wisc.edu>

## Announcements

* Remember you must begin each cell with the comment #Q1, #Q2, etc.  This comment is read by test.py to
identify which question is being answered. We recommend copying the entire question line as a comment
into your notebook.
* To view comments grader comments for previous projects go to the project submission page and select
the graded project and click view submission.
* For regrade requests, please fill in the [regrade form](https://forms.gle/gmJGC9GAKKjtzgs19).


## Learning Objectives

In this project, you will learn how to

* Access and utilize data in CSV files
* Deal with messy real world datasets
* Use string functions and sorting to order data

**Please go through [Lab P6](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p6) before working on this project.** The lab introduces some useful techniques related to this project.




## Introduction

Data Science can help us understand user behaviors in online platform services. This project is about the rooms in Airbnb. Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. The dataset describes the listing activity and metrics in NYC, NY for 2019. This data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.
you will be using various string manipulation functions that come with Python as well as rolling some of your own to solve the problems posed. Happy coding!

## Directions

Be sure to do [lab-p6](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p6) before starting this project; otherwise you probably won't get very far. Begin by downloading `airbnb.csv` and `test.py`.  Create a `main.ipynb` file to start answering the following questions, and remember to run `test.py` often.  There is no `project.py` this week, use the code from the lab to access the data.  Remember to use the `#qN` format as you have for previous projects.


<h4>You are expected to use the `cell` function you wrote in lab-p6 for all data accesses. </h4>

### #Q1: What room types are present in the airbnb dataset?

Generate a Python list containing the different room types. The order doesn't matter but make sure that your answer doesn't contain duplicate entries.

<!--Note: Some entries in the data set are missing room type information (real-life data is often messy,
unfortunately!).  Missing values are represented as `None`. Do not include `None` in your answer.-->

Now is a good time to run the tests with `python test.py`.  If you did Q1 correctly, it should look like this:

```
Summary:
  Test 1: PASS
  Test 2: not found
  Test 3: not found
  Test 4: not found
  Test 5: not found
  Test 6: not found
  Test 7: not found
  Test 8: not found
  Test 9: not found
  Test 10: not found
  Test 11: not found
  Test 12: not found
  Test 13: not found
  Test 14: not found
  Test 15: not found
  Test 16: not found
  Test 17: not found
  Test 18: not found
  Test 19: not found
  Test 20: not found

TOTAL SCORE: 5.00%
```

### #Q2: What is the average price?

Your answer should be a float value rounded off to 3 decimal places.

### #Q3: Count the number of rooms located in neighborhood "Kingsbridge"? (`neighborhood`=="Kingsbridge")

You can find the value "Kingsbridge" in the `neighborhood` column.

### #Q4: Find the room names containing "superbowl" (case insensitive)

Your answer should be in the form of a Python list. You are expected to write a function to obtain the answer. Make sure your list doesn't contain any duplicates.

Hint: There might be some missing entires in our dataset. You directly skip the row if the room name is missing.

### #Q5: Find the room names containing "free wifi" (case insensitive) or "cable" (case insensitive)

Your answer should be in the form of a Python list. If there are entries that contain both "free wifi" and "cable", make sure to include it only once in your answer. If the room name has a word which contains "cable", such as "Impeccable", include it in your answer. You are expected to use the function from your solution to #Q4. Make sure your list doesn't contain any duplicates.

### #Q6: Which host names (`host_name` column) are anagrams of the phrase "loondar"?

If you liked Professor Langdon's adventures in Da Vinci Code, you'll have fun with this one. :)

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
(Read more here: https://en.wikipedia.org/wiki/Anagram).  For our
purposes, we'll ignore case and spaces when considering whether two words are anagrams of each other.

Hint: although you'll need to loop over all the names to check for
anagrams, checking whether a single word is an anagram of another word
does not require writing a loop.  So if you're writing something
complicated, review the string methods and sequence operations to see
if there is a short, clever solution.

Your answer should be in the form of a Python list. Make sure to remove duplicate entries if present in the list.

### #Q7: List all room ids that require the minimum nights greater than 365 days (`minimum_nights` > 365).

Your answer should be in the form of a Python list. Each room id has string type, not int type.

### #Q8: List all *host ids* who are hosting greater than 50 rooms. (`calculated_host_listings_count` > 50)

Your answer should be in the form of a Python list. Each host id has string type, not int type. Make sure that your answer doesn't contain duplicate entries.

### #Q9 What percentage of rooms are shared rooms? (`room_type` == "Shared room")

Your answer should be a float value rounded off to 3 decimal places.


### #Q10: What are the names of the cheapest rooms in Brooklyn (`neighborhood_group` == "Brooklyn")?

Your answer should be in the form of a Python list. If there is only one cheapest room, that list may contain one entry with that one cheapest room name. If more than one room has the same lowest price, then add them all to your final list. You are expected to write a function to obtain the answer.

### #Q11: What are the names of the cheapest rooms in Manhattan (`neighborhood_group` == "Manhattan")?

Your answer should be in the form of a Python list. If there is only one cheapest room, that list may contain one entry with that one cheapest room name. If more than one room has the same lowest price, then add them all to your final list. You are expected to use the function from your solution for #Q10.

### #Q12: What is the average ratio of the number of reviews to availability? (Ignore rooms that has `availability_365`==0).

Your answer should be a float value rounded off to 3 decimal places.

Hint1: Denominator is the availiability of a room (`availability_365` column). Numerator is the number of reviews of a room (`number_of_reviews` column).

Hint2: Be careful! You need to compute the ratio for each room, then take the average of those ratios. Simply dividing the sum of reviews by the sum of availiability will calculate the wrong answer.

### #Q13: Which room ids have the highest `reviews_per_month` among rooms within (40.50 <= latitude <= 40.75, -74.00 <= longitude <= -73.95)

Your answer should be in the form of a Python list. If there is only one room with maximum number of reviews per month, that list may contain one entry. If more than one room has the same maximum number of reviews per month, then add them all to your final list. You should ignore rooms that have a None value for `reviews_per_month` . You are expected to write a function to obtain the answer.


### #Q14: Which room ids have the highest `reviews_per_month` among rooms within (40.75 <= latitude <= 41.00, -73.95 <= longitude <= -73.85)

Your answer should be in the form of a Python list. If there is only one room with maximum number of reviews per month, that list may contain one entry. If more than one room has the same maximum number of reviews per month, then add them all to your final list. You should ignore rooms that have a None value for `reviews_per_month` . You are expected to use the function from your solution for #Q13.

### #Q15: Which room ids in Queens (`neighborhood_group` == "Queens") have not received a review since 2013?

Your answer should be in the form of a Python list. Include room ids for rooms with the `last_review` less than 2013, and ignore room ids that do not have an entry for `last_review`.


### #Q16: What is the average price of rooms that have greater than 300 reviews?

Your answer should be a float value rounded off to 3 decimal places.

Hints

Step 1) find rooms which have greater than 300 reviews (`number_of_reviews` > 300).

Step 2) calculate their average price of rooms.

### #Q17: What is the average number of reviews of rooms that have price greater than 1000 dollars?

Your answer should be a float value rounded off to 3 decimal places.

Hints

Step 1) find rooms which have price greater than 1000 dollars (`price` > 1000).

Step 2) calculate their average number of reviews.


### #Q18: What percentage of rooms whose name contains the word "sweet" also contain the word "home" in its name? (case insensitive)

Your answer should be a float value rounded off to 3 decimal places. You are expected to write a function that utilizes your solution for #Q4. Note: You do not have to disregard duplicates.

Hint: Denominator is the number of rooms with 'sweet' in their name. Numerator is the number of rooms that have both 'sweet' and 'home' in their name.

### #Q19: What percentage of rooms whose name contains the word "pool" also contain the word "gym" in its name? (case insensitive)

Your answer should be a float value rounded off to 3 decimal places.  You are expected to use the function from your solution to #Q18.

### #Q20: What is the minimum amount of money one needs to spend to stay for 5 days in Queens, and then 10 days in Staten Island? (You can only stay in a total of 2 different rooms, one per `neighborhood_group`)

Your answer should be in the form of type int. You can ignore the `availability_365` column for this problem.

Hint: total cost = (lowest price in Queens with minimum nights less than or equal to 5) * 5 + (lowest price in Staten Island with minimum nights less than or equal to 10)* 10
### Please remember to `Kernel->Restart and Run All` to check for errors, save your notebook, then run the test.py script one more time before submitting the project.

Cheers!
