import pandas as pd
import numpy as np
from ast import literal_eval

movies_data = pd.read_csv("Data\movies_dataset.csv")
credits = pd.read_csv("Data\credits.csv")

# Select only the columns that are to be used
movies_data = movies_data[['id', 'title','belongs_to_collection', 'budget', 'genres',
                           'original_language', 'popularity', 'production_companies', 
                           'production_countries', 'release_date', 'revenue', 'runtime', 
                           'spoken_languages', 'vote_average', 'vote_count']]

movies_data.drop_duplicates(inplace=True)

movies_data['release_date'].isnull().sum()                      # 87
movies_data = movies_data.dropna(subset=['release_date'])

# Change the data types of the budget, revenue, votecount, id and popularity columns
# If an error is encountered while trying to convert, fill with zero (in the case of the id, with -1)
movies_data['budget'] = pd.to_numeric(movies_data['budget'], errors='coerce').fillna(0).astype(int)
movies_data['revenue'] = movies_data['revenue'].fillna(0).astype(int)
movies_data['vote_count'] = movies_data['vote_count'].fillna(0).astype(int)
movies_data['id'] = pd.to_numeric(movies_data['id'], errors='coerce').fillna(-1).astype(int)
movies_data['popularity'] = pd.to_numeric(movies_data['popularity'], errors='coerce').fillna(0).astype(float)

# Convert release_date to the requested format
movies_data['release_date'] = pd.to_datetime(movies_data['release_date'], format="%Y-%m-%d", errors='coerce')
movies_data['release_date'].isna().sum()                                # 3
# Delete records that could not be converted
movies_data = movies_data.dropna(subset=['release_date'])

movies_data['release_year'] = movies_data['release_date'].dt.year
movies_data['return'] = np.where(movies_data['budget'] != 0, movies_data['revenue'] / movies_data['budget'], 0)

movies_data['belongs_to_collection'] = movies_data['belongs_to_collection'].fillna('{}')
# Convert from string to dict
movies_data['belongs_to_collection'] = movies_data['belongs_to_collection'].apply(literal_eval)

# Flatten the column belongs_to_collection
df_collection = pd.json_normalize(movies_data['belongs_to_collection'])
df_collection = df_collection[['id', 'name']]
df_collection.rename(columns={'id':'collection_id', 'name':'collection_name'}, inplace=True)

# Combine the two datasets
movies_data.drop(['belongs_to_collection'], axis=1, inplace=True)
movies_data = movies_data.join(df_collection)

# Parsing and extract names from genres
movies_data['genres'] = movies_data['genres'].apply(lambda x: literal_eval(x) if x is not None else [])
movies_data['genres'] = movies_data['genres'].apply(lambda x: [dict['name'] for dict in x] if isinstance(x, list) else [])

# Parsing and extract names from production_companies
movies_data['production_companies'] = movies_data['production_companies'].apply(lambda x: literal_eval(x) if x is not None else [])
movies_data['production_companies'] = movies_data['production_companies'].apply(lambda x: [dict['name'] for dict in x] if isinstance(x, list) else [])

# Parsing and extract names from production_countries
movies_data['production_countries'] = movies_data['production_countries'].apply(lambda x: literal_eval(x) if x is not None else [])
movies_data['production_countries'] = movies_data['production_countries'].apply(lambda x: [dict['name'] for dict in x] if isinstance(x, list) else [])

# Parsing and extract names from spoken_languages
movies_data['spoken_languages'] = movies_data['spoken_languages'].apply(lambda x: literal_eval(x) if x is not None else [])
movies_data['spoken_languages'] = movies_data['spoken_languages'].apply(lambda x: [dict['name'] for dict in x] if isinstance(x, list) else [])

# From dataframe credits, convert "cast" and "crew" columns from string to list
credits['cast'] = credits['cast'].apply(lambda x: literal_eval(x) if x is not None else [])
credits['crew'] = credits['crew'].apply(lambda x: literal_eval(x) if x is not None else [])