# In this tutorial you will learn how to fit a gaussian to your histograms or similar profiles
# We will do it using two different methods, the second method (in the next tutorial) is universal in the sense that you can use it for fitting to custom functions

import numpy as np 
import matplotlib.pyplot as plt 

from scipy.stats import norm

# first let us generate a histogram by sampling points from a gaussian distribution

x = np.random.normal(0,1,1000) # gauss with 0 mean and sd 1, 1000 samples

mean,std=norm.fit(x) 
print("The mean and standard deviation of the fitted gaussian are:{0} and {1}".format(mean,std))

plt.hist(x,bins=50,normed=True)

# now we will see how the fitted gaussian looks like
xx = np.arange(-3,3,0.1)
y = norm.pdf(xx, mean, std)
plt.plot(xx, y)
plt.show()

# assignment
# see what happens if you change the mean and standard deviation of the distribution and check if the fitted values match with it
# change the nummber of samples from 1000 to 100 and 10000 and see the effect of the fitted values in mean and sd