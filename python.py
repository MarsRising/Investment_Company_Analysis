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


