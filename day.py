class Day():
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []

    def add(self, foodname, cal, protein, fat, carbs):
        self.foods.append(foodname)
        self.totalCal += foodname.cal
        self.totalProtein += foodname.prot
        self.totalFat += foodname.fat
        self.totalCarbs += foodname.carb



testFood = Food("milk", 200)
print(testFood.toString())
test = Day()
test.add(testFood)
# print(test.getDayFacts())
