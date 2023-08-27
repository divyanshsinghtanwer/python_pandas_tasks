# loading the IMDb dataset into a pandas DataFrame.

import pandas as pd
df=pd.read_csv(r"C:\Users\pf3l1\Downloads\IMDB-Movie-Data.csv")
print(df)
print()

#  the first 5 rows of the dataset
pd.set_option('display.max_rows',5)
print(df.head())
print()

# overview of column data types and missing values
print(df.info())
print()

# the columns with missing values
print(df.isnull().sum())
print()

#columns are essential for analyzing movie ratings and details
print(df.loc[:,['Description','Rating']])
print()

# the average runtime of movies in the dataset
print(df['Runtime (Minutes)'].mean())
print()

# the number of movies in each genre
x=df['Genre'].value_counts()
print(x)
print()

# top 5 directors with the most movies 
y=df['Director'].value_counts(sort=True).head(5)
print(y)
print()

# Q10
import matplotlib.pyplot as plt
year_counts=df['Year'].value_counts()
x=df['Year']
fig=plt.figure()
year_counts.plot(kind='line')
plt.xlabel("Year")
plt.ylabel('Number of movies in that year')
plt.title("number of movies in each year")
print()


 # Q11
num_bins = 10
plt.hist(df['Runtime (Minutes)'], bins=num_bins, edgecolor='k', alpha=0.7)
plt.xlabel('Movie Runtimes')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Runtimes')
# Show the plot
plt.show()

# Q12
plt.hist(df['Rating'],bins=10,edgecolor='k')
plt.xlabel('Movie Ratings')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Ratings')
plt.show()
print()

# Q13
print(df['Runtime (Minutes)'].corr(df['Runtime (Minutes)']))

# Q14
print(df['Actors'].value_counts(sort=True).head(3))
print()

# Q15
plt.scatter(df['Rating'],df['Revenue (Millions)'])
plt.xlabel("Ratings")
plt.ylabel("Revenue (Millions)")
plt.title("Relationship between ratings and revenue")
plt.show()

# Q16



# Q17
average_ratings = df.groupby('Year')['Rating'].mean()
plt.figure(figsize=(10, 6))
plt.plot(average_ratings.index, average_ratings.values, marker='o')
plt.title('Average Movie Ratings Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.grid(True)
plt.show()
print()

#21
print((df['Rating']).corr(df['Year']))
print()

#22
print(df.value_counts(subset=['Actors','Director'],sort=True).head(3))
print()

#23
print("correlation of year and runtime is: ",df['Year'].corr(df['Runtime (Minutes)']))
plt.scatter(df['Year'],df['Runtime (Minutes)'])
plt.xlabel("Years")
plt.ylabel("Runtime")
plt.show()
plt.show()

#24
trend=df['Genre'].value_counts(sort=True)
plt.bar(trend.index,trend.values)
plt.show()
print()

#25
#identifying outliers using boxplot
plt.figure(figsize=(10,8))
plt.boxplot(df['Runtime (Minutes)'])
plt.grid()
plt.show()
print()


#28
print("correlation of rating and votes is: ",df['Rating'].corr(df['Votes']))
plt.figure(figsize=(10, 6))
plt.bar(df['Rating'],df['Votes'])
plt.ylabel('Number of Votes')
plt.xlabel('Movie Rating')
plt.title('Relationship between Number of Votes and Movie Rating')
plt.show()