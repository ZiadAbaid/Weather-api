import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

netflix_titles=pd.read_csv(r"C:\Users\Sigma\Downloads\netflix_titles.csv.zip")
tmp = netflix_titles.explode('country')

result=tmp.groupby('release_year')['country'].agg(lambda x: x.mode() if not x.mode().empty else None)

netflix_titles['country'] = (netflix_titles['country'].fillna('').str.split(r',\s*'))

print(result)
