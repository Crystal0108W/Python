import pandas as pd

#Read in datasets
links = pd.read_csv('MovieLens Data/links.csv')
movies = pd.read_csv('MovieLens Data/movies.csv')
ratings = pd.read_csv('MovieLens Data/ratings.csv')
tags = pd.read_csv('MovieLens Data/tags.csv')
movies[:5]


data = pd.merge(pd.merge(ratings, users), movies)
data.ix[0] #loc() - label based; iloc() - index based; ix() - flexible
# type of (data.ix[0]) is Series

mean_ratings  = data.pivot_table(values = 'rating', index = 'title', columns = 'userId', aggfunc = 'mean', fill_value = 0) #pivot_table
ratings_by_title = data.groupby('title').size() #groupby to get the count of ratings for each title
ratings_by_title #slice
active_titles = ratings_by_title.ix[ratings_by_title >= 150].sort_values(ascending = False)
active_titles[:10] # active_titles is series
ratings_by_title.ix['10 Things I Hate About You (1999)']
mean_ratings = mean_ratings.ix[active_titles]
