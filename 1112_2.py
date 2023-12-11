import numpy as np
import pandas as pd

arr=np.genfromtxt('litecoin.csv',delimiter=',',skip_header=1,usecols=(1,4))
print(arr)
maxs = np.max(arr,axis=0)
print(maxs)
print('позиции максимумов')
numbers = np.argmax(arr,axis=0)
print(numbers)

data = pd.read_csv('litecoin.csv')
print(data)
print(data.describe())
datas = data['Date']
print(datas)
print('даты максимумов')
print(datas[numbers[0]],datas[numbers[1]])