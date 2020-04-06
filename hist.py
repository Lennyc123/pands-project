import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('iris.csv')

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

