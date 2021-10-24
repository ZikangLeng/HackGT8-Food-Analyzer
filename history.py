from day import *
class History:
    #stores an array of days to store the logs of past food consumption 
    dayList = []

    def add(self, inputDay):
        self.daylist.append(inputDay)

    def get(self, dayNum):
        return self.dayList[dayNum]