'''
Author: Bhagya Hendalage
Date : 23/01/2021
implement the K-means clustering algorithm on the famous iris data set
'''
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
# read iris dataset
iris_data = pd.read_csv('iris.csv')
#print(iris_data)

# get sepal length and width
sep_len_wid = pd.DataFrame(iris_data, columns=['sepal.length', 'sepal.width'])
v_label=pd.DataFrame(iris_data,columns=['v_short'])
print(v_label)
#print(sep_len_wid)
# labels of dataset
labels = iris_data['v_short']
#print(labels)
#Kmeans test
kmeans=KMeans(n_clusters=3).fit(sep_len_wid)
#getting cetroids
centrodis=kmeans.cluster_centers_
#print(centrodis)
lable=kmeans.labels_
print(lable)

# unknown data sample
unknown=np.array([[4.6, 3.0, 1.5, 0.2],[6.2, 3.0,4.1,1.2]])
new_x = unknown[:, [0, 1]]
predicted=kmeans.predict(new_x)
print(predicted)
#scatter plot of sepal length ,sepal width ,unknown sapal data with cetroids
plt.scatter(sep_len_wid['sepal.length'],sep_len_wid['sepal.width'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
#plt.show()
# unknown data
plt.scatter(unknown[:,0],unknown[:,1],c='green',s=50)
plt.scatter(centrodis[:,0],centrodis[:,1],c='red',s=50)
#plt.show()
#annotation of v_short labels
for labels, x, y,z in zip(labels, sep_len_wid.iloc[:, 0], sep_len_wid.iloc[:, 1],v_label.iloc[:,0]):
    if z=='s':
        plt.annotate(
            labels,
            xy=(x, y),
            xytext=(-30, 30), textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))
    elif z == 've':
        plt.annotate(
            labels,
            xy=(x, y),
            xytext=(60, -60), textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))

    else:
        plt.annotate(
            labels,
            xy=(x, y),
            xytext=(60, 60),
            textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))

#label annotation
for label, x, y in zip(lable, sep_len_wid.iloc[:, 0], sep_len_wid.iloc[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        textcoords='offset points'

       )
plt.show()
print("for the petals data")
#define label columns
labels=iris_data['v_short']

##add petal data to data frame
pet_len_wid=pd.DataFrame(iris_data,columns=['petal.length','petal.width'])
v_label=pd.DataFrame(iris_data,columns=['v_short'])

#kmeans test for petal
kmeans = KMeans(n_clusters=3, random_state=0).fit(pet_len_wid)

#getting cetroids
centrodis=kmeans.cluster_centers_
predicted=kmeans.predict(new_x)
print(predicted)

#define labels
label2=kmeans.labels_
print(labels)

#unknown sample petal data
new_x = unknown[:, [2, 3]]

#scatter plot of petal length ,petal width ,unknown sapae data with cetroids
plt.scatter(pet_len_wid['petal.length'],pet_len_wid['petal.width'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(new_x[:,0],new_x[:,1],c='green',s=50)
plt.scatter(centrodis[:,0],centrodis[:,1],c='red',s=50)
#plt.show()
#annotation from v_short
for labels, x, y,z in zip(labels, pet_len_wid.iloc[:, 0], pet_len_wid.iloc[:,1],v_label.iloc[:,0]):
    if z=='s':
        plt.annotate(
            labels,
            xy=(x, y), xytext=(-60, 60),
            textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))
    elif z == 've':
        plt.annotate(
            labels,
            xy=(x, y), xytext=(60, -60),
            textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))
    else:
        plt.annotate(
            labels,
            xy=(x, y), xytext=(-60, 60),
            textcoords="offset points",
            va="bottom", ha="right",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"))
#annotation of labels
for label, x, y in zip(label2, pet_len_wid.iloc[:, 0], pet_len_wid.iloc[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        textcoords='offset points')

plt.show()