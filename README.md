# 52167 - Programming and Scripting, Project 2020 | Leonard Curtin

## Brief introduction
Within this section the reader should be provided with an initial overview that will allow for one to grasp the direction of which the project has taken.
The overarching approach of the following project is related to that of investigating a data set and further expanding on the concept of investigative research. The development of the project itself occurs through the usage of an object-oriented, high-level programming language known as Python. The data set that is to be dissected throughout the course of the project is the Fisher iris data set.
 https://www.python.org/doc/essays/blurb/

## An abstract of information related to Fisher’s iris data set.
https://en.wikipedia.org/wiki/Iris_flower_data_set
Fishers iris data set is a multivariate data set (i.e. where simultaneous observation and analysis of more than one outcome variable occurs). The data set was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper _The use of multiple measurements in taxonomic problems_.
Within the data set, there are 50 samples from each of three species of Iris (Iris Setosa, Iris Virginica, and Iris Versicolor). Of these three species, four variables were obtained.
The length and the width of the sepals and petals, which is measured in centimetres.

Depiction of the variables within the data set|
---
|Sepal length (cm)|
|Sepal width (cm)|
|Petal length (cm)|
|Petal width (cm)|

## Accessibility of the data set
The data set is freely available to the public at the UCI Machine Learning Repository. The data set currently stands as the most popular data set on their site.
http://archive.ics.uci.edu/ml/datasets/iris
Due to the popularity of the data set, the iris flower data set is built into some coding libraries.
https://www.techopedia.com/definition/32880/iris-flower-data-set

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
The python code was written in version 3.7 which was downloaded from https://www.anaconda.com/distribution/ . This open-source Anaconda individual Edition comes with several python libraries.
In order for the execution analysis.py to occur successfully one must have the following python libraries installed.
Mathplotlib – a comprehensive library for creating static, animated and interactive visualizations in python. https://matplotlib.org/
Pandas – an open source data analysis and manipulation tool. https://pandas.pydata.org/
NumPy – a fundamental package for scientific computing. https://numpy.org/
Seaborn – a data visualization library based on matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics. https://seaborn.pydata.org/

## Utilisation of the additional python libraries.
In order to use these python libraries, they must first be imported within the script.
``` python
# Commands for importing the various python libraries used in order for the script to function properly.
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns
```
## Creation of a DataFrame.
As previously stated, Pandas acts as an open source data analysis and manipulation tool. Throughout the course of the investigation and analysis, the usage of Pandas was central to both the interpretation of the dataset i.e the .csv file and the direction taken by the investigation of the dataset.

In order for python to process the contents of the dataset. The “iris.csv” file was interpreted as a dataframe.
``` python
# The iris data set is read using pandas, the data set is abbreviated to 'df'.
df = pd.read_csv('iris.csv')
```

## Reduction of the data set into more convenient sections.
The following code was central to allowing the contents of the dataframe to be easily manipulated and was core to the development of the python script. Here the contents of the .csv file were segmented into the various plant species.

``` python
# Allows for segmentation of the data set into the various plant species.
setosa = df[df['variety'] == 'setosa']
versicolor = df[df['variety'] == 'versicolor']
virginica = df[df['variety'] == 'virginica']
```

## The initial creation of a summary from the information within the Iris data set.
The following code allows for the creation of a summary table, which depicts data such as the mean, min, max and standard deviation. Within this summary table the three plant species are taken into consideration. The contents of the summary table are then appended to the "summary.txt" file.

``` python
# The following commands allow for the initial creation of the 'summary.txt' file.
with open("summary.txt", 'a') as file: # 'a' is used to append additions to a file.
    file.write("Descriptive statistical data of the Iris Data Set \n \n") # (Formatting) Header added to the table.
with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string()) # The pandas DataFrame.describe() command provides calculations of statistical data related to the data set set. e.g. mean, std and percentile.
with open("summary.txt", 'a') as file:
    file.write("\n \n") # '\n' creates a line break.
```

#### Descriptive statistical data of the Iris Data Set 
       sepal.length  sepal.width  petal.length  petal.width
	   ------------| ------------| -----------| -----------|
count |    150.000000 |   150.000000 |   150.000000 |  150.000000 |
mean  |     5.843333  |   3.057333   |  3.758000    | 1.199333    |
std   |    0.828066   |  0.435866    |  1.765298    | 0.762238    |
min   |     4.300000  |   2.000000   |   1.000000   |  0.100000   |
25%   |    5.100000   |  2.800000    |  1.600000    | 0.300000    |
50%   |     5.800000  |  3.000000    |  4.350000    | 1.300000    |
75%   |     6.400000  |   3.300000   |   5.100000   |  1.800000   |
max   |    7.900000   |  4.400000    |  6.900000    | 2.500000    |

## Depiction and explanation of the visual graphics that are outputted upon execution of the analysis.py python script.