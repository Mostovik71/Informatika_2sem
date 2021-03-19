import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
df = pd.read_csv('r2z2.csv')
#df.sort_values('X',ascending='True')
list=df['X'].tolist()
list.sort()
#plist=[]
kol1=0
kol2=0
kol3=0
kol4=0
kol5=0
kol6=0
kol7=0
kol8=0
kol9=0
kol10=0
kol11=0
n=len(list)
for i in list:
    if -2<=i<-1.5:
     kol1+=1
    if -1.5<=i<-1:
     kol2+=1
    if -1<=i<-0.5:
     kol3+=1
    if -0.5<=i<0:
     kol4+=1
    if  0<=i<0.5:
     kol5 += 1
    if 0.5<=i<1:
     kol6+=1
    if 1<=i<1.5:
     kol7+=1
    if 1.5<=i<2:
     kol8+=1
    if 2<=i<2.5:
     kol9+=1
    if 2.5<=i<3:
     kol10+=1

srednee=sum(list)/len(list)
print(round(kol1/n,3),round(kol2/n,3),round(kol3/n,3),round(kol4/n,3),round(kol5/n,3),round(kol6/n,3),round(kol7/n,3),round(kol8/n,3),round(kol9/n,3),round(kol10/n,3))
plt.style.use('dark_background')
sns.distplot(df,bins=[-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
x_axis = np.arange(-4, 4, 0.001)
# Среднее значение = 0, стандартное отклонение = 1.
plt.plot(x_axis, norm.pdf(x_axis,0,1))
plt.title('Гистограмма')
plt.xlim(-2.5,3.5)
#plt.ylim(1,2)
plt.xticks([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.show()
#print(df)
#print(srednee)
#print(kol1,kol2,kol3,kol4,kol5,kol6,kol7,kol8,kol9,kol10)