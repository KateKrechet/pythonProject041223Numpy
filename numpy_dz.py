import numpy as np
import pandas as pd

products = np.array([
[1000, 1200, 1500, 1350, 1400, 1300, 1250, 1450, 1300, 1550, 1600, 1700], # Завод 1
    [800, 900, 1000, 950, 1000, 1100, 1200, 1150, 1000, 1100, 1200, 1300], # Завод 2
    [1200, 1300, 1250, 1400, 1500, 1600, 1650, 1700, 1600, 1550, 1500, 1400], # Завод 3
    [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]]) #Завод 4
print(products)
factories = np.array(['Завод 1', 'Завод 2', 'Завод 3', 'Завод 4'])
months = np.array(['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август','сентябрь', 'октябрь', 'ноябрь', 'декабрь'])
# Общее количество выпущенных велосипедов
volume = np.sum(products)
print('Общее количество выпущенных велосипедов:',volume)
# Количество велосипедов, произведенных на каждом заводе за год.
sum_year = np.sum(products,axis=1)
data = {'factory':factories,'sum_velo':sum_year}
df1 = pd.DataFrame(data)
print('Количество велосипедов, произведенных на каждом заводе за год')
print(df1)
# Самый продуктивный завод компании
max_volume = np.argmax(sum_year)
print('Самый продуктивный завод компании')
print(factories[max_volume],':',sum_year[max_volume])
# Самый продуктивный месяц компании
sum_month = np.sum(products,axis=0)
max_month = np.argmax(sum_month)
print('Самый продуктивный месяц компании')
print(months[max_month],':',sum_month[max_month])