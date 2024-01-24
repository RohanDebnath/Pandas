import pandas as pd 
df = pd.read_excel("stock_data.xlsx","Sheet1") #Note there was an extra row which needed modification
print(df)
print()
df=pd.read_excel("stock_data.xlsx",skiprows=1) #header=1 will also produce the same output
print(df)
print()
#suppose you want to give an extra heading by yourself
df=pd.read_excel("stock_data.xlsx",skiprows=1,header=None,names=["Name 1","Name 2","Name 3","Name 4","Name 5"])
print(df) 
print()
#suppose we want to read only few rows
df=pd.read_excel("stock_data.xlsx",skiprows=1,nrows=3)
print(df)
print()
#to fill values with NAN 
df=pd.read_excel("stock_data.xlsx",skiprows=1,na_values=["not available","n.a."])
print(df)

#If we see carefully then we will notice that in revenue as -1 value which is not practically possivble
#but the eps -1 value is pratically possible 
print()
df = pd.read_excel("stock_data.xlsx", skiprows=1, na_values={
    'eps': ["not available", "n.a.", -1],
    'revenue': ["not available", "n.a.", -1], #Nahi hua
    'people': ["not available", "n.a."]
})
print(df)

# Writing to CSV/EXCEL file
print("Our new File")
df.to_excel('new.xlsx',index=False)#if we don't want the index to include we give index=false
newDf=pd.read_excel("new.xlsx")
print(newDf)

# df.to_excel('new.xlsx', columns=['tickers', 'eps'], index=False)
print()

def convert_people_cell(cell):
    if cell=="n.a.":
        return '200'
    return cell

df = pd.read_excel("new.xlsx", converters={
    'price': convert_people_cell
})
print(df)

df.to_excel('new.xlsx',index=False) #This will permanently write to excel file
print(df)

#Writing to a new sheet in Excel file

df.to_excel("new.xlsx",sheet_name="stocks",startrow=1,startcol=2,index=False) #startrow and startcol will specify the rows and column shift


#creation of two dataFrames into an excel file using Excel Writer
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer,sheet_name="Stoks")
    df_weather.to_excel(writer,sheet_name="Weather")