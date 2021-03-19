from math import *
from scipy.stats import ttest_rel
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
#Гипотеза H0: Мат ожидание разности равно 0
#Альтернатива: мат ожидание меньше нуля
sum=0
sumsqr=0
m0=0
df = pd.read_csv('r2z1.csv')
diff=df['Y']-df['X']
listdiffx=df['X'].tolist()
listdiffy=df['Y'].tolist()
listdiff=diff.tolist()
listsort=listdiff.sort()
for i in listdiff:
    sum+=i
    sumsqr += i * i
    round(i,2)
#srednee=sum/len(listdiff)
#disp=(sumsqr/len(listdiff))-srednee*srednee
#standarotkl=sqrt(disp)
#T=((srednee-m0)/standarotkl)*sqrt(len(listdiff)-1)
#print(round(standarotkl,2))
print(diff)
#res=stats.shapiro(np.log10(df['X']))
#print(res)
plt.style.use('dark_background')
sns.distplot(diff)
plt.title('Гистограмма')
#plt.xlim(-100,100)
plt.show()

