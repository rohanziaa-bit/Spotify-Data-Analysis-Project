import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data Set/dataset.csv') 
print(df.head(10))

print (df.info())
print (df.columns)

print (df.isnull().sum())
print (df.duplicated().sum())

print (df['track_id'].duplicated().sum())

print (df.value_counts('track_id').head(10))

print (df[df['track_id'] == '6S3JlDAGk3uu3NtZbPnuhS'][['track_id', 'track_name', 'artists', 'track_genre']])

genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)
print (genre_popularity)

sns.barplot(
    x=genre_popularity.index,
    y=genre_popularity.values
)


plt.title('Top 10 genres by avarage popularity')
plt.xlabel('Genres')
plt.ylabel('Average Popularity')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print (df[['energy','popularity']].corr())
print (df[['danceability','popularity']].corr())
print (df[['loudness','popularity']].corr())

numeric_df = df[['danceability','energy','loudness',
                 'speechiness','acousticness','instrumentalness',
                 'liveness','valence','tempo','popularity']]
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Spotify Features correlation heatmap')
plt.tight_layout()
plt.show()

print (df['track_id'].nunique())


print ("total rows:",len(df))
print ("Unique track ID:",df['track_id'].nunique())

print (df['track_id'].value_counts().head(10))

print (df['track_name'].nunique())

top_10_song = df['track_name'].value_counts().head(10)

analysis_by_song = df[df['track_name'] == "Run Rudolph Run"][['track_id', 'track_name', 'artists', 'track_genre']]
print (analysis_by_song)

print (analysis_by_song['track_genre'].nunique())
print (analysis_by_song['track_genre'].unique())
print (analysis_by_song['track_id'].nunique())

print (df['track_genre'].nunique())
print (df['track_genre'].unique())

print (df['track_genre'].value_counts().head(10))

genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)
print (genre_popularity)

print (df.columns)

print (df.groupby('explicit')['track_id'].count())

print (df.groupby('explicit')['popularity'].mean())

print (df['duration_ms'].mean())

print (df['duration_ms'].max())
print (df['duration_ms'].min())

filterred = df[df['duration_ms'] == 0][['track_id','track_name','artists','track_genre']]
print (filterred)


print (df['track_name'].isnull().sum())
print (df['artists'].isnull().sum())

df_Cleane = df.dropna(subset=['track_name','artists'])

print ("before clearning",df.shape)
print ("after cleaning",df_Cleane.shape)

print (df.duplicated().sum())
print (df.isnull().sum())

missing_rows = df[df[['artists','album_name','track_name']].isnull().any(axis=1)]
print (missing_rows[['track_id','artists','album_name','track_name']])

remove_missing_value = df.dropna(subset=['artists','album_name','track_name'])

print ("before removing",df.shape)
print ("after",remove_missing_value.shape)
print ("Missing values after cleaning")
print (remove_missing_value.isnull().sum())


histograms = df['popularity']

plt.hist(histograms, color='skyblue',edgecolor='black')

plt.xlabel('Popularity score ki ranges')
plt.ylabel('Har range mein songs ki tadaad')
plt.title('Distribution of Song Popularity')
plt.show()

plt.figure(figsize=(10,5))

sns.boxplot(
    y=df['popularity'],
    color='skyblue'
)
plt.title('Distribution of track by popularity',fontsize=14)
plt.ylabel('Popularity score',fontsize=11)
plt.xlabel('')

plt.tight_layout()
plt.show()


plt.figure(figsize=(10,5))

sns.boxplot(
    y=df['popularity'],
    color='skyblue'
)

plt.title('Distribution by energy')
plt.xlabel('')
plt.ylabel('Energy Score')


# plt.tight_layout()
# plt.show()

plt.figure(figsize=(10,5))

sns.scatterplot(
    y=df['popularity'],
    x=df['energy'],
    color='red'
)

plt.title('Relationship Between Track Energy and Popularity')
plt.xlabel('Energy Score')
plt.ylabel('Popularity Score')

plt.tight_layout()
plt.show()


plt.figure(figsize=(10,5))

sns.scatterplot(
    y=df['popularity'],
    x=df['danceability'],
    color='red'
)

plt.title('Relationship Between Danceability and Popularity')
plt.xlabel('Danceability Score')
plt.ylabel('Popularity Score,')

plt.tight_layout()
plt.show()



comparision = df[[
    'energy',
    'danceability',
    'valence',
    'tempo',
    'popularity'
]]

select = comparision.sample(1000)

sns.pairplot(select, hue='popularity', palette='coolwarm')

plt.tight_layout()
plt.show()

