#Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pylot as plt
import seaborn as sns
print("libs downloaded!")

#import the data file as a data frame
df = pd.read_csv
#check dataframe
print(df.head())

#check for duplicates
duplicates = df[df.duplicated()]
print(duplicates)

#drop duplicates
df = df.drop_duplicates()
print(df)

#Group by State
grouped = df.groupby('State')
print(grouped)

#Descriptive stats (mean, median, min, and max)
grouped_stats = grouped.agg({
  'Total Long-term Debt':['mean','median','min','max'],
  'Total Equity': ['mean','median','min','max'],
  'Debt to Equity': ['mean','median','min','max'],
  'Total Liabilities': ['mean','median','min','max'],
  'Total Revenue': ['mean','median','min','max'],
  'Profit Margin': ['mean','median','min','max']
})
print(grouped_stats)

#Debt-to-equity ratio = debt-to-income/revenue
df['Debt to Revenue Ratio']=df['Total Long-term Debt']/df['Total Revenue']
#filter to find businesses with negative debt-to-equity ratio
negative_debt_to_income = df[df['Debt to Income Ratio']<0]
print(negative_debt_to_income)

#Scatterplot for debt-to-income ratio to demonstrate our spread
plt.figure(figsize=(10, 6)) 
plt.scatter(df['Business ID'], df['Debt to Income Ratio'], color='blue', alpha=0.6)
#title of visual and labels
plt.title('Debt to Income Ratio Scatter Plot')
plt.xlabel('Bussiness ID')
plt.ylabel('Debt to Income Ratio')
plt.show()

#Filter the data to include only Debt-to-Income ratios greater than 1. These could be of risk.
filtered_df = df[df['Debt to Income Ratio'] > 1]

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(filtered_df['Business ID'].astype(str), filtered_df['Debt to Income Ratio'], color='skyblue')

# Customize the plot with titles and labels
plt.title('Debt to Income Ratios Above 1 by Business ID')
plt.xlabel('Business ID')
plt.ylabel('Debt to Income Ratio')

# Rotate x-axis labels to make them readable if necessary
plt.xticks(rotation=90)

# Show the plot
plt.show()

#Boxplot to what is considered an outlier in this data. Which company's our at risk?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Debt to Income Ratio'], color='lightblue')
plt.title('Boxplot of Debt to Income Ratios')
plt.xlabel('Debt to Income Ratio')
plt.show()

#Final Bar Chart to show business ID's of every company at risk
#calculate Q1
Q1=df['Debt to Income Ratio'].quantile(0.25)
#calculate Q3
Q3=df['Debt to Income Ratio'].quantile(0.75)
#IQR
IQR=Q3-Q1
#Calculate for what is over Q3 (Our at risk Conmpanies)
Q3whisker=Q3+1.5*IQR
#set outliers
outliers = df[(df['Debt to Income Ratio'] > Q3whisker)]

#plot it
plt.figure(figsize=(10, 6))
sns.barplot(x=outliers['Business ID'].astype(str), y=outliers['Debt to Income Ratio'], color='red')
plt.title('Outliers in Debt to Income Ratio')
plt.xlabel('Business ID')
plt.ylabel('Debt to Income Ratio')
plt.xticks(rotation=90)
plt.show()

#Bar Charts of profit margins of the high debt to income ratios. These are at most risk!!  
#Negative Profit Margins
filtered_df.loc[:,'Negative Profit Margin'] = filtered_df['Profit Margin'] < 0
plt.figure(figsize=(12, 6))
sns.barplot(x='Business ID', y='Profit Margin', data=filtered_df,hue='Negative Profit Margin', palette='coolwarm')

#Red negative profit margin
sns.barplot(x='Business ID', y='Profit Margin', data=filtered_df[filtered_df['Negative Profit Margin']], color='red', legend=False)

plt.title('Profit Margin by Business ID (Negative Profit Margins Highlighted)')
plt.xlabel('Business ID')
plt.ylabel('Profit Margin (%)')
plt.xticks(rotation=90)
plt.show()

