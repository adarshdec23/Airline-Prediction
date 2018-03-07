import csv

class DataHandler:

    _allData = []
    _queryData = []
    
    '''
    Training data: 1-70001
    Test data: 70001-73831
    '''
    _trainingStart = 1
    _trainingEnd = 60001
    _testStart = 60001
    _testEnd = 73831

    @staticmethod
    def getAllData():
        if DataHandler._allData:
            return DataHandler._allData
            
        with open("./data/train.csv") as trainingData:
            rawCsvData = csv.reader(trainingData)
            for row in rawCsvData:
                DataHandler._allData.append(row)
        return DataHandler._allData

    @staticmethod
    def getTrainingData():
        allData = DataHandler.getAllData()
        return allData[DataHandler._trainingStart : DataHandler._trainingEnd]
        
    @staticmethod
    def getTestData():
        allData = DataHandler.getAllData()
        return allData[DataHandler._testStart : DataHandler._testEnd]