# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. find [dir] -name [search_pattern]
2. grep: stands for global regular expression print. It searches files for lines that match a pattern and returns the results. It is case sensitive.
3. cd ../../
4. .. (parent/enclosing directory)
5. env: returns a list of environment variables
6. touch: creates a new file inside the working directory. It takes in a file name as an argument and creates a new empty file in the current working directory.
7. sed 's/he/she' file.txt: stands for "stream editor." It accepts standard input and modifies itbased on an expression expression before displaying it as output data. In the expression 's/he/she', s stands for "substitution," he is the search string, and she is the replacement string.
8. rm -r directory_name: deletes a directory and all of its child directories
9. mkdir directory_name: takes in a directory name as an argument and creates a new directory in the current working directory
10. mv file.txt directory_name/: moves the file (first argument) into the destination directory (second argument)

---

###Q2.  List Files in Unix   

What do the following commands do:  
>>`ls`  : lists the files in a directory (short listing)  
`ls -a`  : lists all content in the working directory, including hidden files and directories  
`ls -l`  : long listing  
`ls -lh`  : long listing with Human readable file sizes  
`ls -lah`  : displays the long format listing, all files,  
`ls -t`  : listing sorted by modification time  
`ls -Glp` : inhibit display of group information, append indicator to entries  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>>1. -p: displays directories with /
2. -R: displays subdirectories as well
3. -1: displays each entry on a line
4. -d: displays only directories
5. -m: displays the names as a comma-separated list

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command expects the input from stdin and executes over the input

 

