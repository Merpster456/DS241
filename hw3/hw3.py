import numpy as np
from statistics import *
import csv
from matplotlib import pyplot as plt
"""
Homework 3
By Ryan Quirk <quirkrf@clarkson.edu>
"""

# 1.
ds = [5,7,8,5,10,12,7,6]

mean = sum(ds)/len(ds)
print(mean)

print(variance(ds))


# 2. Correlation

X1 = np.array([1,2,3,4,5])
Y1 = np.array([2,4,6,8,10])
print(np.corrcoef(X1, Y1))

X2 = np.array([1,2,3,4,5])
Y2 = np.array([7,1,4,2,5])
print(np.corrcoef(X2, Y2))

X3 = np.array([-2,-1,0,1,2])
Y3 = np.array([2,1,0,1,2])
print(np.corrcoef(X3,Y3))

# Solution doesn't exist
X4 = np.array([])
Y4 = np.array([])
#print(np.corrcoef(X4,Y4))

# 3. Correlation and Causation

rows = []
with open("test-score.csv", 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)

    for row in reader:
        rows.append(row)

hours = []
grades = []

for row in rows:
    hours.append(int(row[0]))
    grades.append(int(row[1]))

hours = np.array(hours)
grades = np.array(grades)

print(np.corrcoef(hours, grades))
# Coeffecient is 0.98, VERY STRONG CORRELATION

plt.scatter(hours, grades)
plt.plot(hours,grades, '--')
plt.title("Average Grade per Hours Studied")
plt.show()