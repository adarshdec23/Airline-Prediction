from sklearn.tree import DecisionTreeClassifier
from DataHandler import DataHandler
import numpy as np
from Utils import OneHotEncode
from datetime import datetime


allData = DataHandler.getAllData()[1:]
bookingDate = []
origin = []
dest = []
deptDate = []
deptTime = []
pax = []
label = []

BOOKINGDATE = 1
ORIGIN = 2
DEST = 3
DEPTDATE = 4
DEPTTIME = 5
PAX = 6
LABEL = 7

for row in allData:
    bookingDate.append(row[BOOKINGDATE])
    origin.append(row[ORIGIN])
    dest.append(row[DEST])
    deptDate.append(row[DEPTDATE])
    deptTime.append(row[DEPTTIME])
    pax.append(row[PAX])
    label.append(row[LABEL])
    
def getEncodedDepartureDate(iDeptDate):
    #Transform departure date to day of week - 0-6.  Then again onehot encode it as is required
    departureDay = []
    for stringDate in deptDate:
        departureDay.append(datetime.strptime(stringDate, '%Y%m%d').weekday())

    return OneHotEncode().encode(departureDay)
    
    
    
    

originEncoder = OneHotEncode()
destinationEncoder = OneHotEncode()


encodedOrigin = originEncoder.encode(origin)
encodedDestination = destinationEncoder.encode(dest)


encodedDepartureDay = getEncodedDepartureDate(deptDate)

    