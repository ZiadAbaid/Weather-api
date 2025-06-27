import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import normal

netflix_titles=pd.read_csv(r"C:\Users\Sigma\Downloads\netflix_titles.csv.zip")


def count_cast(arr):
    i=0
    result=[]
    while i<len(arr):
        if type(arr[i]) is str :
            result.append(len(arr[i].split(',')))
        else :
            result.append(arr[i])
        i+=1
    return result
def Cast_Richness_Score(x,y):
    a= list(count_cast(x))
    b=len(y.index)
    return a*b

cast=netflix_titles['cast']
generes=netflix_titles.groupby('listed_in').agg({'type':'count'}).sort_values('type', ascending=False)
tmp=Cast_Richness_Score(cast,generes)
normal= normal(tmp)
print(tmp)
q1=np.quantile(tmp,0.25)
q3=np.quantile(tmp,0.75)
iqr=q3-q1
lower = q1-1.5*iqr
upper=q3+1.5*iqr
print(lower, q1, q3, iqr , upper )

plt.subplot(2,1,1)
plt.plot(normal)

plt.subplot(2,2,2)
plt.hist(tmp,color='blue')

plt.show()