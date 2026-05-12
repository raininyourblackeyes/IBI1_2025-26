import matplotlib.pyplot as plt
import numpy as np

#create a list of the heart rates and calculate the average.
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64] #create a list
ave_hr = sum(heart_rates)/len(heart_rates) #calculate average
print(f"\nThere are {len(heart_rates)} pieces of heart rate data.")
print(f"\nThe average heart rate is: {ave_hr} beats per minute.")

# find the number of each category and compare
low = [] #create lists for three categories
normal = []
high = []
for hr in heart_rates: #sort the data
    if hr < 60:
        low.append(hr)
    elif 60 <= hr <= 100:
        normal.append(hr)
    else:
        high.append(hr)
print(f"\nNumber of patients in each category:") #print the number of the heart rate data of each category
print(f"- Low (<60 bpm): {len(low)}")
print(f"- Normal (60-120 bpm): {len(normal)}")
print(f"- High (>120 bpm): {len(high)}")

#find the category which has the largest number of pieces of heart rate data.
category_counts = {"low": len(low), "normal": len(normal), "high": len(high)}
largest_category = max(category_counts, key=category_counts.get)
print(f"\nThe {largest_category} heart rate category contains the largest number of patients.")

# create pie chart which reports the number of patients in each heart rate category.
labels = 'low', 'normal', 'high'
numbers = [len(low), len(normal), len(high)]
plt.pie(numbers, labels=labels, autopct='%1.0f%%') #create the pie chart
plt.title('Heart Rate Categories') 
plt.tight_layout()
plt.show()