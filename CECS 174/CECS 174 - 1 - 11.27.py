import random
import importFile

importFile.speciesNum = 1

fileR = open("TestCSV.csv", 'r') # \\ : go up one directory
dataC = fileR.read()
print(dataC)
fileR.close()

txtFileR = open("test.txt", 'r')
data = txtFileR.read()
print(data)
txtFileR.close()

txtFileW = open("test.txt", 'w')
#txtFileW.write
txtFileW.write("Test line")
txtFileW.close()

print("asdasd \u1232 ")