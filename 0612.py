import numpy as np

a = [1,2,3,4,5]
arr=np.array(a)
arr = np.arange(1,26).reshape(5,5)
print(arr)
print(arr.shape)#ajhvf 5*5
print(arr.size)#размер массива как длина
print(arr.ndim)#измерение
print(arr.dtype)


arr = np.random.randint(10,99,size=(2,6))
print(arr)
# меняем форму
arr = arr.reshape(4,3)
print(arr)

arr2 = np.resize(arr,new_shape=(2,2))
print(arr2)

arr3 = np.resize(arr,new_shape=(12,12))
print(arr3)
# диапазон, который делится на 9 частей
arr = np.linspace(0,5,num=9)
print(arr)

arr = np.arange(1,10).reshape(3,3)
print(arr)
print(arr*2)
print(arr<4)
newarr = arr[arr<4]
print(newarr)
newarr = arr[(arr<8)&(arr%2==0)]
print(newarr)
newarr = arr[(arr<8)|(arr%2==0)]
print(newarr)

print(arr)
# вырезать 6 - идем вниз-1, вправо-2
print(arr[1,2])
# вырезать с 1 строчки
print(arr[1:])
# берем все строки, но 2 столбец
print(arr[:,2])
# вырезаем квадрат
print(arr[1:,0:2])

print(np.mean(arr,axis=0))
arr =np.delete(arr,1,axis=0)
print(arr)
arr = np.insert(arr,1,values=[0,0,0],axis=0)
print(arr)
# np.info(np.random)

# task
arr = np.random.randint(1,1000,size=(5,10))
print(arr)
arr2 = np.resize(arr,new_shape=(10,5))
print(arr2)
maxN = np.max(arr2)
minN = np.min(arr2)
averN = np.average(arr2)
print(maxN,minN,averN)
print(np.max(arr2,axis=1))
print(np.min(arr2,axis=1))
print(np.mean(arr2,axis=1))


