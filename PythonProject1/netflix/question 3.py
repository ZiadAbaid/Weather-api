import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


netflix_titles=pd.read_csv(r"C:\Users\Sigma\Downloads\netflix_titles.csv.zip")

groups=pd.cut(netflix_titles['release_year'],[i for i in range(1925,2022,5)])
print(netflix_titles.columns)
tmp=netflix_titles.isnull()
tmp['groups']=groups
z=tmp.groupby('groups', observed=True).agg(
    {'show_id':'sum','type': 'sum', 'title': 'sum','director':'sum', 'cast':'sum','country':'sum','date_added':'sum',
     'release_year':'sum','rating':'sum','duration':'sum','listed_in':'sum',
     'description':'sum'})
 #boolean : true values are 1 , false are 0
print(z)

x=np.arange(0,12,1)
y=np.arange(1940,2020,5)
plt.contourf(x,y,z,cmap=plt.cm.jet)
plt.ylim(1980,2020)
plt.colorbar()
plt.show()
