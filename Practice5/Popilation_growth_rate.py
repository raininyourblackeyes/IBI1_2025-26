import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

# define the data
countries = ["UK", "China", "Italy", "Brazil", "USA"]
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]  # 2020年人口（百万）
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]  # 2024年人口（百万）

# calculate the percentage change of population
percent_changes = []
for i in range(len(countries)):
    change = (pop_2024[i] - pop_2020[i]) / pop_2020[i] * 100
    percent_changes.append(change)

# sort by percentage change in descending order
sorted_data = sorted(zip(countries, percent_changes), key=lambda x: x[1], reverse=True)

# output the percentage change
for country, change in sorted_data:
    print(f"{country}: {change:.2f}%")

# find the countries that have the largest percentage change and the smallest percentage change
largest_increase = sorted_data[0][0]
largest_decrease = sorted_data[-1][0]
print(f"\n: Countries with the largest population growth{largest_increase}")
print(f": Countries with the largest population decline{largest_decrease}")

# 4. create bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(countries, percent_changes)

# add title and labels
plt.title("Population Percentage Change (2020-2024)", fontsize=14, pad=20)
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")

# label each bar with a percentage value
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + (0.05 if height > 0 else -0.2),
            f'{height:.2f}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=10)
plt.ylim(-2, 4.5) 
plt.axhline(y=0, color='black', linewidth=0.8)
# show the chart
plt.tight_layout()
plt.show()