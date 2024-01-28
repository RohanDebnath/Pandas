import pandas as pd 
df=pd.read_excel('stocks_12.xlsx',header=[0,1])
print(df)

#Suppose you want the data to be as like Stack_12.png
print()
print(df.stack())
print(df.stack(level=0))
print( )
print(df.unstack())