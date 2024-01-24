import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'co2_daily_mlo.csv'
df = pd.read_csv(file_path, header=None, names=['Year', 'Month', 'Day', 'Decimal Date', 'CO2'])

monthly_means = df.groupby(['Year', 'Month'])['CO2'].mean().reset_index()

monthly_means['Date'] = pd.to_datetime(monthly_means[['Year', 'Month']].assign(day=1))


x = np.arange(len(monthly_means))
y = monthly_means['CO2'].values
coefficients = np.polyfit(x, y, 1) # least square fit
trend = np.poly1d(coefficients)(x)


# plt.figure(figsize=(12, 6))
# plt.plot(monthly_means['Date'], y)
# plt.plot(monthly_means['Date'], trend, linestyle='--')
plt.title('Monthly Mean CO2 Concentration')
plt.xlabel('Date')
plt.ylabel('CO2')
plt.grid(True)
plt.tight_layout()
plt.savefig(f'./results/ex3a.pdf')

# plt.show()

# plt.plot(monthly_means['Date'], y - trend)
plt.savefig(f'./results/ex3b.pdf')

# plt.show()

import ex2



# c
x = monthly_means['Date'][-12:]
y -= trend # eliminam trend
y = y[-12:]



plt.figure()
plt.scatter(x, y, marker="o", label="Samples")
# x contains times info, y contains samples

kernel = ex2.kernels["periodic"]
cov = cov = np.array([[kernel(x, y) for x, y in zip(xi, yi)] for xi, yi in zip(ex2.X, ex2.Y)])
mean = np.full(ex2.SAMPLES,np.mean(y))

# what do here?

plt.show()

