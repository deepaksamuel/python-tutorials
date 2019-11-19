# plotting is one important aspect is any analysis
# python has a very wide selection of plotting modules
# in our tutorials we will use the matplotlib module which is sufficient for a beginner

# as usual import numpy since we will require it
import numpy as np 
# next we will import another important library from plotting
import matplotlib.pyplot as plt 

# we are going to see how our random number distributions look like (refer tutorial 04-random-number-generatiion)
# generate a series of 1000 random numbers from a gaussian distribution with mean 0, sigma 1 
ran = np.random.normal(0,1,1000) #(mean, sigma, number of samples)
print(ran)
# this is how you plot a histogram
plt.hist(ran, bins=1000)
# you need to show it using the following command (not required in Spyder)
plt.show()

# Assignment
# How do you change the binning of the histogram
# Using the bins argument: 
# plt.hist(ran, bins=1000) 
# Try this.

# How do you change the axis labels and titles?
# plt.xlabel("Random")
# plt.ylabel("Freq")
# plt.title("Gaussian distribution")
# Try this

# How do you change the axis to log scale?
# plt.yscale('log')
# plt.xscale("log")
# Try this








