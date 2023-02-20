'''
Author: Bhagya Hendalage
Date:22/01/2021
Input: temperature.csv
Output:do statistical analysis two paired sample t-test(Kruskal-Wallis H Test)
'''
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
#read the datafile
blackbird = pd.read_csv('BlackbirdTestosterone.csv')
#to get rid from spaces of the colomn header
blackbird=blackbird.rename(columns={'log before':'before','log after':'after','dif in logs':'diff'})
print(blackbird)
# seperate columns
before_data=blackbird['before']
print(before_data)
# seperate columns
after_data=blackbird['after']
print(after_data)
# seperate columns
diff_data=blackbird['diff']
print(diff_data)
# discriptive statisctics
print('before data :',before_data.describe())
print('after data :',after_data.describe())
print('difference data :',diff_data.describe())

# draw qq plot and histogram for log difference
qqplot(diff_data, line='s')
plt.title('QQplot for log difference')
plt.show()
plt.hist(diff_data)
plt.title("Histogram for log difference")
plt.show()
#Shapiro
stat, p = stats.shapiro(diff_data)
print('P value of log difference:',p)
stat, p = stats.shapiro(before_data)
print('P value of log before:',p)
stat, p = stats.shapiro(after_data)
print('P value of log after:',p)
# draw boxplots for two samples
fig,ax =plt.subplots(1,2, figsize=(12,3))
ax[0].boxplot(before_data)
ax[0].set_title("Boxplot of before level of testosterone")
ax[1].boxplot(after_data)
ax[1].set_title("Boxplot of after level of testosterone")
plt.show()

# draw violin plots for two samples
fig,ax =plt.subplots(1,2, figsize=(12,3))
ax[0].violinplot(before_data)
ax[0].set_title("Violin plot of before level of testosterone")
ax[1].violinplot(after_data)
ax[1].set_title("Violin plot of after level of testosterone")
plt.show()

#independed sample t-test
stat,p = stats.kruskal(before_data,after_data)
print('P value for paired sample t-test',p)
