import csv
file= open("r3z1.csv")
reader=csv.reader(file)
rows=list(reader)#Получаем список списков
rows.remove(rows[0])
res = [''.join(ele) for ele in rows]#Преобразуем список списков в список строк
for i, item in enumerate(res):#
    res[i] = float(item)#Преобразуем список строк в список чисел
print(len(res))