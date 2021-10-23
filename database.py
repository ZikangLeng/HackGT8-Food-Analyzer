import csv,sys

class database:
    
    def getID (keyword):
        FoodFile = csv.reader(open('food.csv', "r"), delimiter= ',')
        for data in FoodFile:
            id = data[0]
            name = data[2]
            if name.__contains__(keyword):
                return id

    def getNutrition(id, mass):
        output = []
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        NutritionIDFile = csv.reader(open("nutrient.csv", "r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id:
                if row[2] == '1003':
                    output.append("Protein: " + str(float(row[3])*mass/100) + " g")
                elif row[2] == '1004':
                    output.append("Fat: " + str(float(row[3])*mass/100) + " g")
                elif row[2] == '1005':
                    output.append("Carbs: " + str(float(row[3])*mass/100) + " g")
        
        outputStr = ""
        for nutrient in output:
            outputStr = outputStr + str(nutrient) + "\n"
        return outputStr 
                
    def getCal(id):
        NutritionFile = csv.reader(open("food_nutrient.csv","r"), delimiter= ',')
        for row in NutritionFile:
            if row[1] == id and row[2] == "1008":
                return row[2]
                
print(database.getNutrition(database.getID("Milk"), 300))



