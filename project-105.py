import math
import csv

with open('data.csv.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

    total_marks = 0
    total_entries = len(file_data)

    for marks in file_data:
        total_marks += float(marks[1])

def mean(data):
    n= len(data)
    total =0
    for marks in file_data:
        total_marks += float(marks[1])


    mean = total_marks / n
    return mean 

    squared_list= []
    for number in data :
        a = int(number) = mean(data)
        a= a**2
        squared_list.append(a)

        sum =0
        for i in squared_list:
            sum =sum + i

        result = sum/ (len(data)-1)

        std_deviation = math.sqrt(result)
        print(std_deviation)

