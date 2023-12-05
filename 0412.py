import numpy as np

'''
направления
прикладные ычисления - автоматизация, аналитика больших данных
серверное программирование(джанго)
работа с ИИ (нейросети и боты)
'''

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)

c = np.arange(0, 10)
print(c)
# массив 3*3 случайных значений от 0 до 1
d = np.random.rand(3, 3)
print(d)

z = np.zeros((3, 5))
print(z)

e = np.ones((3, 5))
print(e)
print('**************************************')
n1 = np.random.randint(1, 9, size=(3, 3))
n2 = np.random.randint(1, 9, size=(3, 3))
print(n1)
print(n2)
n3 = n1 + n2
print(n3)
# n3 *= -1
# print(n3)

maxN = np.max(n3)
minN = np.min(n3)
sumN = np.sum(n3)
averN = np.average(n3)
print(maxN,minN,sumN,averN)
