# TASK 2: Unemployment Analysis with Python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Unemployment in India.csv")

print(data.head())

data.columns = ['State', 'Date', 'Frequency',
                'Estimated Unemployment Rate',
                'Estimated Employed',
                'Estimated Labour Participation Rate',
                'Region']

data['Date'] = pd.to_datetime(data['Date'])

plt.figure()
plt.plot(data['Date'], data['Estimated Unemployment Rate'])
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.title("Unemployment Rate Over Time in India")
plt.show()

covid_data = data[data['Date'].dt.year == 2020]

print("Average Unemployment Rate in 2020:",
      covid_data['Estimated Unemployment Rate'].mean())
