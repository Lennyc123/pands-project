import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('iris.csv') # This command makes a data frame from a csv file

#print(df['sepal.length'])

#setosa = df[df['variety'] == 'setosa'] # shortcut setosa values

#print(setosa)

# print(df[['sepal.width', 'sepal.length']])

#code = df['sepal.width'] #selecting a specific column
#print(code)

# print(df.iloc[3]) #selecting a single row via its position in a list

sns.set(palette='bright')

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

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
