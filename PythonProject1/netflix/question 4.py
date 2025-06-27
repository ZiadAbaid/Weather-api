import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


netflix_titles=pd.read_csv(r"C:\Users\Sigma\Downloads\netflix_titles.csv.zip")
tmp=netflix_titles.copy()

tmp['listed_in']=tmp['listed_in'].str.split(r',\s*')
tmp=tmp.explode('listed_in')

print(tmp['listed_in'].mode())
print(netflix_titles['listed_in'].mode())

#this was my first idea
'''iN = netflix_titles['listed_in']
find= np.array(result.index)
print(len(iN),type(find))
c=0
for i in range (0,len(find),1):
    for j in range (0,len(iN),1):
        if (find[i]==iN[j]):
            c+=1
        j+=1
    find[i]+='---count '+str(c)
    c=0
    i+=1
print(find)'''
