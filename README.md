# k Nearest Neighbor
This repository consists of the k Nearest Neighbor machine learning algorithm. It's purpose is to find the example in the training set with the smallest Euclidian distance from the test set. *k* represents the number of voting neighbors to determine the test set's class. For example, if we are classifying iris flowers, *k* equals 3, and the 3 smallest training examples are classified as Iris-versicolor, Iris-setosa, and Iris-versicolor, the test set will be classified as Iris-versicolor since that class has the most voting neighbors.
## Input
Upon entry to the program, you will be prompted for the following inputs:
1. Training data set file path
2. Test data set file path
3. Header file path (optional if data file's first row contains header names)
4. K value
Notes: Be sure to only include one empty line at the end of each data file.
## Functionality and Data Structures
1. Transform the file lines into a workable dataframes and convert the appropriate strings to numerical values.
2. Preprocess the datasets by normalizing the values.
3. Use a min heap to store Euclidian distances for each test set
4. Pop the first *k* values from the heap to determine classification for the test set
