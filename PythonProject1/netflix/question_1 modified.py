import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ast

netflix_titles=pd.read_csv(r'C:\Users\Sigma\Downloads\netflix_titles.csv.zip')

part=netflix_titles.loc[ (netflix_titles['type'] == 'TV Show' ) & (netflix_titles['release_year']>=2015) ].copy()
part['country'] = part['country'].str.split(r',\s*', regex=True)
part['cast'] = part['cast'].str.split(r',\s*', regex=True)

part=part.explode('country')

part['ncast'] = part['cast'].apply(lambda x: len(x) if isinstance(x, list) else None)
top_3=part.groupby('country').agg({'type':'count','ncast':'sum'}).sort_values('type', ascending=False).reset_index().rename(columns={'type':'tv s`hows count'}).iloc[0:3]
print(top_3)
print(top_3['ncast']/top_3['tv s`hows count'])
