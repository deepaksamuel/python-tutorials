# Technique 2:  This can be used for fitting a gaussian when your data is not from a histogram but from a profile (i.e y axis is not counts but some parameter)
# We will use optimize module from scipy
# infact this technique can be used for fitting to any arbitary function

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaus(x,a,mu,sd):
    return a*np.exp(-(x-mu)**2/(2*sd**2))

x = np.arange(-3,3,0.1)
y = gaus(x,10,0,1) # mean zero and sd 1, with amplitude 10


# popt is an array of parameters and pcov is the matrix of covarianes
popt,pcov = curve_fit(gaus,x,y,p0=[1,1,1]) # the number within square brackets are the initial values.

plt.plot(x,y,'b+:',label='data')
plt.plot(x,gaus(x,*popt),'ro:',label='fit')
plt.legend()
plt.show()

# assignment
# generate a data set containing numbers from an exponential decay function
# write a function to fit the dataset to an exponential decay and find the fit parameters