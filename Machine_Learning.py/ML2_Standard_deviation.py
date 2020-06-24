# What is Standard Deviation?

# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.

# The NumPy module has a method to calculate the standard deviation

import numpy as np

x=input("Enter array elements(in \",\" format) :").split(",")
a=[]
for i in x:
    a.append(int(i))
ar=np.array(a)
print(ar)
print("Standard_Deviation of the given array : ",ar," is ",np.std(ar))

# Variance
# Variance is another number that indicates how spread out the values are.
# In fact, if you take the square root of the variance, you get the standard deviation!
# Or the other way around, if you multiply the standard deviation by itself, you get the variance!

# To calculate the variance you have to do as follows:

# 1. Find the mean
# 2. For each value: find the difference from the mean
# 3. For each difference: find the square value
# 4. The variance is the average number of these squared differences

# Luckily, NumPy has a method to calculate the variance

print("Variance of the given array : ",ar," is ",np.var(ar))