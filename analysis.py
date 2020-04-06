import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('iris.csv')

with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string())

sns.set(palette='bright')

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

# Commands Related to Histogram
HSL = setosa['sepal.length'], versicolor['sepal.length'], virginica['sepal.length']
plt.hist(HSL, color='c''m''y', label=['setosa', 'versicolor', 'virginica'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length (cm)  Variable')
plt.legend()
#plt.show()
plt.savefig('Hist. sepal length.png')
plt.clf()

HSW = setosa['sepal.width'], versicolor['sepal.width'], virginica['sepal.width']
plt.hist(HSW, color='c''m''y', label=['setosa', 'versicolor', 'virginica'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Width (cm)  Variable')
plt.legend()
#plt.show()
plt.savefig('Hist. sepal width.png')
plt.clf()

HPL = setosa['petal.length'], versicolor['petal.length'], virginica['petal.length']
plt.hist(HPL, color='c''m''y', label=['setosa', 'versicolor', 'virginica'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length (cm)  Variable')
plt.legend()
#plt.show()
plt.savefig('Hist. petal length.png')
plt.clf()

HPW = setosa['petal.width'], versicolor['petal.width'], virginica['petal.width']
plt.hist(HPW, color='c''m''y', label=['setosa', 'versicolor', 'virginica'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width (cm)  Variable')
plt.legend()
#plt.show()
plt.savefig('Hist. petal width.png')
plt.clf()


#Commnads related to scatter plot
plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color="cyan", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color="magenta", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color="yellow", alpha=0.5, label="Iris virginica")

plt.title('Relationship between Sepal Length and Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
#plt.show()
plt.savefig('Scatter sepal length vs sepal width.png')
plt.clf()

plt.scatter(setosa['petal.length'], setosa['petal.width'], color="cyan", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['petal.length'], versicolor['petal.width'], color="magenta", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['petal.length'], virginica['petal.width'], color="yellow", alpha=0.5, label="Iris virginica")

plt.title('Relationship between Petal Length and Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
#plt.show()
plt.savefig('Scatter petal length vs petal width.png')
plt.clf()
