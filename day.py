from food import *
class Day():
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []
    def getDayFacts(self):
        return "Total Calories: " + str(self.totalCal)  + " kCal Total Protein: " + str(self.totalProtein)  + " g Total Fat: " + str(self.totalFat) + " g Total Carbohydrates: " + str(self.totalCarbs) + " g"

    def add(self, foodname):
        self.foods.append(foodname)
        self.totalCal += foodname.cal
        self.totalProtein += foodname.prot
        self.totalFat += foodname.fat
        self.totalCarbs += foodname.carb


    
    
testFood = Food("milk", 200)
test = Day()
test.add(testFood)
print(test.getDayFacts())
