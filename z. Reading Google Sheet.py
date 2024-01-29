import pandas as pd 
gsheetId="1Tfsie3jgw-FrZC03vUB4a2jot8oJfHpR3ftF9jnYT2M"
sheet_name="Sheet1"

gsheet_Url="https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetId,sheet_name)
df=pd.read_csv(gsheet_Url)
print(df)
rows,column=df.shape
print(rows)