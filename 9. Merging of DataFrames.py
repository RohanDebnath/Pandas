import pandas as pd 
df1=pd.DataFrame({
    'city':['Kolkata','Pune','Bangalore'],
    'temperature':[12,23,32]
})
print(df1)
df2=pd.DataFrame({
    'city':['Kolkata','Pune','Bangalore'],
    'humidity':[22,45,30]
})
print(df2)

df3=pd.merge(df1,df2,on='city') #better way from concatination
print(df3)

#What if there is mismatch of city names?
df1=pd.DataFrame({
    'city':['Kolkata','Pune','Bangalore','Gurugram'],
    'temperature':[12,23,32,34]
})
df2=pd.DataFrame({
    'city':['Kolkata','Pune','Bangalore','Mumbai'],
    'humidity':[22,45,30,36]
})
df3=pd.merge(df1,df2,on='city')  
print(df3)#Still print the same by ignoring the new added cities
#------Thus it's working like inner join of SQL-----

#to do outer join
df3=pd.merge(df1,df2,on='city',how='outer')  #In how we can put the type of join we want 
print(df3)                                   #Note-> Left and right is decided by the order df1 is left and df2 is right

#If you want a indicator flag to know from where this data came form
df3=pd.merge(df1,df2,on='city',how='outer',indicator=True)
print(df3)

#Supoose those Dataframe's key have same column name 
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df3=pd.merge(df1,df2,on='city')
print(df3) #Commnon element will show data as x and y 
#Suppose we want 
