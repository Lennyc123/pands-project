import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 
import seaborn as sns

sns.set(palette='bright')

df = pd.read_csv('iris.csv') # This command makes a data frame from a csv file

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

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

