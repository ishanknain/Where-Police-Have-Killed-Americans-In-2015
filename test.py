import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas dataframe
df = pd.read_csv('police_killings.csv', encoding='ISO-8859-1')

# # Convert the 'date' column to datetime format and extract the year
# df['year'] = pd.to_datetime(df['date']).dt.year

# Group the dataframe by year and count the number of rows in each group
yearly_counts = df.groupby('year').size()

# Create a bar chart of the yearly counts
plt.bar(yearly_counts.index, yearly_counts.values)
plt.title('Total Police Killings by Year')
plt.xlabel('Year')
plt.ylabel('Number of Killings')
plt.show()

# Create a line chart of the yearly counts
plt.plot(yearly_counts.index, yearly_counts.values)
plt.title('Total Police Killings by Year')
plt.xlabel('Year')
plt.ylabel('Number of Killings')
plt.show()
