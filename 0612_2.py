import numpy as np
import pandas as pd

virushka = np.array([[1000000, 2000000, 2500000, 3000000, 2150000],
                     [1560000, 2330000, 2500000, 3990000, 2150000],
                     [2120000, 2500000, 3770000, 2650000, 4000000],
                     [2589000, 2990000, 4488000, 4586000, 3500000],
                     [2100000, 2599000, 3100000, 2110000, 4233000],
                     [1533000, 2660000, 4220000, 3500000, 2577000]])
cities = np.array(['Нижний Новгород', 'Астрахань', 'Самара', 'Москва', 'Воронеж', 'Санкт-Петербург'])
datas = np.array(['10.07.23', '11.07.23', '12.07.23', '13.07.23', '14.07.23'])
sumstr = np.sum(virushka, axis=1)  # сумма продаж по городам
sumstr = sumstr.reshape(6, 1)  # развернули строку вертикально
# argmax - index max value
maxcity = np.argmax(sumstr)
print(sumstr)
print(maxcity)
print(cities[maxcity])

sumcol = np.sum(virushka, axis=0)
sumcol = sumcol.reshape(5, 1)
# argmax - index max value
maxday = np.argmax(sumcol)
print(sumcol)
print(maxday)
print(datas[maxday])

# Транспонирование
newT = virushka.T
print(newT)

# средние по каждому городу и по каждому числу
srstr = np.sum(virushka, axis=1)  # среднее продаж по городам
# srstr = srstr.reshape(6,1)#развернули строку вертикально
print(srstr)
data = {'cities': cities, 'srstr': srstr}
df = pd.DataFrame(data)
print(df)

srdata = np.sum(virushka, axis=0)
data = {'data': datas, 'srdata': srdata}
df1 = pd.DataFrame(data)
print(df1)
