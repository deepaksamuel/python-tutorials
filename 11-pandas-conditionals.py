# in this tutorials, we will see how to use pandas to select a particular set of rows that pass a condition

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# We have no headers in the file, we name the columns as i and i-squared as shown below. The names will be used while plotting
df = pd.read_csv("out.txt",header=None, names=["i","i-squared"]) # the dataframe will be shown in Spyder IDE

df1 = df[df["i"]<50] # this selects only the rows where i is < 50 and stores it in df1 

# you can also plot from a dataframe
df1.plot(x="i",y="i-squared") # plot df1
plt.show()

# if the file has NO header rows, you must state that explicitly
# more info at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

