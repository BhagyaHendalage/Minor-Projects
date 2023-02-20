'''
Author: Bhagya Hendalage
Date:22/01/2021
Input: temperature.csv
Output:do statistical analysis chi-square test
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import statsmodels.graphics.mosaicplot as mosaicplot
# Creating a Dataframe from the data and printing it
#fish = pd.DataFrame([[1,10,37],[49,35,9]],index=['eaten','not_eaten'],columns=['uninfected','light_infected','heavy_infected'])
#print(fish)

# initialise data of lists.
data = {'uninfected': [1, 49],'light_infected': [10, 35],'heavy_infected':[37,9]}
# Creates pandas DataFrame.
fish = pd.DataFrame(data, index=['eaten','not_eaten'])
# print the data
print(fish)
# plot a mosaicplot for the dataframe
mosaicplot.mosaic(fish.stack(),title='mosaic plot for the table')
plt.show()

# do a chi-square contingency test
chi_value,p,dof,expected = stats.chi2_contingency(fish)
print('Chi values :',chi_value)
print('P value :',p)
print('degree of freedom :',dof)
#use the expected variable from it make a dataframe
expected = pd.DataFrame(expected)
print(expected)
