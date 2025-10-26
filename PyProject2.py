import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('mymoviedb.csv',lineterminator='\n')

print(df.head())
df.describe()
df.info()
df.duplicated().sum()
df['Release_Date']=pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)
df['Release_Date']=df['Release_Date'].dt.year

#columns to be dropped
cols=['Overview','Original_Language','Poster_Url']
df.drop(cols,axis=1,inplace=True)
df.columns

df.dropna(inplace=True)
df.isna().sum()

#split the string into lists
df['Genre']=df['Genre'].str.split(', ')
df=df.explode('Genre').reset_index(drop=True)
df.head()
df['Genre']=df['Genre'].astype('category')

df.nunique()

sns.set_style('whitegrid')

#Most frequent genre
df['Genre'].describe()
sns.catplot(y='Genre',data=df,kind='count',order=df['Genre'].value_counts().index)
plt.title('Genre column distribution')
plt.show()

#movie which got the highest popularity and it's genre
print(df[df['Popularity']==df['Popularity'].max()])

#movie which got the lowest popularity and it's genre
print(df[df['Popularity']==df['Popularity'].min()])

#Year which has the most filmmed movie
df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()