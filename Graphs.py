import matplotlib.pyplot as plt
from DataHandler import DataHandler


allData = DataHandler.getAllData()
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