import pandas as pd 
df=pd.read_csv('weather_by_cities_7.csv')
print(df)
# 1. FInd the max temp in each of the cities 
# 2. Fine the avg wind speed in each city
g=df.groupby('city')
print(g) # Now G has the object in the same representation as (Object of code 7.png)
for city, city_df in g:
    print(city)
    print(city_df)

#What if you want he data frame for a particular city only
print(g.get_group('mumbai'))

#to have the max temperature in each cities
print(g.max())
print(g.describe()) #It will say the possible operation 
