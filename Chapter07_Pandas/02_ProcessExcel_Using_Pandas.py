



import pandas as pd

# Read CSV into dataframe
df = pd.read_csv("movies.csv")
print("====== Head ======")
print(df.head())
print("====== Info ======")
print(df.info())
print("===== Describe ========")
print(df.describe())
print("===== End Describe ========")

print("===== Sample 4 records ========")
print(df.sample(4))
print("===== Sample ========")


print("===== Columns ========")
print(df.columns)
print("===== Columns ========")

# Convert imdb_rating to numeric (handles '', NULL, bad data automatically)
df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')

# Drop invalid ratings (NaN)
df = df.dropna(subset=['imdb_rating'])

# ---- All records ----
print("All records:")
print("Min:", df['imdb_rating'].min())
print("Max:", df['imdb_rating'].max())
print("Avg:", df['imdb_rating'].mean())

# ---- Bollywood ----
bollywood = df[df['industry'] == 'Bollywood']
print("\nBollywood:")
print("Min:", bollywood['imdb_rating'].min())
print("Max:", bollywood['imdb_rating'].max())
print("Avg:", bollywood['imdb_rating'].mean())

# ---- Hollywood ----
hollywood = df[df['industry'] == 'Hollywood']
print("\nHollywood:")
print("Min:", hollywood['imdb_rating'].min())
print("Max:", hollywood['imdb_rating'].max())
print("Avg:", hollywood['imdb_rating'].mean())

print("unique ="+ str(df.industry.unique()))
print("Language ="+ str(df.language.value_counts()))

print("============ Extract Subset of Data================")
df_new = df[["title","imdb_rating","industry"]]
print(df_new.head())

df_greater_2000 = df[(df.release_year > 2000)]
print('df_greater_2000 ='+ str(df_greater_2000))

print(df.studio.unique())
print(df[df.studio =='Marvel Studios'])

print('IMDB  max Rating ')
print(df.imdb_rating.max())

print('IMDB  max Rating  Movie')
print(df[(df.imdb_rating == df.imdb_rating.max())])


print('Print how old the Movies is')
df['current_age_of_movie'] = df['release_year'].apply(lambda x: 2026- x)
print(df.sample(5))

print('Profit made by each movie=')
#When yoy say Axis =1 it will give full row its like for loop
df['Profit'] = df.apply(lambda x:x['revenue']-x['budget'], axis=1 )
print(df.head(5))


#By default first column is used as Index. We can change that to any column.

#We are saying use title as new first column and inplace tells to modify existing  data frame.
print(' After resetting index.')
df.set_index('title', inplace=True)
print(df.head(5))

print(' using loc() which is like search')
print(df.loc['Pather Panchali'])


print(' using iloc() which is like search using integer or more like by row index.')
print(df.iloc[0])


print(' using iloc() which is like search using integer or more like by row index. This time using range')
print(df.iloc[2:6])



