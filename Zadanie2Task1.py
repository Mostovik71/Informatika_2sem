
from scipy.stats import cumfreq
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
'''file= open("r1z1.csv")
reader=csv.reader(file)
rows=list(reader)#Получаем список списков
rows.remove(rows[0])#Удаляем элемент с инлдексом 0(Буква 'Х')
rows.sort()#Сортируем список
res = [''.join(ele) for ele in rows]#Преобразуем список списков в список строк
for i, item in enumerate(res):#
    res[i] = float(item)#Преобразуем список строк в список чисел
'''

df = pd.read_csv('r1z1.csv')
#dfsort=df.sort_values('X')
#list=[df]
#listsort=list.sort()
#pd.set_option('display.max_rows', 100)
plt.style.use('dark_background')
df.hist(grid=True,column='X',bins=[112,114,116,118,120,122,124,126,128])
plt.title('Гистограмма')
plt.xlim(112,128)
plt.show()
#print(df.X.mode())
#print(dfsort)

#print(df.describe())#количество значений, среднее,стандартное отклонение, минимум, квантили порядка 1/4,1/2(медиана),3/4, максимум



'''
file= open("r1z1.csv")
reader=csv.reader(file)
rows=list(reader)#Получаем список списков
rows.remove(rows[0])#Удаляем элемент с инлдексом 0(Буква 'Х')
rows.sort()#Сортируем список
res = [''.join(ele) for ele in rows]#Преобразуем список списков в список строк
for i, item in enumerate(res):#
    res[i] = float(item)#Преобразуем список строк в список чисел
part0, part1, part2, part3, part4, part5, part6= np.array_split(res, 7)

plt.figure(figsize=(5,5), dpi= 80)
plt.bar(part0,50)
plt.show()
'''


