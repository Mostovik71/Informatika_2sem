import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import stats
sumx=0
sumxsqr=0
sumy=0
sumysqr=0
sumkorel=0
r=0
n=108
newx=[]
newy=[]
df = pd.read_csv('r4z2.csv')
pd.set_option('display.max_rows', None)
dfx=df['X'].tolist()
dfy=df['Y'].tolist()
for x in dfx:
   sumx+=x
   sumxsqr+=x*x
for y in dfy:
    sumy += y
    sumysqr += y * y


sredneex=sumx/len(dfx)
sredneey=sumy/len(dfy)
dispx=(sumxsqr/len(dfx))-sredneex*sredneex#Выборочная дисперсия(Смещённая)
dispy=(sumysqr/len(dfy))-sredneey*sredneey#Выборочная дисперсия(Смещённая)
standartotklx=sqrt(dispx)
standartotkly=sqrt(dispy)

for x,y in zip(dfx,dfy):
    sumkorel+=(x-sredneex)*(y-sredneey)
r=(sumkorel/n)/(standartotklx*standartotkly)
#print(r)

for x in dfx:#для регрессии y на x
 y=sredneey + r*(standartotkly/standartotklx)*(x-sredneex)
 newy.append(y)
#plt.xlim()


'''
for y in dfy:#для регрессии x на y
    x = sredneex + r * (standartotklx / standartotkly) * (y - sredneey)
    newx.append(x)
'''
#plt.plot(newx,dfy)
plt.scatter(dfx,dfy)
x1=107
x2=129

y1=sredneey + r*(standartotkly/standartotklx)*(x1-sredneex)
y2=sredneey + r*(standartotkly/standartotklx)*(x2-sredneex)
newy.append(y1)
newy.append(y2)
dfx.append(x1)
dfx.append(x2)
plt.plot(dfx,newy)

#print(y1)
plt.xlim(108.2,128.9)
plt.show()



#df1=pd.DataFrame({'X':dfx,'Y':dfy})
#print(df1)