import pandas as pd 
df = pd.read_excel("stock_data.xlsx") #Note there was an extra row which needed modification
print(df)
print()
df=pd.read_excel("stock_data.xlsx",skiprows=1) #header=1 will also produce the same output
print(df)
