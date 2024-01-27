#Melt is also used to transform and reshape data
import pandas as pd 
df=pd.read_csv('weather_11.csv')
print(df)
print()
df1=pd.melt(df,id_vars=['day'])
print(df1)
print()
print(df1[df1['variable']=='chicago'])
print()
#instead of variable and value suppose you want city and temperature
df1=pd.melt(df,id_vars=['day'],var_name='city',value_name='temperature')
print(df1)