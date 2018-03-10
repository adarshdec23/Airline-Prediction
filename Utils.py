import numpy as np

class OneHotEncode:
    def __init__(self):
        self.orderedInput = None
        self.uniqueCount = None
    
    def encode(self, iValueToEncode):
        self.orderedInput = list(sorted(set(iValueToEncode)))
        self.uniqueCount = len(self.orderedInput)
        #print(self.orderedInput)
        oResult = np.zeros((len(iValueToEncode), self.uniqueCount))
        for idx, item in enumerate(iValueToEncode):
            oResult[idx][self.orderedInput.index(item)] = 1
        return oResult