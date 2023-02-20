'''
Author: Bhagya Hendalage
Date:21/01/2021
Input: temperature.csv
Output:do statistical analysis like normality test and one sample t-test
'''
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
from scipy import stats

# read the temperarure data file and analyze the descriptive statistics
tem = pd.read_csv("Temperature.csv")
print(tem.describe())
# histogram
plt.hist(tem)
plt.title("Histogram for human body temperatures")
plt.show()
# QQ plot
qqplot(tem, line='s')
plt.title('QQplot for human body temperature')
plt.show()
#Shapiro
stat, p = stats.shapiro(tem)
print('P value:',p)

#t-test
checkvalue = 98.6
t,p =stats.ttest_1samp(tem, checkvalue)
print('t value',t)
print('P value',p)

