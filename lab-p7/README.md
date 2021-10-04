# Lab 7: Dictionaries

# WARNING: Unless you took a time portal to become my student in the past, this is not the correct repository :) Please go to the correct github repository for the current semester. If you are a Spring'21 semester student though, you are in the right place.

In this lab, we'll practice using dictionaries to help you get ready for P7. 
Start these exercises in a new Jupyter notebook.

## Exercises

### Counting Letters

Fill in the blanks so that `counts` becomes a dictionary where each
key is a character and the corresponding value is how many times it
appeared in the string `PI`.

Question:  Before beginning, which character
do you think will occur the most often?

*TAs: Ask three different students to provide the correct response to each ????
one at a time, and wait for a student response before entering the code.*

```python
PI = "three, dot, one, four, one, five, nine, two, six, five, three, five, nine"
counts = {}
for char in ????:
    if not char in counts:
        counts[????] = ????
    else:
        ????[char] += ????
counts
```

If done correctly, your code output should be smilar to something like this:

```python
{'t': 4, 'h': 2, 'r': 3, 'e': 11, ',': 12, ' ': 12, 'd': 1, 'o': 5, 'n': 6, 'f': 4, 'u': 1, 'i': 6, 'v': 3, 'w': 1, 's': 1, 'x': 1}
```
*TAs: Ask students what would happen if they changed the statement to 'if char not in counts'*

### Counting Words

Fill in the blanks such that counts becomes a dictionary where each key is a word in a list generated from the string `PI` and the corresponding value is how many times it occured in `PI`.

*TAs:  Ask students how to get a list of words from a string.  Pause before continuing.*

```python
PI = "three, dot, one, four, one, five, nine, two, six, five, three, five, nine"
counts = {}
for word in PI.????(????):
    if ????:
        ????
    else:
        ????
counts
```

If done correctly, your code output should be smilar to something like this:

```python
{'three': 2, 'dot': 1, 'one': 2, 'four': 1, 'five': 3, 'nine': 2, 'two': 1, 'six': 1}
```

*TAs: Make a Zoom poll to ask students if you should wait, continue, or go back.
Run the poll.*

### Dictionary from Two Lists

Fill in the blanks to create a dictionary that maps the English words in list `keys` to their corresponding Spanish translations in list `vals`:

*Question: Before you write the code, ask yourself...what is this code trying to do?*


```python
keys = ["two", "zero"]
vals = ["dos", "cero"]
en2sp = ???? # empty dictionary
for i in range(len(????)):
    en2sp[keys[????]] = ????
en2sp
```

The resulting dictionary containing the mapping from English to Spanish
words, should look like this:

```python
{'two': 'dos', 'zero': 'cero'}
```

Now lets try using your `en2sp` dictionary to partially translate the following English sentence.
Not exactly a replacement for Google translate just yet, but it's
a good start...

```python
words = "I love Comp Sci two two zero".split(" ")
for i in range(len(words)):
    default = words[i] # don't translate it
    words[i] = en2sp.get(words[i], default)
" ".join(words)
```
*Question: What is the purpose of the 'default' variable?*

*Question: What is the purpose of the line words[i] = en2sp.get(words[i], default)?*



### Flipping Keys and Values

What if we want a dictionary to convert from Spanish back to English?

*Question:  What does flipping keys and values mean? 
TAs:  Ask a different student to state what each ???? will be.
Pause and enter their response.
Test it.*


```python
sp2en = {}
for en in en2sp:
    sp = ????
    sp2en[sp] = ????
sp2en
```

You should get this:

```python
{ 'dos': 'two', 'cero': 'zero'}
```

### Dictionary Division

What if we want to do multiple division operations, but we have all our
numerators in one dictionary and all our denominators in another. 
Can you fill in the missing code to help do these divisions correctly?

*TAs:  Ask students to try this on their own. 
Consider putting students into breakout rooms with a random partner.
Bring students back after 5 minutes and for a volunteer to demo their code.*

```python
numerators = {"A": 1, "B": 2, "C": 3}
denominators = {"A": 2, "B": 4, "C": 4}
result = {}
for key in ????:
    result[????] = ????[key] / ????[key]
result
````

If done correctly, you should get `{'A': 0.5, 'B': 0.5, 'C': 0.75}`.



### Ordered Print

Imagine that a dorm kept stastics on the number of noise complaint incidents in different years.
Complete the code so it prints the incidents per year, with earliestyear first.

*TAs: Ask a student to suggest each ????.
Wait for a response, enter it in, and then ask a different student for the next ????*

```python
incidents = {2017: 14, 2020: 18, 2018: 13, 2019: 16, 2021: 25, 2016: 10}
keys = sorted(list(????.keys()))
for k in ????:
    print(k, incidents[????])
```

``` your result should look like this:
2016 10
2017 14
2018 13
2019 16
2020 18
2021 25
```

*TAs: Make a Zoom poll to ask students if you should wait, continue, or go back.
Run the poll.*

### Histogram

*TAs:  Ask students to try this on their own. 
Consider putting students into breakout rooms with a random partner.
Bring students back after 5 minutes and have one student screen share their code.*

Modify the above code so it prints a yearly vaule histogram using the '*' character, like this:

```
2016 **********
2017 **************
2018 *************
2019 ****************
2020 ******************
2021 *************************
```

### Dictionary Max
*TAs:  Ask students to try this on their own.
Answer questions as students pose them.*

Complete the following code to find the year with the highest number of incidents:

```python
incidents = {2017: 14, 2020: 18, 2018: 13, 2019: 16, 2021: 25, 2016: 10}
best_key = None
for key in incidents:
    if best_key == None or incidents[????] > incidents[????]:
        best_key = ????
print("Year", best_key, "had", incidents[????], "incidents (the max)")
```
