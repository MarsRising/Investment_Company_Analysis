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


df =pr
