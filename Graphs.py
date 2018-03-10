import matplotlib.pyplot as plt
from DataHandler import DataHandler


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
    
    

def originStats():
    stats = dict()
    # for idx, city in enumerate(origin):
        # if city not in stats:
            # stats[city] = dict()
        # if label[idx] not in stats[city]:
            # stats[city][label[idx]] = 0
        # stats[city][label[idx]] +=1
        
    for idx, localLabel in enumerate(label):
        if localLabel not in stats:
            stats[localLabel] = dict()
        if origin[idx] not in stats[localLabel]:
            stats[localLabel][origin[idx]] = 0
        stats[localLabel][origin[idx]] +=1
    return stats
    

def Stats(column):
    stats = dict()
    for idx, column in enumerate(column):
        if column not in stats:
            stats[column] = dict()
        if label[idx] not in stats[column]:
            stats[column][label[idx]] = 0
        stats[column][label[idx]] +=1
    return stats
    
print(Stats(pax))