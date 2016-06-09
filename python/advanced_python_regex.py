import pandas as pd

dir = '/Users/kpully/ds/metis/prework/dsp/python/faculty.csv'
data = pd.read_csv(dir)
df = pd.DataFrame(data)
df.columns = ['name', 'degree', 'title', 'email']

titles_unique = set()
titles_all = list()
for title in df.title:
    of = title.find('of ')
    title = title[:of]
    #print title
    titles_all.append(title.strip())
    titles_unique.add(title.strip())
titles_all.count('Professor')
titles_unique

degrees_unique = set()
degrees_all = list()
for degree in df.degree:
    degree_list = degree.lower().strip().replace('.', '').split(' ')
    for degree in degree_list:
        degrees_unique.add(degree)
        degrees_all.append(degree)
degrees_unique.remove('0')
print len(degrees_unique)
print degrees_unique
print "PhDs: " + str(degrees_all.count('phd'))
print "MDs: " + str(degrees_all.count('md'))
print "MAs: " + str(degrees_all.count('ma'))
print "BSEds: " + str(degrees_all.count('bsed'))
print "JDs: " + str(degrees_all.count('jd'))
print "MPHs: " + str(degrees_all.count('mph'))
print "SCDs: " + str(degrees_all.count('scd'))
print "MSs: " + str(degrees_all.count('ms'))

domains = set()
for email in df.email:
    cutoff = email.find('@')
    domain = email[cutoff:]
    domains.add(domain)