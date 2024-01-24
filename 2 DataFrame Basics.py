import pandas as pd 
df=pd.read_csv("weather_data.csv")
print(df)
print(df.columns)
print(df.day)
print(df.event)
print(df['event']) #same as df.event
print(df[['event','day']]) 
print(df.shape) #will print the dimentions
rows,colums=df.shape
print(rows) 
print(df.head()) #gives convinient of printing only few rows
print(df.tail(1)) #gives the first from tail
print(df[2:5]) #will print row 2->4

print(df['temperature'].max())
print(df.describe()) #will print the statistics
print(df.temperature>=32) #will print row wise boolean
print(df[df.temperature>=32])  #Now it will print the rows data
print(df[df.temperature==df.temperature.max()])
# df['day'][df[df.temperature==df['temperature'].max()]]  This syntax is not allowed
print(df['day'][df['temperature'] == df['temperature'].max()]) #If we want to print a spefic column
print(df[['day','temperature']][df['temperature'] == df['temperature'].max()]) #If we want to print a spefic column

print(df.index)
print(df.set_index('day')) #but it will not modify the original one
df.set_index('day',inplace=True) # here it has modifies the original one
print(df)
print(df.loc['1/3/2017'])
df.reset_index(inplace=True) #It will return back the original one
print(df)

df.set_index('event',inplace=True) 
print(df)
print(df.loc['Snow']) #Thus will work on not unique case also
df.reset_index(inplace=True) #It will return back the original one
print(df)