import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2013, 2014, 2015, 2016, 2017, 2018])
company_p_profits = [25, 35, 45, 55, 50, 60]
company_q_profits = [20, 30, 40, 50, 60, 55]

# Bar width and positioning
bar_width = 0.35
index = np.arange(len(years))

# Plotting
fig, ax = plt.subplots()
bars1 = ax.bar(index, company_p_profits, bar_width, label='Company P', hatch='/', color='red', edgecolor='black')
bars2 = ax.bar(index + bar_width, company_q_profits, bar_width, label='Company Q', color='lightblue', edgecolor='black')

# Labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Profit percentage')
ax.set_title('Profit percentage of Company P and Company Q (2013-2018)')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(years)
ax.legend()

# Display the chart
plt.show()

