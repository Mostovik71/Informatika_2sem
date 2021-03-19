import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('r4z1.csv')
dfx=df['X'].tolist()
dfy=df['Y'].tolist()
dfx.sort()
dfy.sort()
df.hist(grid=True,column='X',bins=[117.05,119.05,121.05,123.05,125.05])
pd.set_option('display.max_rows', None)


n=108
n1=7
n2=19
n3=20
stat=((n*n1-n2*n3)**2)/(n*n2*n3)
print(stat)

T=0
'''
for i in dfx:
    if i<117.05:
     kolx1+=1
    if 117.05<=i<119.05:
     kolx2+=1
    if 119.05<=i<121.05:
     kolx3+=1
    if 121.05<=i<123.05:
     kolx4+=1
    if  123.05<=i<125.05:
     kolx5 += 1
    if 125.05<=i:
     kolx6+=1

for i in dfy:
    if i<80.05:
     koly1+=1
    if 80.05<=i<81.55:
     koly2+=1
    if 81.55<=i<83.05:
     koly3+=1
    if 83.05<=i<84.55:
     koly4+=1
    if  84.55<=i<86.05:
     koly5 += 1
    if 86.05<=i:
     koly6+=1
   '''
#1 строка таблицы















#dict1=dict(zip(dfx,dfy))
#df1=pd.DataFrame({'X':dfx,'Y':dfy})
#print(df.sort_values("X"))
#plt.xlim(100,130)
#print(kol1,kol2,kol3,kol4,kol5,kol6)
#print(len(dfy))
#plt.show()
#print(dfx)
#print(dfy)
