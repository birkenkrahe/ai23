# load the mtcars dataset
import pandas as pd
df = pd.read_csv('data/mtcars.csv')
# display the first 5 rows of the dataframe
print(df.head())
# get the sum of the mpg column
print(df['mpg'].sum())
# get the mean of the mpg column
print(df['mpg'].mean())
'''Plot the mpg column as a histogram'''
import matplotlib.pyplot as plt
df['mpg'].plot(kind='hist')
# customize the plot
plt.title('Histogram of mpg')
plt.xlabel('mpg')
plt.ylabel('Frequency')
# save the plot
plt.savefig('histogram.png')

'''plot mpg vs. wt as a scatter plot'''
df.plot(kind='scatter', x='mpg', y='wt')
# customize the plot
plt.title('Scatter plot of mpg vs. wt')
plt.xlabel('mpg')
plt.ylabel('wt')
# save the plot
plt.savefig('scatter.png')
# draw a red trend line using linear regression
import seaborn as sns
sns.regplot(x='mpg', y='wt', data=df, color='red')
# customize the plot
plt.title('Scatter plot of mpg vs. wt')
plt.xlabel('mpg')
plt.ylabel('wt')
# save the plot
plt.savefig('scatter.png')
# display the plot
plt.show()