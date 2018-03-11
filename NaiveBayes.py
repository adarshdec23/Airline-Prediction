from sklearn.naive_bayes import BernoulliNB
import sklearn.metrics as Metrices
import numpy as np
from DataHandler import DataHandler
import csv
import sys

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
predictedValue = model.predict(finalPredictList)

#Result Array
result = np.empty(len(testData),dtype=int)
ctr = 0
for tempList in testData:
    result[ctr] = fareClass[tempList[-1]]
    ctr += 1

print("Accuracy : ", Metrices.accuracy_score(result, predictedValue, normalize=False))

#Writing to a CSV file
csvFileHandle = open("data\\NBBernoulli.csv",'w', newline='')
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

def finalResult():
    finalData = list()

    #File read operation
    with open('data\\test.csv','r') as finalDataFH:
        rawCsvData = csv.reader(finalDataFH)
        for row in rawCsvData:
            finalData.append(row)

    #only if data is read
    if finalData:
        finalResArr = np.empty([len(finalData)-1,44], dtype=int)

        #Forming the array for prediction
        counter = 0
        for testList in finalData[1:]:
            oriDestPair = testList[2] + testList[3]
            paxCount = int(testList[-1])
            tempXList = [0] * 44
            tempXList[pair[oriDestPair]] = 1
            if paxCount > 1:
                tempXList[43] = 1
            else:
                tempXList[42] = 1
            finalResArr[counter] = tempXList
            counter += 1

        result = model.predict_proba(finalResArr)

        # Writing to a CSV file
        csvWriteHandle = open("data\\NBBernoulliRes.csv", 'w', newline='')
        with csvWriteHandle:
            csvResWriter = csv.writer(csvWriteHandle)
            csvResWriter.writerow(['id', 'Classic', 'Deal', 'Flex', 'Saver'])
            counter = int(finalData[1][0])
            for predictList in result:
                tempList = np.array(["%.2f" % w for w in predictList.reshape(predictList.size)])
                tempList = tempList.tolist()
                tempList.insert(0, counter)
                csvResWriter.writerow(tempList)
                counter += 1

        print("Completed the Result Write")
    return

option = input("Do you want to run it on the test Data? (Y/N)")
if option == 'Y':
    finalResult()




