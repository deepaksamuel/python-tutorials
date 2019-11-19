# reading file with pandas
# Pandas is a python module to read files and manipulate its contents (and also plot it)
# the read data is stored in what is called as a dataframe (like excel worksheet, which can be viewed in Spyder)
# This example shows how to read file which we wrote in the previous assignment (09-file-write)
# Pandas can also be used to write files.

import numpy as np 
import matplotlib.pyplot as plt

# You must also import pandas and if it is not installed use the anaconda navigator -> environments and search for pandas and install it
# You can also see detailed instructions to install in https://github.com/deepaksamuel/python-tutorials and see the README.md
import pandas as pd 

# We have no headers in the file, we name the columns as i and i-squared as shown below. The names will be used while plotting
df = pd.read_csv("out.txt",header=None, names=["i","i-squared"]) # the dataframe will be shown in Spyder IDE

print(df.head()) # this prints out the first 5 elements in the file

# you can also plot from a dataframe
df.plot(x="i",y="i-squared")
plt.show()

# if the file has NO header rows, you must state that explicitly
# more info at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

# if you want to have the full view of the dataframe, go to variable explorer in the Spyder IDE and click on the parameter df. 
# A separate window will open show the file in an Excel Sheet like view.