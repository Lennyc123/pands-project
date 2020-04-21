Heading Related to module title, insert name also
52167 - Programming and Scripting, Project 2020 | Leonard Curtin

Brief introduction
Within this section the reader should be provided with an initial overview that will allow for one to grasp the direction of which the project has taken.
The overarching approach of the following project is related to that of investigating a data set and further expanding on the concept of investigative research. The development of the project itself occurs through the usage of an object-oriented, high-level programming language known as Python. The data set that is to be dissected throughout the course of the project is the Fisher iris data set.
 https://www.python.org/doc/essays/blurb/

An abstract of information related to Fisher’s iris data set.
https://en.wikipedia.org/wiki/Iris_flower_data_set
Fishers iris data set is a multivariate data set (i.e. where simultaneous observation and analysis of more than one outcome variable occurs). The data set was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper the use of multiple measurements in taxonomic problems.
Within the data set, there are 50 samples from each of three species of Iris (Iris Setosa, Iris Virginica, and Iris Versicolor). Of these three species, four variables were obtained.
The length and the width of the sepals and petals, which is measured in centimetres.

Depiction of the variables within the data set
	Sepal length (cm)
	Sepal width (cm)
	Petal length (cm)
	Petal width (cm)

Accessibility of the data set
Inserting link to UCI
The data set is freely available to the public at the UCI Machine Learning Repository. The data set currently stands as the most popular data set on their site.
http://archive.ics.uci.edu/ml/datasets/iris
Due to the popularity of the data set, the iris flower data set is built into some coding libraries.
https://www.techopedia.com/definition/32880/iris-flower-data-set

The directional driving force behind the development of the project
This segment explains the route of which was to be paved and acted as the motivational factor behind the growth of the python script.
The python code was developed under the following premises occurring under the name of analysis.py.
The output of which the analysis.py script was to provide a summary of each variable to a single text file, to save a histogram of each variable to .png files, and to output a scatter plot of each pair of variables.

The initialisation of the python script i.e. analysis.py
The python code was written in version 3.7 which was downloaded from https://www.anaconda.com/distribution/ . This open-source Anaconda individual Edition comes with several python libraries.
In order for the execution analysis.py to occur successfully one must have the following python libraries installed.
Mathplotlib – a comprehensive library for creating static, animated and interactive visualizations in python. https://matplotlib.org/
Pandas – an open source data analysis and manipulation tool. https://pandas.pydata.org/
NumPy – a fundamental package for scientific computing. https://numpy.org/
Seaborn – a data visualization library based on matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics. https://seaborn.pydata.org/


# Commands for importing the various python libraries used in order for the script to function properly.
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns



