# Upon executing the following script, the user will be provided with,
# A summary of the data set and its variables provided by the 'summary.txt' file.
# 4 histogram images(.png files) of the varibles compared amongst the 3 iris species.
# 2 scatter plot images (.png files) of each pair of variables. i.e sepal length plotted against sepal width and petal length plotted against petal width.

# Commands for importing the various python libraries used in order for the script to function properly.
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

# Sets the color "Theme" for the various plots using a command from seaborn.
sns.set(palette='bright')

# The iris data set is read using pandas, the data set is abbreviated to 'df'.
df = pd.read_csv('iris.csv')

# Allows for segmentation of the data set into the various plant species.
setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']

# The following commands allow for the initial creation of the 'summary.txt' file.
with open("summary.txt", 'a') as file: # 'a' is used to append additions to a file.
    file.write("Descriptive statistical data of the Iris Data Set \n \n") # (Formatting) Header added to the table.
with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string()) # The pandas DataFrame.describe() command provides calculations of statistical data related to the data set set. e.g. mean, std and percentile.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # '\n' creates a line break.


# Creation of table for setpal length variable which is to be added to the 'summary.txt' file.
print('\n Table for Sepal Length Variable') # Heading of the table.
tbl_sepal_length = pd.DataFrame(np.array([ # DataFrame for the variable sepal length created.
[np.mean(setosa['sepal.length']), np.min(setosa['sepal.length']), np.max(setosa['sepal.length']), np.std(setosa['sepal.length'])],
[np.mean(versicolor['sepal.length']), np.min(versicolor['sepal.length']), np.max(versicolor['sepal.length']), np.std(versicolor['sepal.length'])],
[np.mean(virginica['sepal.length']), np.min(virginica['sepal.length']), np.max(virginica['sepal.length']), np.std(virginica['sepal.length'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica'] # Creation of Columns and Indices to provide formatting for the DataFrame.
)
print(tbl_sepal_length) # Contents of the sepal length DataFrame are printed.

#The contents of the sepal length DataFrame are appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("Table for Sepal Length Variable\n") # (Formatting) Header added to the table.
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_sepal_length.to_string()) # The contents of the sepal length DataFrame are transformed to 'string' values and appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # Line break added for formatting.

# Creation of table for Sepal Width variable which is to be added to the 'summary.txt' file.
print('\n Table for Sepal Width Variable') # Heading of the table.
tbl_sepal_width = pd.DataFrame(np.array([ # DataFrame for the variable Sepal Width created.
[np.mean(setosa['sepal.width']), np.min(setosa['sepal.width']), np.max(setosa['sepal.width']), np.std(setosa['sepal.width'])],
[np.mean(versicolor['sepal.width']), np.min(versicolor['sepal.width']), np.max(versicolor['sepal.width']), np.std(versicolor['sepal.width'])],
[np.mean(virginica['sepal.width']), np.min(virginica['sepal.width']), np.max(virginica['sepal.width']), np.std(virginica['sepal.width'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica'] # Creation of Columns and Indices to provide formatting for the DataFrame.
)
print(tbl_sepal_width) # Contents of the sepal width DataFrame are printed.

#The contents of the sepal width DataFrame are appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("Table for Sepal Width Variable\n") # (Formatting) Header added to the table.
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_sepal_width.to_string()) # The contents of the sepal width DataFrame are transformed to 'string' values and appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # Line break added for formatting.

# Creation of table for Petal Length variable which is to be added to the 'summary.txt' file.
print('\n Table for Petal Length Variable') # Heading of the table.
tbl_petal_length = pd.DataFrame(np.array([ # DataFrame for the variable Petal Length created.
[np.mean(setosa['petal.length']), np.min(setosa['petal.length']), np.max(setosa['petal.length']), np.std(setosa['petal.length'])],
[np.mean(versicolor['petal.length']), np.min(versicolor['petal.length']), np.max(versicolor['petal.length']), np.std(versicolor['petal.length'])],
[np.mean(virginica['petal.length']), np.min(virginica['petal.length']), np.max(virginica['petal.length']), np.std(virginica['petal.length'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica'] # Creation of Columns and Indices to provide formatting for the DataFrame.
)
print(tbl_petal_length) # Contents of the Petal Length DataFrame are printed.

#The contents of the Petal Length DataFrame are appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("Table for Petal Length Variable\n") # (Formatting) Header added to the table.
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_petal_length.to_string()) # The contents of the Petal Length DataFrame are transformed to 'string' values and appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # Line break added for formatting.

# Creation of table for Petal Width variable which is to be added to the 'summary.txt' file.
print('\n Table for Petal Width Variable') # Heading of the table.
tbl_petal_width = pd.DataFrame(np.array([ # DataFrame for the variable Petal Length created.
[np.mean(setosa['petal.width']), np.min(setosa['petal.width']), np.max(setosa['petal.width']), np.std(setosa['petal.width'])],
[np.mean(versicolor['petal.width']), np.min(versicolor['petal.width']), np.max(versicolor['petal.width']), np.std(versicolor['petal.width'])],
[np.mean(virginica['petal.width']), np.min(virginica['petal.width']), np.max(virginica['petal.width']), np.std(virginica['petal.width'])],
]),
columns=['Mean', 'Min', 'Max', 'SD'], index=['Setosa','Versicolor', 'Virginica'] # Creation of Columns and Indices to provide formatting for the DataFrame.
)
print(tbl_petal_width) # Contents of the Petal Width DataFrame are printed.

#The contents of the Petal Width DataFrame are appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("Table for Petal Width Variable\n") # (Formatting) Header added to the table.
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_petal_width.to_string()) # The contents of the Petal Width DataFrame are transformed to 'string' values and appended to the 'summary.txt' file.


# The following commands allow for the creation of histograms related to the various variables within the data set i.e. Sepal length, sepal width, petal length and petal width.

# Creation of histogram for sepal length which takes the 3 different plant species into consideration.
HSL = setosa['sepal.length'], versicolor['sepal.length'], virginica['sepal.length']
plt.hist(HSL, color='c''m''y', label=['setosa', 'versicolor', 'virginica']) # Addition of color scheme to ease legibility.
plt.xlabel('Value') # Label for x axis 
plt.ylabel('Frequency') # label for y axis
plt.title('Histogram of Sepal Length (cm)  Variable') # Title added to histogram
plt.legend() # addition of a legend
#plt.show() # Issue arose when the following command was left within the script, .png images were appearing white i.e the contents of the histograms were not added to the .png files.
plt.savefig('Hist. sepal length.png') # Histogram of sepal length is saved as an image(.png file).
plt.clf() # Contents of histogram cleared before beginning a new one.


# Creation of histogram for sepal width which takes the 3 different plant species into consideration.
HSW = setosa['sepal.width'], versicolor['sepal.width'], virginica['sepal.width']
plt.hist(HSW, color='c''m''y', label=['setosa', 'versicolor', 'virginica']) # Addition of color scheme to ease legibility.
plt.xlabel('Value') # Label for x axis 
plt.ylabel('Frequency') # Label for y axis 
plt.title('Histogram of Sepal Width (cm)  Variable') # Title added to histogram
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Hist. sepal width.png') # Histogram of sepal width is saved as an image(.png file).
plt.clf() # Contents of histogram cleared before beginning a new one.


# Creation of histogram for petal length which takes the 3 different plant species into consideration.
HPL = setosa['petal.length'], versicolor['petal.length'], virginica['petal.length'] 
plt.hist(HPL, color='c''m''y', label=['setosa', 'versicolor', 'virginica']) # Addition of color scheme to ease legibility.
plt.xlabel('Value') # Label for x axis 
plt.ylabel('Frequency') # Label for y axis 
plt.title('Histogram of Petal Length (cm)  Variable') # Title added to histogram
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Hist. petal length.png')  # Histogram of petal length is saved as an image(.png file).
plt.clf() # Contents of histogram cleared before beginning a new one.

# Creation of histogram for petal width which takes the 3 different plant species into consideration.
HPW = setosa['petal.width'], versicolor['petal.width'], virginica['petal.width']
plt.hist(HPW, color='c''m''y', label=['setosa', 'versicolor', 'virginica']) # Addition of color scheme to ease legibility.
plt.xlabel('Value') # Label for x axis 
plt.ylabel('Frequency') # Label for y axis
plt.title('Histogram of Petal Width (cm)  Variable') # Title added to histogram
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Hist. petal width.png') # Histogram of petal width is saved as an image(.png file).
plt.clf() # Contents of histogram cleared before beginning a new one.


# The following commands are related to the creation of scatter plots.

# Data related to sepal length and sepal width of the 3 iris plants is read from the DataFrame.
# Colour scheme, aplha set to 0.5, and labels added to ease legibilty of the scatter plot.
plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color="cyan", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color="magenta", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color="yellow", alpha=0.5, label="Iris virginica")

plt.title('Relationship between Sepal Length and Sepal Width') # Title added
plt.xlabel('Sepal Length (cm)') # Label for x axis
plt.ylabel('Sepal Width (cm)') # Label for y axis
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Scatter sepal length vs sepal width.png') # scatter plot saved as an image (.png file)
plt.clf() # Contents of scatter plot cleared before beginning a new one.

# Data related to petal length and petal width of the 3 iris plants is read from the DataFrame.
# Colour scheme, aplha set to 0.5, and labels added to ease legibilty of the scatter plot.
plt.scatter(setosa['petal.length'], setosa['petal.width'], color="cyan", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['petal.length'], versicolor['petal.width'], color="magenta", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['petal.length'], virginica['petal.width'], color="yellow", alpha=0.5, label="Iris virginica")

plt.title('Relationship between Petal Length and Petal Width') # Title added
plt.xlabel('Petal Length (cm)') # Label for x axis
plt.ylabel('Petal Width (cm)') # Label for y axis
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Scatter petal length vs petal width.png') # scatter plot saved as an image (.png file)
plt.clf()

print('\n Thank you for executing the analysis.py script, you should have been provided with a summary.txt file, four histogram.png files and two scatter plot.png files')
print('\n Also summary tables for the various variables should be printed to the terminal/console')
print('\n Please note that, executing the script more than once before deleting any instances of the summary.txt file, can lead to the duplication of the contents within the summary.txt file.')