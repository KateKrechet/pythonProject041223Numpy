import numpy as np
import pandas as pd

years = np.random.randint(2010, 2024, size=(100000, 1))
print(years)
print(len(years))
sales = np.random.randint(500, 1500, size=(100000, 1))
viruchka = np.random.randint(50000, 150000, size=(100000, 1))
print('слеили 3 массива')
data = np.concatenate((years, sales, viruchka), axis=1)
print(data)

# newdata = data[data[:,0]==2018]
# sum18sales = np.sum(newdata[:,1])
# sum18vir = np.sum(newdata[:,2])

df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.index)
df2 = df.groupby(0).sum()
print(df2)
print(df2.columns)
print(df2.index)
print('максимум продаж')
print(df2[1].max())
print('максимум выручки')
print(df2[2].max())
print('год максимума продаж')
print(df2.idxmax(axis="index")[1])
print('год максимумальной выручки')
print(df2.idxmax(axis="index")[2])
