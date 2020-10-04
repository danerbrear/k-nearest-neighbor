import os
import math

from cleanData import cleanData
from preprocess import preprocess
from nearestNeighbor import nearestNeighbor
from progressBar import printProgressBar

# # Get path for data file and open
# inputPath = input("Enter the path of your file ('parent/filename.filetype'): ")
# inputPath = "iris_data/iris.data"
inputPath = "abalone_data/abalone.data"
# inputPath = "mock_data/mock.data"
# assert os.path.exists(inputPath), "I did not find the file at, "+str(inputPath)
dataFile = open(inputPath, "r+")

# # Get path for data file and open
# inputPath = input("Enter the path of your file ('parent/filename.filetype'): ")
# inputPath = "iris_data/testData.data"
inputPath = "abalone_data/testData.data"
# inputPath = "mock_data/mock.data"
# assert os.path.exists(inputPath), "I did not find the file at, "+str(inputPath)
testFile = open(inputPath, "r+")

# Check if has a names file. If yes, open file
hasHeader = True
# inputNamePath = input("Enter the path of your file: ")
# inputNamePath = "iris_data/irisNames.txt"
inputNamePath = "abalone_data/abaloneNames.txt"
# inputNamePath = "mock_data/mock.txt"
if os.path.exists(inputNamePath):
    hasHeader = False
nameFile = open(inputNamePath, "r+")
nameFile2 = open(inputNamePath, "r+")

# Get k for number of voters
k = int(input("k = "))

# Get row name for classification attribute
classCol = input("Name of column to be the class attribute: ")

# Clean data
trainingSet = cleanData(dataFile, nameFile)
testSet = cleanData(testFile, nameFile2)

# Preprocess datasets
preprocessedTrainingSet = preprocess(trainingSet)
preprocessedTestSet = preprocess(testSet)

# Find nearest neighbor for each test row and compute error rate
testCount = 0
errors = 0
totalCount = len(preprocessedTestSet)
printProgressBar(0, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
for row in preprocessedTestSet.iterrows():
    errors += nearestNeighbor(preprocessedTrainingSet, row, classCol, k)
    testCount += 1
    printProgressBar(testCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
    

print("Error rate: ", errors/(testCount))

dataFile.close()
if(not hasHeader):
    nameFile.close()
    nameFile2.close()