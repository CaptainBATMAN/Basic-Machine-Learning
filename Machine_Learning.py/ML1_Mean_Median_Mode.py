# In Machine Learning (and in mathematics) there are often three values that interests us:
# Mean - The average value                  --Has method mean() in numpy module.
# Median - The mid point value              --Has method median() in numpy module.
# Mode - The most common value              --Has method mode() in stats sub-module of scipy module.

import numpy as np
from scipy import stats

# Mean
# The mean value is the average value.
# To calculate the mean, find the sum of all values, and divide the sum by the number of values

x=input("Enter array elements(in \",\" format) :").split(",")
a=[]
for i in x:
    a.append(int(i))
ar=np.array(a)
print(ar)
print("Mean of the given array : ",ar," is ",np.mean(ar))

# Median
# The median value is the value in the middle, after you have sorted all the values
# It is important that the numbers are sorted before you can find the median.
# If there are two numbers in the middle, divide the sum of those numbers by two.

print("Median of the given array : ",ar," is ",np.median(ar))

# Mode
# The Mode value is the value that appears the most number of times.
print("Mode of the given array : ",ar," is ",stats.mode(ar))