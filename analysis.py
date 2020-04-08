import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

sns.set(palette='bright')

df = pd.read_csv('iris.csv')

setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

with open("summary.txt", 'a') as file:
    file.write("Descriptive statistical data of the Iris Data Set \n \n")
with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string())
with open("summary.txt", 'a') as file:
    file.write("\n \n")

print('\n Table for Sepal Length Variable')
tbl_sepal_length = pd.DataFrame(np.array([
[np.mean(setosa['sepal.length']), np.min(setosa['sepal.length']), np.max(setosa['sepal.length']), np.std(setosa['sepal.length'])],
[np.mean(versicolor['sepal.length']), np.min(versicolor['sepal.length']), np.max(versicolor['sepal.length']), np.std(versicolor['sepal.length'])],
[np.mean(virginica['sepal.length']), np.min(virginica['sepal.length']), np.max(virginica['sepal.length']), np.std(virginica['sepal.length'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica']
)
print(tbl_sepal_length)

with open("summary.txt", 'a') as file:
    file.write("Table for Sepal Length Variable\n")
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_sepal_length.to_string())
with open("summary.txt", 'a') as file:
    file.write("\n \n")

print('\n Table for Sepal Width Variable')
tbl_sepal_width = pd.DataFrame(np.array([
[np.mean(setosa['sepal.width']), np.min(setosa['sepal.width']), np.max(setosa['sepal.width']), np.std(setosa['sepal.width'])],
[np.mean(versicolor['sepal.width']), np.min(versicolor['sepal.width']), np.max(versicolor['sepal.width']), np.std(versicolor['sepal.width'])],
[np.mean(virginica['sepal.width']), np.min(virginica['sepal.width']), np.max(virginica['sepal.width']), np.std(virginica['sepal.width'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica']
)
print(tbl_sepal_width)

with open("summary.txt", 'a') as file:
    file.write("Table for Sepal Width Variable\n")
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_sepal_width.to_string())
with open("summary.txt", 'a') as file:
    file.write("\n \n")

print('\n Table for Petal Length Variable')
tbl_petal_length = pd.DataFrame(np.array([
[np.mean(setosa['petal.length']), np.min(setosa['petal.length']), np.max(setosa['petal.length']), np.std(setosa['petal.length'])],
[np.mean(versicolor['petal.length']), np.min(versicolor['petal.length']), np.max(versicolor['petal.length']), np.std(versicolor['petal.length'])],
[np.mean(virginica['petal.length']), np.min(virginica['petal.length']), np.max(virginica['petal.length']), np.std(virginica['petal.length'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica']
)
print(tbl_petal_length)

with open("summary.txt", 'a') as file:
    file.write("Table for Petal Length Variable\n")
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_petal_length.to_string())
with open("summary.txt", 'a') as file:
    file.write("\n \n")


print('\n Table for Petal Width Variable')
tbl_petal_width = pd.DataFrame(np.array([
[np.mean(setosa['petal.width']), np.min(setosa['petal.width']), np.max(setosa['petal.width']), np.std(setosa['petal.width'])],
[np.mean(versicolor['petal.width']), np.min(versicolor['petal.width']), np.max(versicolor['petal.width']), np.std(versicolor['petal.width'])],
[np.mean(virginica['petal.width']), np.min(virginica['petal.width']), np.max(virginica['petal.width']), np.std(virginica['petal.width'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica']
)
print(tbl_petal_width)

with open("summary.txt", 'a') as file:
    file.write("Table for Petal Width Variable\n")
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_petal_width.to_string())


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
