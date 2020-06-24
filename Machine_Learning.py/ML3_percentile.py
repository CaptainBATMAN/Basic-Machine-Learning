# What are Percentiles?
# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
# The NumPy module has a method for finding the specified percentile
import numpy as np
x=input("Enter array elements(in \",\" format) :").split(",")
a=[]
for i in x:
    a.append(int(i))
ar=np.array(a)
y=int(input("Enter Number to check percentile:"))
print(ar)
per=np.percentile(ar,y)
print(per)