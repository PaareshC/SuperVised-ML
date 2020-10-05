#Set working directory
import os
os.chdir("E:\Linear Regression")
# Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
# Creating a dataframe
df=pd.read_csv("House_Price.csv",header=0)
# To view first 5 rows
df.head()
# To view shape of df
df.shape
