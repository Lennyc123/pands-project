# f = open("iris.csv", "r")
# contents = f.read()
# print(contents)
# f.close()

with open('iris.csv', 'r') as f:
    for line in f:
        print(line, end='')
    #print(f.readline())

# Always remember to close files
print("This is the end!")

#Current program prints out the data set (csv format)