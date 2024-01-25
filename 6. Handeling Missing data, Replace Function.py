import pandas as pd 
import numpy as np
df= pd.read_csv('weather_data_6.csv')
print(df)
#If we want to replace the -99999 with a value
new_df=df.replace(-99999,np.NaN)
print(new_df)
#Incase of general column replacement
new_df=df.replace(
    {
        'temperature':-99999,
        'windspeed':-99999,
        'event':0
    },np.NaN
)
print(new_df)
#using a dictionary to perform this
new_df=df.replace(
    {
        -99999:0,
    }
)
print(new_df)
#Suppose there is some units attached with the Temp and windspeed such as C F or Kmph
new_df=df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]',
},'',regex=True)
print(new_df)

#replacing a list of values with another list
df=pd.DataFrame({
    'score':['exceptional','average','good','poor'],
    'student':['Soumik','Vishal','Jibon','Rohan']
})
print(df)
new_df=df.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(new_df)