import pandas as pd

df = pd.read_csv('students.csv')
print(df)
mean = df[['Математика', 'Физика', 'Химия', 'Информатика', 'История']].mean(axis=1)
# mean = df.mean(axis=1,numeric_only=True)
mean = mean.round(2)
df['Средний'] = mean
df = df.sort_values('Средний', ascending=False)
print(df)

df.to_excel('1312.xlsx', index=False)

print(df.max(axis=0, numeric_only=True))
max_bal = df['Средний'].max()
sort_df = df[df['Средний'] == max_bal]
print(sort_df['Имя'])
min_bal = df['Средний'].min()
sort_df1 = df[df['Средний'] == min_bal]
print(sort_df1['Имя'])
