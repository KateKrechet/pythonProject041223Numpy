import pandas as pd

data = pd.read_csv('sales_data.csv')
df = data.Количество
print(df.to_list())
# ser=pd.Series(df.to_list(),index=pd.date_range(start='2019-01-01', periods=len(df.to_list()),freq='D'))
ser = pd.Series(df.values, index=pd.date_range(start='2019-01-01', periods=len(df.values), freq='D'))
print(ser)
