import matplotlib.pyplot as plt
import numpy as np
sr = 0.001 # sampling rate in seconds
t = np.arange(0,1,0.001)
print(t)
freq = 200.0 # in Hz
p = np.math.pi
y =np.sin(2.0*np.math.pi*freq*t)
#y = np.sin(2.0*np.math.pi*freq*t) + np.sin(np.math.pi*freq*t)

plt.plot(t,y)

sp = np.fft.fft(y)

freq = np.fft.fftfreq(t.shape[-1])/sr # this gives out the frequency values appropriately
print(freq)
print(len(freq))
plt.plot(t,y)
plt.show()

plt.scatter(freq, np.sqrt(sp.real**2+sp.imag**2))
plt.show()

#merged_arr = np.concatenate(freq,freq)
#print(merged_arr)
# In case you want to find the peaks in the spectrum to report the dominant frequencies automatically:
from scipy.signal import find_peaks
merged=np.c_[freq,np.sqrt(sp.real**2+sp.imag**2)] # this is how two np arrays are merged (the first column is freq, second is the amplitude)
# the above line is not really required but may be useful for other operations
nn = merged[:,1] # this is how you extract the second column of a multicolumn array. The comma separates the row selection from column r,c
peaks,_ = find_peaks(merged[:,1],threshold=10) # find peaks in the second column    

print("Peaks found at {0} Hz".format(freq[peaks]))
print(freq[peaks])