import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

netflix_titles=pd.read_csv(r"C:\Users\Sigma\Downloads\netflix_titles.csv.zip")
part1=netflix_titles[netflix_titles['type']=="TV Show"]
part2=netflix_titles[netflix_titles['type']=="Movie"]

release_date_tvshow=part1.groupby('release_year').agg({'type': 'count'})
release_date_movie=part2.groupby('release_year').agg({'type': 'count'})
plt.subplot(3,1,1)
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.plot(release_date_tvshow)
plt.subplot(3,1,2)
plt.xlabel('Year')
plt.ylabel('Number of TV Shows')
plt.plot(release_date_movie)
plt.subplot(3,1,3)
plt.xlabel('movies/year')
plt.ylabel('TV Shows/year')
plt.plot((release_date_movie['type']._values[0:46]),(release_date_tvshow['type']._values))
plt.show()
