import pandas as pd
import numpy as np

data = {'Name': ['Boris', 'Max', 'Tomas', 'Robert'], 'Age': [25, 35, 45, 55], 'City': ['Ny', 'LA', 'SPB', 'Sochi'], }
df = pd.DataFrame(data)
# df = df.rename(columns={'Name':'A','Age':'B','City':'C'})
df.columns = ['A', 'B', 'C']
df.index = ['a', 'b', 'c', 'd']
print(df)
# вытащить данные про Boris
print(df.loc['a', 'A'])  # по названию колонок
print(df.iloc[0, 0])  # по индексам
print(df['A']['a'])
# вытащить всю строку Boris
print(df.loc['a'])
# способы вытащить столбец
print(df['A'])
print(df.loc[:, 'A'])

arr = np.random.randint(10, 99, size=(4, 4))
arrdf = pd.DataFrame(arr)
arrdf.columns = ['A', 'B', 'C', 'D']
print(arrdf)

df_file = pd.read_csv('data.csv')
print(df_file)
df2 = df_file.sort_values(by='столбец_2')
print(df2)
df3 = df_file.sort_values(by='столбец_3')
print(df3)
df4 = df_file.drop(['столбец_1'], axis=1)
print(df4)

data = {'Name': ['Igor', 'Anna', 'Igor', 'Anna', 'Zahar'], 'Money': [120, 130, 140, 150, 160]}
df5 = pd.DataFrame(data)
df6 = df5.groupby(by='Name').sum()
print(df5)
print(df6)

# task1
data = {'Name': ['Kate', 'Olga', 'Max', 'Zahar', 'Polina', 'Oleg', 'Gena', 'Anna', 'Ruben', 'Alla'],
        'Height': [165, 170, 180, 185, 150, 190, 190, 155, 195, 175],
        'Weight': [54, 60, 80, 85, 50, 90, 100, 55, 95, 75]}
df7 = pd.DataFrame(data).sort_values(by='Height').reset_index()
print(df7)
for i in df7.index:
    if i==1 or i==3 or i==5:
        print(df7.loc[i])


