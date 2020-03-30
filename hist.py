import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('iris.csv')

Setosa = df[df['variety'] == 'Setosa']
Versicolor = df[df['variety'] == 'Versicolor']
Virginica = df[df['variety'] == 'Virginica']

