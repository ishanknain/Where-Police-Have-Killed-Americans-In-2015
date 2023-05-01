import pandas as pd
import matplotlib.pyplot as plt
import csv
df = pd.read_csv('/Users/ishanknain/Desktop/Major Project/police_killings.csv',encoding='ISO-8859-1')

cause=df["cause"].value_counts().sort_index()
my_explode= [0, 0.1, 0 , 0, 0 ]
plt.pie(cause, labels=cause.index,wedgeprops={'edgecolor':'black' }, explode= my_explode, autopct='%1.1f%%')
plt.title('Total Police killings by race')
plt.show()