#считывание с файла
import matplotlib.pyplot as plt
from math import *
import csv
file= open("rz.csv")
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
sumassim=0#Сумма случайных величин для коэффициента ассиметрии
summedian=0#Сумма значений с 41 по 51 элементы массива для медианы
summinimum=0#Сумма значений с 19 по 25 элементы списка
summaximum=0#Сумма значений с 65 по 71 элементы списка
kolmedian=0#Количество элементов с 41 по 51  для медианы
kolminimum=0#Количество элементов с 19 по 25
kolmaximum=0#Количество элементов с 65 по 71
resformed=res[40:52]#Элементы списка с 40 по 51 для медианы
resminimum=res[0:45]#Элементы левой половины массива(с 0 по 44)
resmaximum=res[46:90]#Элементы правой половины массива(с 46 по 90)
resmedmin=resminimum[19:26]#Элементы для медианы левой части списка
resmedmax=resmaximum[19:26]#Элементы для медианы правой части списка

maximum=max(res)#Получаем максимум из списка чисел
minimum=min(res)#Получаем минимум из списка чисел

razmah=maximum-minimum#Вычисляем размах (Разница между максимумом и минимумом)

for x in res:
   V+=1
   sum+=x
   sumsqr+=x*x


srednee=sum/len(res)


disp1=(sumsqr/len(res))-srednee*srednee#Выборочная дисперсия(Смещённая)
disp2=(len(res)/(len(res)-1))*disp1#Дисперсия поправленная на несмещённость
standotklon=sqrt(disp1)#Стандартное отклонение

for x in res:
    sumassim+=(x-srednee)**3

assim=(sumassim)/(len(res)*(standotklon**3))#Вычисление коэффициента ассиметрии
for x in resformed:

     summedian+=x
     kolmedian+=1
median=summedian/kolmedian

for x in resmedmin:
    summinimum+=x
    kolminimum+=1

for x in resmedmax:
    summaximum+=x
    kolmaximum+=1

medianminimum=summinimum/kolminimum#Медиана списка элементов с 0 по 44, т.е. квантиль порядка 1/4
medianmaximum=summaximum/kolmaximum#Медиана списка элементов с 46 по 90, т.е. квантиль порядка 3/4
shirota=medianmaximum-medianminimum
print(res)
print('Объём выборки: '+str(V))#Выводим объём выборки
print('Минимум: '+ str(minimum))#Выводим минимум выборки
print('Максимум: '+ str(maximum))#Выводим максимум выборки
print('Размах: '+ str(round(razmah,1)))#Выводим размах
print('Среднее: '+str(round(srednee,2)))#Выводим среднее
print('Дисперсия (Смещённая оценка): '+str(round(disp1,2)))#Выводим смещённую дисперсию
print('Дисперсия (Несмещённая оценка): '+str(round(disp2,2)))#Выводим несмещённую дисперсию
print('Стандартное отклонение: '+ str(round(standotklon,2)))#Выводим стандартное отклонение
print('Коэффициент ассиметрии: '+ str(assim))#Выводим коэффициент ассиметрии
print('Медиана: '+str(round(median,1)))#Выводим медиану
#print('Индекс минимума: '+str(res.index(113.2)))#Индекс минимума
#print('Индекс медианы: '+str(res.index(120.5)))#Индекс медианы
#print('Индекс максимума: '+str(res.index(127.0)))#индекс максимума
print('Интерквартильная широта: ' + str(shirota))
#fig=plt.figure()
#fig.set(facecolor='blue')
#plt.show()


