
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[5]:

A = np.array([[1, 2, 3], [2,7,4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1,2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

alpha = 6


# In[6]:

#2.1
u + v


# In[7]:

#2.2
u - v


# In[8]:

#2.3
alpha*u


# In[9]:

#2.4
u*v


# In[10]:

#2.5


# In[21]:

#3.1
try:
    print A + C
except:
    print "Not Defined"


# In[20]:

#3.2
try:
    print A - C.transpose()
except:
    print "Not Defined"


# In[22]:

#3.3
try:
    print C.transpose() + 3*D
except:
    print "Not Defined"


# In[28]:

#3.4
try:
    print np.dot(B, A)
except:
    print "Not Defined"


# In[29]:

#3.5
try:
    print np.dot(B, A.transpose())
except:
    print "Not Defined"


# In[30]:

#3.6
try:
    print np.dot(B, C)
except:
    print "Not Defined"


# In[31]:

#3.7
try:
    print np.dot(C, B)
except:
    print "Not Defined"


# In[35]:

#3.8**
try:
    print np.linalg.matrix_power(B, 4)
except:
    print "Not Defined"


# In[33]:

#3.9
try:
    print np.dot(A, A.transpose())
except:
    print "Not Defined"


# In[34]:

#3.10
try:
    print np.dot(D.transpose(), D)
except:
    print "Not Defined"


# In[ ]:



