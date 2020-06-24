# Machine Learning - Normal Data Distribution

# Normal Data Distribution
# In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.
# In this chapter we will learn how to create an array where the values are concentrated around a given value.
# In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution,
# after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.

import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(5.0,1.0,100000)
plt.hist(x,100)
plt.show()

# the mean value is 5.0, and the standard deviation is 1.0.
# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.

# Note: A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.