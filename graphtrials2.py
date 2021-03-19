import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
df = pd.read_csv('r1z1.csv')

#df.sort_values('X',ascending='True')
list=df['X'].tolist()
#list.sort()
plist=[]
for i in list:
    p=float(i)/len(df)
    plist.append(p)
df2=pd.DataFrame({'X':plist})

#df2.hist(grid=True,column='X',bins=[112,114,116,118,120,122,124,126,128])
#sns.distplot(df,bins=[112,114,116,118,120,122,124,126,128])
#plt.title('Гистограмма')
#plt.xlim(112,128)
#plt.ylim(1,2)
plt.show()
#print(df)
#print(df2)