
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

dir = '/Users/kpully/ds/metis/prework/dsp/python/faculty.csv'


# In[3]:

data = pd.read_csv(dir)
df = pd.DataFrame(data)


# In[4]:

df.columns = ['name', 'degree', 'title', 'email']
df


# In[5]:

titles_unique = set()
titles_all = list()
for title in df.title:
    of = title.find('of ')
    title = title[:of]
    #print title
    titles_all.append(title.strip())
    titles_unique.add(title.strip())
    df['stripped title'] = title.strip()


# In[6]:

df.head()


# In[7]:

len(titles_unique)
titles_unique


# In[8]:

degrees_unique = set()
degrees_all = list()
for degree in df.degree:
    degree_list = degree.lower().strip().replace('.', '').split(' ')
    for degree in degree_list:
        degrees_unique.add(degree)
        degrees_all.append(degree)


# In[9]:

degrees_unique.remove('0')


# In[10]:

print len(degrees_unique)
print degrees_unique


# In[11]:

print "PhDs: " + str(degrees_all.count('phd'))
print "MDs: " + str(degrees_all.count('md'))
print "MAs: " + str(degrees_all.count('ma'))
print "BSEds: " + str(degrees_all.count('bsed'))
print "JDs: " + str(degrees_all.count('jd'))
print "MPHs: " + str(degrees_all.count('mph'))
print "SCDs: " + str(degrees_all.count('scd'))
print "MSs: " + str(degrees_all.count('ms'))


# In[12]:

domains = set()
for email in df.email:
    cutoff = email.find('@')
    domain = email[cutoff:]
    domains.add(domain)
domains


# In[13]:

#df.email.to_csv('emails.csv')
#how to get it to a list without the index?


# In[14]:

emails = df.email.tolist


# In[15]:

new_dict = dict()
df.head()


# In[16]:

first_names = list()
last_names = list()
for name in df.name:
    space1 = name.find(' ')
    first_name = name[:space1]
    remaining_name = name[space1 + 1:]
    space2 = remaining_name.find(' ')
    last_name = remaining_name[space2+1:]
    #print 'BREAKDOWN: original name = ' + name + ' / first name = ' + first_name + ' / last name = ' + last_name
    first_names.append(first_name)
    last_names.append(last_name)
df['first_name'] = first_names
df['last_name'] = last_names
df.head(6)


# In[19]:

#faculty_dict = df2.set_index('last_name').T.to_dict('list')


# In[20]:

d= dict([(i,[a,b,c ]) for i, a,b,c in zip(df.last_name, df.degree, df['stripped title'],df.email )])
d


# In[22]:

#d= dict([(i,y,[a,b,c ]) for i,y a,b,c in zip(df.last_name, df.first_name, df.degree, df['stripped title'],df.email )])
#d


# In[24]:

# Select just the columns we want and put them in order
faculty2 = df[['last_name','degree','stripped title','email']]

# Here is the command I was referencing
faculty_dict = ( faculty2                             # our dataframe
                 .set_index('last_name')              # set the index column
                 .groupby(level=0)                    # groupby, note that 'last_name' is level 0 of index
                 .apply(lambda x: x.values.tolist())  # this will be applied to each sub-dataframe created by grouping,
                                                      # it handles the conversion to an array (values) and then a list
                                                      # then pandas will recombine everything back into a dataframe per-groupby
                 .to_dict()                           # finally we make a dictionary out of it!
               )


# In[25]:

faculty_dict


# In[27]:

# Here is the command I was referencing
faculty2 = df[['first_name', 'last_name','degree','stripped title','email']]

professor_dict = ( faculty2
                 .set_index(['first_name', 'last_name'])
                 .groupby(level=[0, 1])                             # two index levels!
                 .apply(lambda x: x.values.tolist())
                 .to_dict()
               )


# In[28]:

professor_dict


# In[29]:

# Here is the command I was referencing
#faculty2 = df[['first_name', 'last_name','degree','stripped title','email']]

professor_dict2 = ( faculty2
                 .set_index(['first_name', 'last_name'])
                 .groupby(level=[1, 0])                             # two index levels!
                 .apply(lambda x: x.values.tolist())
                 .to_dict()
               )


# In[30]:

professor_dict2


# In[ ]:



