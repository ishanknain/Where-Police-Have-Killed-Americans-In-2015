import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('/Users/ishanknain/Desktop/Major Project/police_killings.csv', encoding='ISO-8859-1')
no_of_killings= df["state"].value_counts().sort_index()

plt.bar(no_of_killings.index,no_of_killings)
plt.title('Total number of killings in each state')
plt.xlabel('State')
plt.ylabel('no of killings')
plt.show()