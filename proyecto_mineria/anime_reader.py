import pandas as pd

users = pd.read_csv('/archive/users_cleaned.csv')
anime = pd.read_csv('/archive/anime_cleaned.csv')
# anime_lists = pd.read_csv('animelists_cleaned.csv')

print(users.head())