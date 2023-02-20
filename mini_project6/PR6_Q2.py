'''
Author : Bhagya Hendalage
K-nearest neighbors (KNN) algorithm implement using the iris data set
'''
#import packages
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Loading dataset
iris = load_iris()
#print(iris)
# extract only data
iris_data = iris['data']
#print(iris_data)
# labels of data
iris_targets = iris['target']
#print(iris_targets)
#target names
iris_spp = iris['target_names']
#print(iris_spp)

# standarize the data
scalar=StandardScaler().fit(iris_data)
iris_standards=scalar.transform(iris_data)
#print(iris_standards)

# create arrays and standalize the data
plant1=np.array([[4.6, 3.0, 1.5, 0.2]])
plants = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]])
plant1_standards= scalar.transform(plant1)
plants_standards= scalar.transform(plants)

#selecting sepal column
sepal=iris_standards[:, :2]
test_plant1 = plant1_standards[:, :2]
test_plants = plants_standards[:, :2]
# for sepal data training and predicting for 2 neighbors
print('for sepal data',end='\n')
print("for 2 neighbors")
classifier = KNeighborsClassifier(n_neighbors=2).fit(sepal, iris_targets)

for test in test_plant1:
    print("species prediction:")
    for i in classifier.predict(test_plant1):
        print(iris_spp[i], end='\n')
    print(" 2-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 2)[1][0]:
        print("index:", n, end='\t')
        print("data value:", sepal[n], end='\t')
        pred =  classifier.predict([sepal[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])

# for sepal data training and predicting for 5 neighbors
print("for 5 neighbours")
classifier = KNeighborsClassifier(n_neighbors=5).fit(sepal, iris_targets)
for test in test_plants:
    print("species prediction:")
    for i in classifier.predict(test_plants):
        print(iris_spp[i], end='\n')
    print("5-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 5)[1][0]:
        print("index:", n, end='\t')
        print("data value:", sepal[n], end='\t')
        pred =  classifier.predict([sepal[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])
#predictions
print("Predictions for sepal data:")
for pred_species, pred_probability in zip(classifier.predict(test_plants),
                                          classifier.predict_proba(test_plants)):
    print('label',pred_species, end='\t')
    print('species',iris_spp[pred_species], end='\t')
    print(f'(probability: {pred_probability})')

#for petal data
print("for petal data",end='\n')
#select petal data column
test_plants = plants_standards[:, 2:]
petal = iris_standards[:, 2:]
print("for 2 neighbors ")

# for petal data training and predicting for 2 neighbors
classifier = KNeighborsClassifier(n_neighbors=2).fit(petal, iris_targets)

#print result
for test in test_plant1:
    print("species prediction:")
    for i in classifier.predict(test_plant1):
        print(iris_spp[i], end='\n')
    print("2-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 2)[1][0]:
        print("index:", n, end='\t')
        print("data value:", petal[n], end='\t')
        pred =  classifier.predict([petal[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])

print("for 5 neighbours")
# for petal data training and predicting for 5 neighbors
classifier = KNeighborsClassifier(n_neighbors=5).fit(petal, iris_targets)

#print result
for test in test_plants:
    print("species prediction:")
    for i in classifier.predict(test_plants):
        print(iris_spp[i], end='\n')
    print("5-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 5)[1][0]:
        print("index:", n, end='\t')
        print("data value:", petal[n], end='\t')
        pred =  classifier.predict([petal[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])
#predictions
print("Predictions for petal data:",end='\n')
test_plant1 = plant1_standards[:, 2:]
for pred_species, pred_probability in zip(classifier.predict(test_plants),
                                          classifier.predict_proba(test_plants)):
    print('label',pred_species, end='\t')
    print('species',iris_spp[pred_species], end='\t')
    print(f'(probability: {pred_probability})')

#using both petal and sepal data
print("for sepal and petal data")
test_plants = plants_standards[:, :]
data = iris_standards[:, :]
test_plant1 = plant1_standards[:, :]
print("for 2 neighbors ")

# for sepal and petal data training and predicting for 2 neighbors
classifier = KNeighborsClassifier(n_neighbors=2).fit(data, iris_targets)

#print result
for test in test_plant1:
    print("species prediction:")
    for i in classifier.predict(test_plant1):
        print(iris_spp[i], end='\n')
    print("2-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 2)[1][0]:
        print("index:", n, end='\t')
        print("data value:", data[n], end='\t')
        pred =  classifier.predict([data[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])

# for sepal and petal data training and predicting for 5 neighbors
print("for 5 neighbours")
classifier = KNeighborsClassifier(n_neighbors=5).fit(data, iris_targets)
for test in test_plants:
    print("species prediction:")
    for i in classifier.predict(test_plants):
        print(iris_spp[i], end='\n')
    print("5-Nearest Neightbours:")
    for n in classifier.kneighbors([test], 5)[1][0]:
        print("index:", n, end='\t')
        print("data value:", data[n], end='\t')
        pred =  classifier.predict([data[n]])[0]
        print('label:', pred, end='\t')
        print('species:', iris_spp[pred])
# prediction
print("Predictions for sepal and petal data:")
for pred_species, pred_probability in zip(classifier.predict(test_plants),
                                          classifier.predict_proba(test_plants)):
    print('label:',pred_species, end='\t')
    print('species:',iris_spp[pred_species], end='\t')
    print(f'(probability: {pred_probability})')