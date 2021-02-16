# Project 4: Pokémon Simulation

## Corrections/Clarifications
None yet.

**Find any issues?** Report to us: 

- Tim Ossowski <ossowski@wisc.edu>
- Sayali Alatkar <alatkar@wisc.edu>


## Learning Objectives

In this project, you will walk through how to

* Use conditional statements to write programs with more complicated logic
* Practice writing more functions
* Begin using good coding practices outlined in [Lab P4](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p4)

**Please go through [Lab P4](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p4) before working on this project.** The lab introduces some useful techniques related to this project.

## Overview

For this project, you'll be using the data from `pokemon_stats.csv` to
simulate Pokémon battles. This data was gathered by the Python program
`gen_csv.ipynb` from the website https://www.pokemondb.net/.  This project will
focus on **conditional statements**. To start, download `project.py`,
`test.py` and `pokemon_stats.csv`. You'll do your work in a Jupyter Notebook,
producing a `main.ipynb` file. You'll test as usual by running `python test.py`
to test a `main.ipynb` file.

We won't explain how to use the `project` module here (the code in the
`project.py` file). The lab this week is designed to teach you how it
works. So, before starting P4, take a look at [Lab P4](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p4).

This project consists of writing code to answer 20 questions. If
you're answering a particular question in a cell in your notebook, you
need to put a comment in the cell so we know what you're answering.
For example, if you're answering question 13, the first line of your
cell should contain `#q13`.

In this project, you will have to write several functions and keep adding more details to them according to the instructions. When you are adding more things in your functions, **we want you to follow the Good Coding Style for Functions** described in [Lab P4](https://github.com/msyamkumar/cs220-s21-projects/tree/master/lab-p4). Therefore, you should only keep the latest version of your functions in your notebook file. For example, in P4 you are asked to write 5 functions(`simple_battle`, `most_damage`, `num_hits`, `battle`, and `final_battle`), so there should only be the latest version of these 5 functions in your submitted notebook file.

## Questions and Functions

For the first few questions, we will try to simulate a very simple 'battle'.
Create a function `simple_battle(pkmn1, pkmn2)` which simply returns the name of
the Pokémon with the highest stat total.

**Hint: In Lab P4, you created a helper function which could be very useful here.**

### #Q1: What is the output of `simple_battle('Jigglypuff', 'Squirtle')`?

### #Q2: What is the output of `simple_battle('Steelix', 'Mankey')`?

---

While we are off to a good start, the function is not quite finished yet. For instance,
consider the Pokémon Charmander and Chimchar. Both of them have the same stat total
of 309. In such cases, we want our function to return the string `'Draw'` instead of
choosing between the two Pokémon.

### #Q3: What is the output of `simple_battle('Krabby', 'Seel')`?

---

Our function `simple_battle` is quite rudimentary. Sometimes, when two Pokémon meet in the wild,
the weaker one will run away if it senses it is outmatched. In this case, we want our function to return
a message saying the pokemon ran away. Modify `simple_battle` so that it returns `'<pkmn_name> ran away'` 
if `|stat total of pkmn1 - stat total of pkmn2| > 300`. Make sure the function says the Pokémon with the lower stat
total ran away!

### #Q4: What is the output of `simple_battle('Piplup', 'Arceus')`?

### #Q5: What is the output of `simple_battle('Weavile', 'Azurill')`?

---

Our function `simple_battle` is a good start, but we can make our battles a bit
more interesting. Let us set up some rules for our battles.

1. The Pokémon take turns attacking each other.
2. The Pokémon with the higher Speed stat attacks first.
3. On each turn, the attacking Pokémon can choose between two moves - Physical
or Special
4. Based on the move chosen by the attacking Pokémon, the defending Pokémon
receives damage to its HP.
5. If a Pokémon's HP drops to (or below) 0, it faints and therefore loses
the battle.

The damage caused by a Pokémon's Physical move is `10 * Attack stat of
Attacker / Defense stat of Defender`, and the damage caused by a Pokémon's
Special move is `10 * Sp. Atk. stat of Attacker / Sp. Def. stat of Defender`.

**If a Pokémon wants to win, it should always choose the move which will do
more damage.**

For example, let the attacker be Scraggy and the defender be Tranquill. Their
stats are as follows:
```python
>>> project.print_stats('Scraggy')
Name :  Scraggy
Region :  Unova
Type 1 :  Dark
Type 2 :  Fighting
HP :  50
Attack :  75
Defense :  70
Sp. Atk :  35
Sp. Def :  70
Speed :  48
>>> project.print_stats('Tranquill')
Name :  Tranquill
Region :  Unova
Type 1 :  Normal
Type 2 :  Flying
HP :  62
Attack :  77
Defense :  62
Sp. Atk :  50
Sp. Def :  42
Speed :  65
>>>
```
The damage caused by Scraggy's physical move will be `10*75/62`, which is `12.0967`,
while the damage caused by its special move will be `10*35/42`, which is `8.33`.
**So, in this case, when facing Tranquill, Scraggy would always choose its physical
move to do `12.0967` (upto 4 decimal places) damage.**

Copy/paste the following code in a new cell of your notebook and fill in the details.

```python
def most_damage(attacker, defender):
    physical_damage = 10 * project.get_attack(attacker)/project.get_defense(defender)
    special_damage = ???
    if ???:
        return physical_damage
    else:
        ???
```

Verify that `most_damage('Scraggy', 'Tranquill')` returns `12.0967` (up to 4 decimal places).

For the following questions, assume the attacking pokemon chooses the move that does the most damage:


### #Q6: How much damage does Sudowoodo do to Mareep?

### #Q7: How much damage does Blastoise do to Weedle?

---

Now that we have a way of calculating the damage done by the Pokémon during
battle, we have to calculate how many hits each Pokémon can take before fainting.

Going back to our previous example, we saw that Scraggy does `12.0967` (upto 4 decimal places) damage to
Tranquill, each turn. Since Tranquill has HP `62`, it can take a total of `62/12.0697
= 5.125` hits, which is rounded up to `6` hits. So, Tranquill
can take `6` hits from Scraggy before it faints.



### #Q8: How many hits can Caterpie take from Wartortle?

**Hint: If the defending pokemon has 30 HP and the attacking pokemon does 20 damage each turn, it will take 2 turns before the defender faints instead of 30 / 20 = 1.5. You might want to use the method [math.ceil()](https://docs.python.org/3/library/math.html) here. First import the module math and then look up the documentation of math.ceil to see how you could use it.**

Copy/paste the following code in a new cell of your notebook and fill in the details.

```python
def num_hits(attacker, defender):
    return math.ceil(project.get_hp(???)/???)
```



### #Q9: How many hits can Aggron take from Pikachu?

### #Q10: How many hits can Pikachu take from Aggron?

---

Since Aggron can take more hits from Pikachu than Pikachu can from Aggron, clearly
Aggron would win in a battle between the two. With the tools we have created
so far, we can now finally create a battle simulator. Copy/paste the following
code in a new cell of your notebook and fill in the details.


```python
def battle(pkmn1, pkmn2):
    #TODO: Return the name of the pkmn that can take more hits from the other
    # pkmn. If both pkmn faint within the same number of moves, return the
    # string 'Draw'
```

### #Q11: What is the output of `battle('Krabby', 'Scraggy')`?

### #Q12: What is the output of `battle('Charizard','Krabby')`?


---

You may have noticed that the function `battle` does not quite follow all the rules
that we laid out at the beginning. Look at the output of `battle('Swadloon', 'Palpitoad')`.
You will find that it is a draw, since they can both take 7 hits from the other Pokémon.
But since Palpitoad has a higher Speed, it attacks first, so it will land its
seventh hit on Swadloon, before Swadloon can hit Palpitoad. So, even though they
both go down in the same number of moves, Palpitoad should win the battle.

Go back and modify `battle()` so that if both Pokémon faint in the same number of
moves, the Pokémon with the higher Speed wins. If they both have the same Speed,
then the battle should be a `'Draw'`.

### #Q13: What is the output of `battle('Shuckle', 'Shellder')`?

### #Q14: What is the output of `battle('Charmander', 'Tympole')`?

### #Q15: What is the output of `battle('Mudkip', 'Gulpin')`?

---

One last rule we need to implement is the run away feature we coded in simple_battle(). 
It is more reasonable to compare the number of hits a Pokémon can take instead of total stats
in deciding whether it should run away. For example, consider
a battle between Pikachu and Incineroar. Since Incineroar can take 15 hits from Pikachu, 
but Pikachu can only take 2 hits from Incineroar, Pikachu should run away from this battle. 

Modify `battle()` so that if `abs(num_hits_pkmn1_can_take - num_hits_pkmn2_can_take) > 10`, the function
returns `<pkmn_name> ran away'`. Make sure the function says the Pokémon that can take 
less hits ran away!


### #Q16: What is the output of `battle('Shuckle', 'Ursaring')`?

### #Q17: What is the output of `battle('Metagross', 'Noibat')`?


---

Our function `battle` is now working just as intended. But let us build some checks
and balances into the function, to make it more reasonable. We will assume that
Pokémon from different regions cannot battle each other, since they can't both meet
each other.

Create a new function `final_battle(pkmn1, pkmn2)` so that if two Pokémon from
different regions try to fight each other, the function returns `'Cannot battle'`.
If both Pokémon are from the same region, the battle proceeds as before.

### #Q18: What is the output of `final_battle('Geodude', 'Snivy')`?

---

This restriction however, is a little too harsh. We can assume that Pokémon whose
type (Type 1 or Type 2) is `Flying` can reach other regions by flying there.

Modify `final_battle` so that even if the two Pokémon are from different regions, if the
Type 1 **or** Type 2 of **both** pokemon are 'Flying', then the battle can
take place as before, since they will be able to fly to eachother and battle.

### #Q19: What is the output of `final_battle('Zapdos', 'Foongus')`?

### #Q20: What is the output of `final_battle('Starly', 'Pidgey')`?

---


That will be all for now. If you are interested, you can make your `battle` functions
as complicated as you want. Good luck with your project!
