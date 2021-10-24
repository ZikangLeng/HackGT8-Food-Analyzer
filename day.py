from food import *
class Day():
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []

    def add(self, foodname):
        self.foods.append(foodname)
        self.totalCal += foodname.cal
        self.totalProtein += foodname.prot
        self.totalFat += foodname.fat
        self.totalCarbs += foodname.carb
    def getDayFacts(self):
        return "Total Cal " + str(round(self.totalCal,2)) + " kCal Total Protein  " + str(round(self.totalProtein,2)) + " g Total Fat " + str(round(self.totalFat,2)) + " g Total Carbs " + str(round(self.totalCarbs,2)) + " g"


