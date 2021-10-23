import csv,sys

class database:
    
    def getID (keyword):
        FoodFile = csv.reader(open('food.csv', "r"), delimiter= ',')
        for data in FoodFile:
            id = data[0]
            name = data[2]
            if name.__contains__(keyword):
                return id

    def getNutrition(id):
        output = []
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        NutritionIDFile = csv.reader(open("nutrient.csv", "r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] is id:
                if row[2] is '1003':
                    output.append("Protein: " + row[3] + " G")
                elif row[2] is '1004':
                    output.append("Fat: " + row[3] + " G")
                elif row[2] is '1005':
                    output.append("Carbs: " + row[3] + " G")
        outputStr = str
        for nutrient in output:
            outputStr = outputStr + nutrient + "/n"
            return outputStr 
                
    def getCal(id):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] is id and row[2] is "1008":
                return row[2]
                
print(database.getNutrition(database.getID("Milk")))



