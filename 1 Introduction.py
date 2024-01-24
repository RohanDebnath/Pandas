import pandas as pd 
df=pd.read_csv('weatherHistory.csv')
# print(df)
print(df['Temperature (C)'].max()) #Printed Max temp;
# print(df.columns) #It will print the column heading 

# print(df['Formatted Date'][(df['Temperature (C)'] > 38)])
df.fillna(0,inplace=True)# used to fill NAN value (Data Munging)
print(df['Temperature (C)'].mean())
