
class Day():
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []

    def add(self, foodname, cal, protein, fat, carbs):
        self.foods.append(foodname)
        self.totalCal += cal
        self.totalProtein += protein
        self.totalFat += fat
        self.totalCarbs += carbs
    
    def getDayFacts(self):
        return totalCal + 

