import pandas as pd
import os
import matplotlib.pyplot as plt

l1=[]
l2=[]
arr = os.listdir('data1')
for i in arr:
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df=pd.read_csv("data1"+"/"+ i)
    l1.append(i)
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df1=df.groupby('year').last()
    df1['Return'] = ((df1['Open'].iloc[-1]/df1['Open'])*50000)
    j = df1['Return'].sum()
    l2.append(j)
d1=pd.DataFrame({"Investment":l1, "Return":l2})
plt.barh(d1['Investment'],d1['Return'])
plt.show()