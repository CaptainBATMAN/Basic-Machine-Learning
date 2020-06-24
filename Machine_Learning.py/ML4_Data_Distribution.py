# Machine Learning - Data Distribution

# In the real world, the data sets are much bigger, but it can be difficult to gather real world data, 
# at least at an early stage of a project.

#How Can we Get Big Data Sets?
# To create big data sets for testing, we use the Python module NumPy, 
# which comes with a number of methods to create random data sets, of any size.
# or
# we can also obtain online data-sets using "WEB SCRAPPING"

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0, 5, 250)     #it gives 250 values bettween 0.0 to 5.0
print(x)

# Histogram
# To visualize the data set we can draw a histogram with the data we collected.

plt.hist(x,5)
plt.show()

# Note: The array values are random numbers and will not show the exact same result on your computer.

# Big Data Distributions
# An array containing 250 values is not considered very big, but now you know how to create a random set of values, and by changing the parameters, 
# you can create the data set as big as you want.

x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()