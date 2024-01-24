import pandas as pd 
#way 1 from a csv file
df=pd.read_csv('weather_data.csv')

#way 2 from a excel file
# df=pd.read_excel('weather_data.xlsx','sheet_name')

#way 3 from a python dictionary
weather_data={
                'day':['21/02/2024','22/01/2024','23/01/2024'],
                'temperature': [10,11,12],
                'windspeed':[5,8,12],
                'event':['Foggy','Mist','Cloudy']
}
df=pd.DataFrame(weather_data)
print(df)

#way 4 from a tuple list

weather_data=[
                ('21/02/2024',10,32,'Rain'),
                ('22/01/2024',1,2,'Snow'),
                ('23/02/2024',12,9,'Sunny'),
                ]
df=pd.DataFrame(weather_data) #In this way of creation we need to provide column name or else 0 1 2 3... will be by default column name
print(df)
df=pd.DataFrame(weather_data,columns=["Day","Temperature","Wind Speed","Weather Condition"]) 
print(df)

#From a Hash Dictionary
weather_data=[
    {'day':'21/01/2024','temperature':23},
    {'day':'22/01/2024','temperature':24},
    {'day':'23/01/2024','temperature':25},
]
print(pd.DataFrame(weather_data))