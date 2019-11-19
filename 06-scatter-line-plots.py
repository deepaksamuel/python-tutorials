import numpy as np 
import matplotlib.pyplot as plt 

# We are now going to plot a sine wave

# we will first generate a series of numbers from 0 t0 100 with a step size of 1
# if you do not know how to do that, go to 03-number-series.py and see how it is done

x = np.arange(0,100,0.1)

# we now find the sin of all the numbers in x, that is done in a single statment below. No loops required !!!
y = np.sin(x)

# Now we have a set of 100 numbers in sequence and their corresponding sine value. Lets plot

plt.plot(x,y)
plt.show() # comment this line in Spyder

# Assignment:
#  change the step size in z to 0.1 and see what happens
#  plot also the cosine of the numbers
#  change the x-axis title to X and y-axis title to "Sin(x)" and the title of the plot to Plot of sin(x)