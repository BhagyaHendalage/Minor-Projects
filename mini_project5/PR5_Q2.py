'''
Author: Bhagya Hendalage
Date:21/01/2021
Input: temperature.csv
Output:do statistical analysis two sample t-test(Kruskal-Wallis H Test)
'''
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
#read the datafile
lizards = pd.read_csv('HornedLizards.csv')
#print(lizards)
lizards['Squamosal horn length'].replace('', np.nan, inplace=True)
#print(lizards)
lizards.dropna(subset=['Squamosal horn length'], inplace=True)
#print(lizards)

# Printing descriptive statistics
print(lizards.describe())
#print(lizards.rename(columns={'Squamosal horn length':'length'}))
#to get rid from spaces of the colomn header
lizards=lizards.rename(columns={'Squamosal horn length':'length'})

servived = lizards.loc[lizards['Survive'] == "survived"]
servived_data=servived['length']
print(servived_data)

dead = lizards.loc[lizards['Survive'] == "dead"]
dead_data=dead['length']
print(dead_data)
# QQ plot for servived
qqplot(servived_data, line='s')
plt.title('QQplot for servived lizards')
plt.show()
# QQ plot for dead
qqplot(dead_data, line='s')
plt.title('QQplot for dead lizards')
plt.show()

# two histograms on one plot
plt.hist([servived_data, dead_data], label=['servived', 'dead'])
plt.title('Histogram of servived and dead lizards')
plt.legend(loc='upper left')
plt.show()

#Shapiro for servived
stat, p = stats.shapiro(servived_data)
print('P value for servived:',p)

#Shapiro for dead
stat, p = stats.shapiro(dead_data)
print('P value for dead:',p)

# draw boxplots for two samples
fig,ax =plt.subplots(1,2, figsize=(12,3))
ax[0].boxplot(servived_data)
ax[0].set_title("Boxplot of survived lizards horn length")
ax[1].boxplot(dead_data)
ax[1].set_title("Boxplot of dead lizards horn length")
plt.show()

# draw violin plots for two samples
fig,ax =plt.subplots(1,2, figsize=(12,3))
ax[0].violinplot(servived_data)
ax[0].set_title("Violin plot of survived lizards horn length")
ax[1].violinplot(dead_data)
ax[1].set_title("Violin plot of dead lizards horn length")
plt.show()

#independed sample t-test
stat,p = stats.kruskal(servived_data,dead_data)
print('P value for independent two sample t-test',p)



