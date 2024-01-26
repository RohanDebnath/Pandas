import pandas as pd
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
print(india_weather)
us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather
print(us_weather)

df=pd.concat([india_weather,us_weather],ignore_index=True) #If we don't do this ignore_index then the index would be 012012
print(df)

#We can put a key as an additional index
df=pd.concat([india_weather,us_weather],keys=["india","us"])
print(df)
#Now we can retrive the subset of out dataFrame
print(df.loc['us'])

#Observe this

temperature_df=pd.DataFrame({
        "city": ["mumbai","delhi","banglore"],
        "temperature": [32,45,30],
})
windspeed_df=pd.DataFrame({
        "city": ["mumbai","delhi","banglore"],
        "windspeed": [3,5,7],
})
df = pd.concat([temperature_df,windspeed_df])
print(df) #It gives NaN values to the missing cells

#To avoid this we can 
df = pd.concat([temperature_df,windspeed_df],axis=1) #Without using axis they will mark them as column but still not correct as city name have two columns
print(df)
s=pd.Series(["Humid","Dry","Rainy"],name='event')
df=pd.concat([temperature_df,s],axis=1)
print(df)
