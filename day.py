class Day:
    totalCal=0
    totalProtein = 0
    totalFat = 0
    totalCarbs = 0
    foods = []

    def add(name, cal, protein, fat, carbs,self, foods):
        self.foods.append(name)


test = Day()    
test.add("bruh", 1,2,3,4)
