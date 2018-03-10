from sklearn.tree import DecisionTreeClassifier
from DataHandler import DataHandler
import numpy as np
from Utils import OneHotEncode


allData = DataHandler.getAllData()[1:-1]
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

originEncoder = OneHotEncode()
destinationEncoder = OneHotEncode()

for row in allData:
    origin.append(row[ORIGIN])
    dest.append(row[DEST])

encodedOrigin = originEncoder.encode(origin)
encodedDestination = destinationEncoder.encode(dest)
