import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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



arr=netflix_titles['cast']
result= count_cast(arr)

netflix_titles['ncast'] = result #creating a new column

part= netflix_titles[ (netflix_titles['release_year'] > 2015) & (netflix_titles['type']=="TV Show")]

part=part.groupby("country").agg({'type': 'count', 'ncast': 'sum' })
print(part)

top_3=part.sort_values('type', ascending=False).iloc[0:3]

top_3['avg']=top_3['ncast']/top_3['type']

print(top_3)



