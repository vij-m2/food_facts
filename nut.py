#!\python310\python
import csv
import matplotlib.pyplot as plt

def read_fact_file(filename: str):
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           ascii_row = {}
           for k, v in row.items():
               ascii_k = k.encode('ascii', 'ignore').decode('utf-8')
               # print(f"k: {ascii_k}, v: {v}")
               ascii_row[ascii_k] = row[k]
           yield ascii_row



food_item = input("Enter food item: ")
labels = []
values = []
explode = []
fig1, ax1 = plt.subplots()
for item in read_fact_file("C:\\Users\\VMARAM\\Downloads\\MyFoodData.csv"):
    if item['name'].lower().find(food_item.lower()) != -1:
        for k, v in item.items():
            print(f"{k}: {v}")
            if k in ['name', 'Food Group'] or v == 'NULL':
                ax1.set_title(item['name'])
                continue

            labels.append(k)
            values.append(v)
            explode.append(0)
        break


ax1.legend()
ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()


# print(f"{food_item}: No such food found")

"""
calorie_input = float(input("Enter the calorie value: "))
for item in read_fact_file("C:\\Users\\VMARAM\\Downloads\\MyFoodData.csv"):
    if float(item['Calories']) <= calorie_input:
        print(f"name: {item['name']}, calories: {item['Calories']} food group: {item['Food Group']}")
"""

