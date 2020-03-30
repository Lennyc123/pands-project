import pandas
df = pandas.read_csv('iris.csv')

# print(df.describe()) #df.describe provides a quick statistic summary of your data:



with open("summary.txt", 'a') as file:
    file.write(df.describe().to_string())

with open("summary.txt", 'a') as file:
    file.write("\n hello \n this is a test")




