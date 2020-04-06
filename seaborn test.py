import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

sns.set(palette='bright')

df = pd.read_csv('iris.csv')

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

HSL = setosa['sepal.length'], versicolor['sepal.length'], virginica['sepal.length']
plt.hist(HSL, color='c''m''y', label=['setosa', 'versicolor', 'virginica'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length (cm) Variable')
plt.legend()
plt.show()