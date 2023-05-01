import pandas as pd
import matplotlib.pyplot as plt
import csv
df = pd.read_csv('/Users/ishanknain/Desktop/Major Project/police_killings.csv',encoding='ISO-8859-1')
kill_in_each_year=df["month"].value_counts().sort_index()
plt.bar(kill_in_each_year.index,kill_in_each_year.values)
plt.title('Total Police killings by months')
plt.xlabel('months')
plt.ylabel('no of killings')
plt.show()