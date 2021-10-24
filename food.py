from database import *
class Food:
    name = ""
    
    mass, cal, prot, fat, carb = 0

    def __init__(self, in1, in2):
        self.name = in1
        self.mass = in2
        self.cal = database.getCal(database.getID(self.name), self.mass)
        self.prot = database.getProtein(database.getID(self.name), self.mass)
        self.fat = database.getFat(database.getID(self.name), self.mass)
        self.carb = database.getCarbs(database.getID(self.name), self.mass)

    def toString(self):
        return self.name + "\n" + str(self.mass) + "\n" + database.getNutrition(database.getID(self.name), self.mass)

    