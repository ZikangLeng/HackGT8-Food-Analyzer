import csv

FoodFile = csv.reader(open('food.csv', "r"), delimiter= ',')
DictR = open("FoodList.dict", "r")
Dict = open("FoodList.dict", "w")
for entry in FoodFile:
    name = entry[2].split(",")[0].strip().lower()
    alrExists = False
    for existing in DictR:
        
        if name == existing.strip():
            alrExists = True
            
    
    if not alrExists:
        Dict.write(name + "\n")


DictR2 = open("FoodList.dict", "r")
DictW2 = open("FList.dict", "w")
arr = []
arr2 = []
for food in DictR2:
    arr.append(food)
    print("test")
for x in range(arr.__len__()-2):
    if arr[x+1] != arr[x+2]:
        arr2.append(arr[x])
for y in arr2:
    DictW2.write(y)
        


