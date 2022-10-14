import matplotlib.pyplot as plt
import numpy
import csv

x = []
y = []

with open("./rando/grain.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(row)

plt.bar(x,y,color='g', width=.72, label = "Age")
plt.xlabel('Country')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()