import csv,sys

class database:
    
    def getID (keyword):
        FoodFile = csv.reader(open('food.csv', "r"), delimiter= ',')
        #searches database for foods with exact matching name
        for data in FoodFile:
            id = data[0]
            name = data[2].split(",")[0].strip().lower()
            if name == keyword.lower():
                return id
        #searches database for food names that contains the keyword
        for data in FoodFile:
            id = data[0]
            name = data[2]
            if name.__contains__(keyword):
                return id
        #if not found return 00000
        return "00000"

    def getNutrition(id, mass):
        output = []
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        NutritionIDFile = csv.reader(open("nutrient.csv", "r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id:
                if row[2] == '1003':
                    output.append("Protein: " + str(round(float(row[3])*mass/100,2))+ " g")
                elif row[2] == '1004':
                    output.append("Fat: " + str(round(float(row[3])*mass/100,2)) + " g")
                elif row[2] == '1005':
                    output.append("Carbs: " + str(round(float(row[3])*mass/100,2)) + " g")
                elif row[2] == "1008":
                    output.append("Calories: " + str(round(float(row[3])*mass/100,2)) + " kCal")
        outputStr = ""
        for nutrient in output:
            outputStr = outputStr + str(nutrient) + "\n"
        return outputStr 
        
    def getProtein(id,mass):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id and row[2] == '1003':
                return round(float(row[3])*mass/100,2)
        return 0

    def getFat(id,mass):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id and row[2] == '1004':
                return round(float(row[3])*mass/100,2)
        return 0
    def getCarbs(id,mass):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id and row[2] == '1005':
                return round(float(row[3])*mass/100,2)
        return 0
    def getCal(id,mass):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id and row[2] == '1008':
                return round(float(row[3])*mass/100,2)
        return 0

        
print(database.getNutrition(database.getID("apple"),200))
