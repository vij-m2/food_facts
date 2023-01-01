#!\python310\python
import csv

def read_fact_file(filename: str):
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


read_fact_file("C:\\Users\\VMARAM\\Downloads\\MyFoodData.csv")