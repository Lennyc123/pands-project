# 52167 - Programming and Scripting, Project 2020 | Leonard Curtin

## Brief introduction
Within this section the reader should be provided with an initial overview that will allow for one to grasp the direction of which the project has taken.
The overarching approach of the following project is related to that of investigating a data set and further expanding on the concept of investigative research. The development of the project itself occurs through the usage of an object-oriented, high-level programming language known as Python (1). The data set that is to be dissected throughout the course of the project is the Fisher iris data set (2).

## An abstract of information related to Fisher’s iris data set.
Fishers iris data set is a multivariate data set (i.e. where simultaneous observation and analysis of more than one outcome variable occurs). The data set was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper _The use of multiple measurements in taxonomic problems_.
Within the data set, there are 50 samples from each of three species of Iris (Iris Setosa, Iris Virginica, and Iris Versicolor). Of these three species, four variables were obtained (2).
The length and the width of the sepals and petals, which is measured in centimetres.

|Depiction of the variables within the data set|
|---|
|Sepal length (cm)|
|Sepal width (cm)|
|Petal length (cm)|
|Petal width (cm)|

## Accessibility of the data set
The data set is freely available to the public at the UCI Machine Learning Repository. The data set currently stands as the most popular data set on their site (3).
Due to the popularity of the data set, the iris flower data set is built into some coding libraries (4).

## The directional driving force behind the development of the project
This segment explains the route of which was to be paved and acted as the motivational factor behind the growth of the python script.
The python code was developed under the following premises occurring under the name of analysis.py.
The aim of the output related to the analysis.py script was to provide a summary of each variable to a single text file, to save a histogram of each variable to .png files, and to output a scatter plot of each pair of variables.

``` python
# Upon executing the following script, the user will be provided with,
# A summary of the data set and its variables provided by the 'summary.txt' file.
# 4 histogram images(.png files) of the varibles compared amongst the 3 iris species.
# 2 scatter plot images (.png files) of each pair of variables. i.e sepal length plotted against sepal width and petal length plotted against petal width.
```

## The initialisation of the python script i.e. analysis.py
The python code was written in version 3.7 which was downloaded from _Anaconda_ (5). This open-source Anaconda individual Edition comes with several python libraries.

In order for the execution analysis.py to occur successfully one must have the following python libraries installed.

Mathplotlib – a comprehensive library for creating static, animated and interactive visualizations in python (6). 

Pandas – an open source data analysis and manipulation tool (7).

NumPy – a fundamental package for scientific computing (8). 

Seaborn – a data visualization library based on matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics (9). 

## Utilisation of the additional python libraries.
In order to make use of these python libraries, they must first be imported within the script (10).
``` python
# Commands for importing the various python libraries used in order for the script to function properly.
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns
```
## Creation of a DataFrame.
As previously stated, Pandas acts as an open source data analysis and manipulation tool. Throughout the course of the investigation and analysis, the usage of Pandas was central to both the interpretation of the dataset i.e the .csv file and the direction taken by the investigation of the dataset (11).

In order for python to process the contents of the dataset. The “iris.csv” file was interpreted as a dataframe (11).
``` python
# The iris data set is read using pandas, the data set is abbreviated to 'df'.
df = pd.read_csv('iris.csv')
```

## Reduction of the data set into more convenient sections.
The following code was central to allowing the contents of the dataframe to be easily manipulated and was core to the development of the python script. Here the contents of the .csv file were segmented into the various plant species (11).

``` python
# Allows for segmentation of the data set into the various plant species.
setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']
```

## The initial creation of a summary from the information within the Iris data set.
The following code allows for the creation of a summary table, which depicts data such as the mean, min, max and standard deviation. Within this summary table the three plant species are taken into consideration. The contents of the summary table are then appended to the "summary.txt" file (11, 12).

``` python
# The following commands allow for the initial creation of the 'summary.txt' file.
with open("summary.txt", 'a') as file: # 'a' is used to append additions to a file.
    file.write("Descriptive statistical data of the Iris Data Set \n \n") # (Formatting) Header added to the table.
with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string()) # The pandas DataFrame.describe() command provides calculations of statistical data related to the data set set. e.g. mean, std and percentile.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # '\n' creates a line break.
```

### Descriptive statistical data of the Iris Data Set 
Calculation | Sepal Length | Sepal Width | Petal Length | Petal Width |
|------------| ------------| -----------| -----------|     -----------|
| count |    150.000000 |   150.000000 |   150.000000 |  150.000000 |
| mean  |     5.843333  |   3.057333   |  3.758000    | 1.199333    |
| std   |    0.828066   |  0.435866    |  1.765298    | 0.762238    |
| min   |     4.300000  |   2.000000   |   1.000000   |  0.100000   |
| 25%   |    5.100000   |  2.800000    |  1.600000    | 0.300000    |
| 50%   |     5.800000  |  3.000000    |  4.350000    | 1.300000    |
| 75%   |     6.400000  |   3.300000   |   5.100000   |  1.800000   |
| max   |    7.900000   |  4.400000    |  6.900000    | 2.500000    |

## Depiction and explanation of the visual graphics that are outputted upon execution of the analysis.py python script.

### The creation of the histograms.
The histograms were developed through the usage of Matplotlib (13), which allowed for the data contained within the dataset to be depicted in a visual manner. Due to the intuitive nature of Matplotlib development of the histograms occurred with ease and the commands contained within the library provided a vast amount of customisability. This highlights the benefits attached to the usage of Matplotlib, conveying Matplotlib as both an efficient library and one that provides full creative freedom to the user.

Depicted below is an example of the python code that was used for the creation of the histograms.

``` python
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
```

### Development of tables to assist a potential interpreter of the data or user of the analysis.py script.
A summary table was made for each individual variable (14), to assist one in interpreting the data. The initial thought process behind the creation of the tables, was linked to easing the process of understanding both, the information contained within the dataset and also to add a potentially more solid aspect that is related to interpreting the visual data. Upon viewing the visual data i.e., the histograms or scatter plots, the user will be provided with more concrete evidence of an analysis of the dataset. In terms of analysis, the visual data and the tables can be used in tandem to provide an understanding of the data.

``` python
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
```

### Further developments to the summary.txt file
As previously discussed the creation of the summary.txt file occurred through the usage of Pandas and its ability to provide a summary on information contained within a data set.
A Brief depiction of the code used to create a summary of the data, further expanding on the point previously made above (15).
``` python
with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string()) # The pandas DataFrame.describe() command provides calculations of statistical data related to the data set set. e.g. mean, std and percentile.
```


Contained within the summary.txt file are also the tables that were discussed in the previous section. The code shown below, conveys how additions to the summary.txt file were further made (15).
``` python
#The contents of the sepal length DataFrame are appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("Table for Sepal Length Variable\n") # (Formatting) Header added to the table.
with open('summary.txt', 'a') as myfile:
    myfile.write(tbl_sepal_length.to_string()) # The contents of the sepal length DataFrame are transformed to 'string' values and appended to the 'summary.txt' file.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # Line break added for formatting.
```

### The creation of the scatterplots
Similar in nature to the developments of the histograms, the scatterplots were created through the usage of Matplotlib (16).

The code below is an example, related to the creation of the scatterplots

``` python
# Data related to sepal length and sepal width of the 3 iris plants is read from the DataFrame.
# Colour scheme, aplha set to 0.5, and labels added to ease legibilty of the scatter plot.
plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color="cyan", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color="magenta", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color="yellow", alpha=0.5, label="Iris virginica")
```

### Addition of cosmetic features to the scatterplots.
The code in the above section, may be described as the barebones of the scatterplots. Consisting primarily of the data related to the x and y coordinates. In order to ease user legibility, similar to the histograms additional python code was added to help provide an understanding of the data (16).

``` python
plt.title('Relationship between Sepal Length and Sepal Width') # Title added
plt.xlabel('Sepal Length (cm)') # Label for x axis
plt.ylabel('Sepal Width (cm)') # Label for y axis
plt.legend() # addition of a legend
#plt.show()
plt.savefig('Scatter sepal length vs sepal width.png') # scatter plot saved as an image (.png file)
plt.clf() # Contents of scatter plot cleared before beginning a new one.
```

### An explanation of the emphasis placed on easability of interpretation.
Throughout the development of analysis.py with regards to the graphical data. All visual aspects related to the project, were developed with an overarching focus on ease of interpretation.

Primarily seaborn (17) acted as a crucial factor in allowing the stylistic elements to come to fruition. The code below, had an impact on all graphs which were developed through the usage of Matplotlib.

``` python
# Sets the color "Theme" for the various plots using a command from seaborn.
sns.set(palette='bright')
plt.hist(HSW, color='c''m''y', label=['setosa', 'versicolor', 'virginica']) # Addition of color scheme to ease legibility.
```
The colour scheme used throughout the project, was one of which, where the colours were in high contrast to each other. This further emphasises the distinct differences between the variables and the plant species. Usage of alpha command within the development of the scatterplots acted as another visual aid. Values that occur more than once, within the data are plotted with a distinctly more saturated colour.
``` python
alpha=0.5
```


## Depiction of the histograms with an accompaning table related to each individual variable
![sepallength_hist](https://github.com/Lennyc123/pands-project/blob/master/Images/Hist.%20sepal%20length.png)


Table for Sepal Length Variable
Plant Species | Mean | Min | Max | SD | 
| --- | ---| --- | --- | --- |
Setosa |      5.006 | 4.3 | 5.8 | 0.348947 |
Versicolor | 5.936 | 4.9 | 7.0 | 0.510983 |
Virginica  | 6.588 | 4.9 | 7.9 | 0.629489 |


![sepalwidth_hist](https://github.com/Lennyc123/pands-project/blob/master/Images/Hist.%20sepal%20width.png)


Table for Sepal Width Variable
Plant Species | Mean | Min | Max    |    SD |
| --- | --- | --- | --- | --- |
Setosa |     3.428 | 2.3 | 4.4 | 0.375255 |
Versicolor | 2.770 | 2.0 | 3.4 | 0.310644 |
Virginica  | 2.974 | 2.2 | 3.8 | 0.319255 |


![petallength_hist](https://github.com/Lennyc123/pands-project/blob/master/Images/Hist.%20petal%20length.png)


Table for Petal Length Variable
Plant Species | Mean | Min | Max    |    SD |
| --- | --- | --- | --- | --- |
Setosa   |   1.462 | 1.0 | 1.9 | 0.171919 |
Versicolor | 4.260 | 3.0 | 5.1 | 0.465188 |
Virginica  | 5.552 | 4.5 | 6.9 | 0.546348 |


![petalwidth_hist](https://github.com/Lennyc123/pands-project/blob/master/Images/Hist.%20petal%20width.png)


Table for Petal Width Variable
Plant Species | Mean | Min | Max    |    SD |
| --- | --- | --- | --- | --- |
Setosa  |    0.246 | 0.1 | 0.6 | 0.104326 |
Versicolor | 1.326 | 1.0 | 1.8 | 0.195765 |
Virginica |  2.026 | 1.4 | 2.5 | 0.271890 |

## Depiction of the scatterplots
![scatter_sepal](https://github.com/Lennyc123/pands-project/blob/master/Images/Scatter%20sepal%20length%20vs%20sepal%20width.png)
![scatter_petal](https://github.com/Lennyc123/pands-project/blob/master/Images/Scatter%20petal%20length%20vs%20petal%20width.png)


# References
1 - https://www.python.org/doc/essays/blurb/

2 - https://en.wikipedia.org/wiki/Iris_flower_data_set

3 - http://archive.ics.uci.edu/ml/datasets/iris

4 - https://www.techopedia.com/definition/32880/iris-flower-data-set

5 - https://www.anaconda.com/distribution/

6 - https://matplotlib.org/

7 - https://pandas.pydata.org/

8 - https://numpy.org/

9 - https://seaborn.pydata.org/

10 - https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3

11 - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

12 - https://www.guru99.com/reading-and-writing-files-in-python.html

13 - https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html

14 - https://mode.com/python-tutorial/pandas-dataframe/

15 - https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python

16 - https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.scatter.html

17 - https://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial