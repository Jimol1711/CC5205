import pandas as pd

users = pd.read_csv('users_cleaned.csv')
anime = pd.read_csv('anime_cleaned.csv')
anime_lists = pd.read_csv('animelists_cleaned.csv')

print(users.head())