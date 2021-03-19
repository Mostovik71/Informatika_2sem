from math import *
import csv
file= open("r3z2.csv")
reader=csv.reader(file)
rows=list(reader)#Получаем список списков
rows.remove(rows[0])#Удаляем элемент с инлдексом 0(Буква 'Х')
rows.sort()#Сортируем список
res = [''.join(ele) for ele in rows]#Преобразуем список списков в список строк
for i, item in enumerate(res):#
    res[i] = float(item)#Преобразуем список строк в список чисел



V=0#Объём выборки
sum=0#Сумма элементов выборки
sumsqr=0#Сумма квадратов элементов выборки



for x in res:
   V+=1
   sum+=x
   sumsqr+=x*x


srednee=sum/len(res)


disp1=(sumsqr/len(res))-srednee*srednee#Выборочная дисперсия(Смещённая)
disp2=(len(res)/(len(res)-1))*disp1#Дисперсия поправленная на несмещённость
standotklon=sqrt(disp1)#Стандартное отклонение
print(standotklon)