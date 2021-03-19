#from collections import Counter

#import matplotlib
#import numpy as np
#from statsmodels.distributions.empirical_distribution import ECDF
#from plotnine import *
import csv  
import matplotlib.pyplot as plt
file= open("r1z1.csv")
reader=csv.reader(file)
rows=list(reader)#Получаем список списков
rows.remove(rows[0])#Удаляем элемент с инлдексом 0(Буква 'Х')
rows.sort()#Сортируем список
res = [''.join(ele) for ele in rows]#Преобразуем список списков в список строк
for i, item in enumerate(res):#
    res[i] = float(item)#Преобразуем список строк в список чисел


d = {x:res.count(x) for x in res}
a,b=d.keys(),d.values()
x=list(a)
y=list(b)
ynew=[]
sum=0

for i in y:
   k=i/len(res)
   sum+=k
   ynew.append(sum)

#ynew.insert(0,0)

ynew.insert(0,0)
ynew.append(1)
#x.insert(0,100)
x.append(130)
x.insert(0,113.2)

plt.style.use('dark_background')
#plt.plot(x,ynew)
plt.plot([110, 11.2], [0, 0],color='red')

#where_set = ['pre', 'post', 'mid']
'''
fig, axs = plt.subplots(1,3, figsize=(5, 5))
for i, ax in enumerate(axs):
  ax.step(x, ynew, "r-")#where=where_set[i])
  ax.grid()
'''
plt.step(x,ynew,color='red')
plt.xlim(112,130)
#plt.axis('off')
#plt.ylim(0,1)
plt.show()

#print(d)
#print(ynew)