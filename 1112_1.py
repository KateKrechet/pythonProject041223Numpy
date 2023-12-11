import numpy as np

arr = np.random.randint(1, 100, size=(4, 4))
print(arr)
a=np.mean(arr, axis=0)
b=np.mean(arr, axis=1)
print(a)#среднее стобцов
print(b.reshape(4,1))#среднее строк
