import pandas as pd
dir = '/Users/kpully/ds/metis/prework/dsp/python/faculty.csv'
data = pd.read_csv(dir)
df = pd.DataFrame(data)
df.columns = ['name', 'degree', 'title', 'email']
df.email.to_csv('emails.csv')