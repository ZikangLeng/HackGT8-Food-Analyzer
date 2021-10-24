from database import *
class Food:
    name = ""
    
    mass =0
    cal =0
    prot=0
    fat=0
    carb = 0

    def __init__(self, in1, in2):
        self.name = in1
        self.mass = in2
        self.cal = database.getCal(database.getID(self.name), self.mass)
        self.prot = database.getProtein(database.getID(self.name), self.mass)
        self.fat = database.getFat(database.getID(self.name), self.mass)
        self.carb = database.getCarbs(database.getID(self.name), self.mass)

    def toString(self):
        return self.name + " Mass: " + str(self.mass) + " g kCal " + str(self.cal) + " g Protein  " + str(self.prot) + " g Fat " + str(self.fat) + " g Carbs " + str(self.carb) + " g"

    