import pandas as pd 
df=pd.read_csv("weather_data.csv")
# print(df)
print(type(df.day[0])) #It printed str which means string
df=pd.read_csv("weather_data.csv",parse_dates=["day"])      #parse day column as a date type
print(type(df.day[0])) #Now it printed timestamp
print(df)
df.set_index('day',inplace=True) #Now the day will be treated as a index
print(df)

new_df=df.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'no event'
})
print(new_df) #This is inconvinient thought as, just a day difference 31 to 0 makes no sense
                #The better approach would be to give the value of previous day
new_df=df.fillna(method='ffill') #It will get decrypted in future
new_df=df.fillna(method='ffill',limit=1) #It will make sure that filling of values is done in one forward box only
print(new_df)            #'bfill' will do a backward fill

new_df=df.fillna(method='ffill',axis="columns") #It will copy the values from right to left in columns
print(new_df)  

new_df=df.interpolate() #uses Interpolation to solve criteria
print(new_df)

# Sometimes it's better to drop all the rows with NA values 
new_df=df.dropna()
print(new_df)
# what if you don't want to drop a row which has one NA value with some data in other cells

new_df=df.dropna(how="all") #it will only drop if the all cells of a row has missing  info
print(new_df)

#what if you want to delete a row which has (x) number of NA values
#for this we need thereshold command (thresh)
new_df=df.dropna(thresh=2) #>=2 will be deleted
print(new_df)

