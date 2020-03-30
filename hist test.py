
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

df = pd.read_csv('iris.csv') # This command makes a data frame from a csv file

#print(df['sepal.length'])

#Setosa = df[df['variety'] == 'Setosa'] # shortcut Setosa values

#print(Setosa)

# print(df[['sepal.width', 'sepal.length']])

#code = df['sepal.width'] #selecting a specific column
#print(code)

# print(df.iloc[3]) #selecting a single row via its position in a list

Setosa = df[df['variety'] == 'Setosa']
Versicolor = df[df['variety'] == 'Versicolor']
Virginica = df[df['variety'] == 'Virginica']

x = df['sepal.length'], Setosa['sepal.length']
plt.hist(x)
plt.show()

x1 = Setosa['sepal.length']
plt.hist(x1)
#plt.show()

x2 = df['sepal.width']
plt.hist(x2)
#plt.show()

x3 = df['petal.length']
plt.hist(x3)
#plt.show()

x4 = df['petal.length']
plt.hist(x4)
#plt.show()
