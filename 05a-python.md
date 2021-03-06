# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---edited

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>Tuples are immutable. Lists can be changed. The elements in both a list and a tuple have a defined order.
Tuples will work as keys in dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>Sets do not keep order; lists do. Set items must be hashable; list items do not. As a result, searching a set is much quicker. Sets cannot contain duplicates; lists can. 
I would use a list if I was ranking something; I would use a set if I wanted to find something quickly. If I was ranking my favorite movies I'd put them in a list. If I need to search for a movies in a group of my favorite movies, I'd use a set.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>Lambda funcions are anonymous functions. Lambda functions cannot contain  more than one expression. An alternative to def (defining a new function). One benefit is that lambda makes the code cleaner since you can avoid making tons of one-line, one-off functions.

>>If you wanted to sort a list of numbers by absolute value, you might use a lambda.
eg:
nums = [3, -4, 2, 1, -6]
Without lambda, you might create an absolute value function using def absvalue, and then we'd use key=absvalue.
Using lamda, we can do this inline:
sorted([3, -4, 2, 1, -6], key=lambda num: num.abs())

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>List comprehensions are a shortcut for for loops.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>>513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>>7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





