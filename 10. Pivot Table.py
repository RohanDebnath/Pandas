#Pivot allows us to transform or reshape data

import pandas as pd 
df=pd.read_csv('weather_10.csv')
print(df)
print()
new_df=df.pivot(index='date',columns='city') #It will automatecally reshape the data
print(new_df)  
print()
#Suppose we want only humidity not temperature
new_df=df.pivot(index='date',columns='city',values='humidity')
print(new_df)
print()
#If you want humidity as rows and columns as cities
print(df.pivot(index='humidity',columns="city"))  

#pivot table is used to summarize and aggregate data inside dataframe
print()
#Lets print the avg temperature and humidity of cities 
print(df.pivot_table(index='city',columns='date'))
print()
print(df.pivot_table(index='city',columns='date',aggfunc='sum')) # we can also define our aggregate function 
print()
print(df.pivot_table(index='city',columns='date',margins=True)) # it will give a mean of all row