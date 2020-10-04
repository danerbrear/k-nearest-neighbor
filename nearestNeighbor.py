import pandas
from minHeap import MinHeap

# Calculates the euclidian distance between two rows. 
# Skips the class column that we are trying to classify in euclidian distance calculation
def findDistance(trainingRow, testRow, classCol):
    testRowDrop = testRow[1].drop(classCol)
    squaredSum = 0
    for i, item in testRowDrop.iteritems():
        squaredSum += ((trainingRow[i] - item) ** 2)
    distance = squaredSum ** 0.5
    return distance

# Decides a class and returns 1 if wrong and 0 if corrent
def nearestNeighbor(trainingSet, testRow, classCol, k):
    minHeap = MinHeap(len(trainingSet.index))
    for row in trainingSet.iterrows():
        dropRow = row[1].drop(classCol)
        dist = findDistance(dropRow, testRow, classCol)
        minHeap.insert((row, dist))
    minHeap.minHeap()

    # Determine class by k neighbor voting
    votes = {}
    for i in range(k):
        minVal = minHeap.remove()
        if minVal[0][1][classCol] in votes:
            votes[minVal[0][1][classCol]] += 1
        else:
            votes[minVal[0][1][classCol]] = 1
    
    maxVotes = 0
    predictedClass = ""
    for key in votes:
        if votes[key] > maxVotes:
            maxVotes = votes[key]
            predictedClass = key
        
    return 0 if (predictedClass == testRow[1][classCol]) else 1