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
    
def getEncodedDepartureTime(iDeptTime):
    timeSlots = []
    for oneTimeSlot in iDeptTime:
        oneTimeSlot = int(oneTimeSlot)
        if oneTimeSlot > 0 and oneTimeSlot < 359:
            timeSlots.append("night")
        elif oneTimeSlot >= 400 and oneTimeSlot <1100:
            timeSlots.append("morning")
        elif oneTimeSlot >= 1100 and oneTimeSlot < 1540:
            timeSlots.append("noon")
        elif oneTimeSlot >=1540 and oneTimeSlot < 2000:
            timeSlots.append("evening")
        else:
            timeSlots.append("night")

    return  OneHotEncode().encode(timeSlots)

def getEncodedPax(iPax):
    encodedPax = []
    for row in iPax:
        if int(row) > 1:
            encodedPax.append("group")
        else:
            encodedPax.append("single")
    return OneHotEncode().encode(encodedPax)
    
    

originEncoder = OneHotEncode()
destinationEncoder = OneHotEncode()


encodedOrigin = originEncoder.encode(origin)
encodedDestination = destinationEncoder.encode(dest)


encodedDepartureDay = getEncodedDepartureDate(deptDate)

encodedDepartureTime = getEncodedDepartureTime(deptTime)

encodedPax = getEncodedPax(pax)

# There, all done preparing data. Now for the hard part :(