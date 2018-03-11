from sklearn.naive_bayes import BernoulliNB
import numpy as np
from DataHandler import DataHandler
import csv

pair = dict()
counter = 0
for pairInFile in open("data\Pair.txt", "r"):
    pairInFile = pairInFile.rstrip('\n')
    pair[pairInFile] = counter
    counter += 1

fareClass = {"Classic" : 1, "Deal": 2, "Flex": 3, "Saver": 4}

trainingData = DataHandler.getTrainingData()

x = np.empty([len(trainingData),44], dtype=int)
y = np.empty([len(trainingData)], dtype=int)

counter = 0
for trainingList in trainingData:
    oriDestPair = trainingList[2] + trainingList[3]
    paxCount = int(trainingList[-2])
    tempXList = [0] * 44
    tempXList[pair[oriDestPair]] = 1
    if paxCount > 1:
        tempXList[43] = 1
    else:
        tempXList[42] = 1
    x[counter] = tempXList
    y[counter] = fareClass[trainingList[-1]]
    counter += 1

#Create a Gaussian Classifier
model = BernoulliNB()

# Train the model using the training sets
model.fit(x, y)

#Predict Output
testData = DataHandler.getTestData()
finalPredictList = np.empty([len(testData),44], dtype=int)

counter = 0
for testList in testData:
    oriDestPair = testList[2] + testList[3]
    paxCount = int(testList[-2])
    tempXList = [0] * 44
    tempXList[pair[oriDestPair]] = 1
    if paxCount > 1:
        tempXList[43] = 1
    else:
        tempXList[42] = 1
    finalPredictList[counter] = tempXList
    counter += 1

predicted = model.predict_proba(finalPredictList)

#Writing to a CSV file
csvFileHandle = open("data\\NBBernoulli.csv", 'w', newline='')
with csvFileHandle:
    csvWriter = csv.writer(csvFileHandle)
    csvWriter.writerow(['id','Classic','Deal','Flex','Saver'])
    counter = int(testData[0][0])
    for predictList in predicted:
        tempList = np.array(["%.2f" % w for w in predictList.reshape(predictList.size)])
        tempList = tempList.tolist()
        tempList.insert(0,counter)
        csvWriter.writerow(tempList)
        counter += 1

    print("Write Complete")

