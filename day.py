class Day():
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []

    def add(self, food, cal, protein, fat, carbs):
        self.foods.append(food)
        self.totalCal += cal
        self.totalProtein += protein
        self.totalFat += fat
        self.totalCarbs += carbs
    
    
    def getDayTotals(self):
        return "Calories: " + self.totalCal + "\n" + "Protein: " + self.totalProtein + "\n" + "Fat: " + self.totalFat + "\n Carbohydrates: " + self.totalCarbs + "\n"

