## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>>There are 8 different degrees.
PhDs: 31
MDs: 1
MAs: 1
BSEds: 1
JDs: 1
MPHs: 2
SCDs: 6
MSs: 2


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>>There are 3 different titles.
Assistant Professor: 12
Associate Professor: 12
Professor: 13


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
>>
0     bellamys@mail.med.upenn.edu
1                warren@upenn.edu
2               bryanma@upenn.edu
3              jinboche@upenn.edu
4              sellenbe@upenn.edu
5     jellenbe@mail.med.upenn.edu
6               ruifeng@upenn.edu
7     bcfrench@mail.med.upenn.edu
8              pgimotty@upenn.edu
9         wguo@mail.med.upenn.edu
10        hsu9@mail.med.upenn.edu
11       rhubb@mail.med.upenn.edu
12      whwang@mail.med.upenn.edu
13      mjoffe@mail.med.upenn.edu
14    jrlandis@mail.med.upenn.edu
15            liy3@email.chop.edu
16     mingyao@mail.med.upenn.edu
17              hongzhe@upenn.edu
18             rlocalio@upenn.edu
19    nanditam@mail.med.upenn.edu
20    knashawn@mail.med.upenn.edu
21     propert@mail.med.upenn.edu
22       mputt@mail.med.upenn.edu
23             sratclif@upenn.edu
24             michross@upenn.edu
25       jaroy@mail.med.upenn.edu
26     msammel@cceb.med.upenn.edu
27                shawp@upenn.edu
28        rshi@mail.med.upenn.edu
29       hshou@mail.med.upenn.edu
30     jshults@mail.med.upenn.edu
31    alisaste@mail.med.upenn.edu
32     atroxel@mail.med.upenn.edu
33       rxiao@mail.med.upenn.edu
34        sxie@mail.med.upenn.edu
35                 dxie@upenn.edu
36     weiyang@mail.med.upenn.edu


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>>There are 4 different email domains:
{'@cceb.med.upenn.edu', '@email.chop.edu', '@mail.med.upenn.edu', '@upenn.edu'}

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:
>>>
{'Bellamy': [' Sc.D.', 'Assistant Professor ', 'bellamys@mail.med.upenn.edu'],
 'Bilker': ['Ph.D.', 'Assistant Professor ', 'warren@upenn.edu'],
 'Bryan': [' PhD', 'Assistant Professor ', 'bryanma@upenn.edu'],

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
>>>
{'Bellamy': [[' Sc.D.', 'Assistant Professor', 'bellamys@mail.med.upenn.edu']],
 'Bilker': [['Ph.D.', 'Assistant Professor', 'warren@upenn.edu']],
 'Bryan': [[' PhD', 'Assistant Professor', 'bryanma@upenn.edu']],
```

Print the first 3 key and value pairs of the dictionary:

>>
{('A.',
  'Localio'): [[' JD MA MPH MS PhD',
   'Assistant Professor',
   'rlocalio@upenn.edu']],
 ('Alisa',
  'Stephens'): [[' Ph.D.',
   'Assistant Professor',
   'alisaste@mail.med.upenn.edu']],
 ('Andrea',
  'Troxel'): [[' ScD', 'Assistant Professor', 'atroxel@mail.med.upenn.edu']],

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

>>
{('Bellamy',
  'Scarlett'): [[' Sc.D.',
   'Assistant Professor',
   'bellamys@mail.med.upenn.edu']],
 ('Bilker', 'Warren'): [['Ph.D.', 'Assistant Professor', 'warren@upenn.edu']],
 ('Bryan', 'Matthew'): [[' PhD', 'Assistant Professor', 'bryanma@upenn.edu']],

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

