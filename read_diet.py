from day import*
Five_Day_Diet = open("Five Day Food Consumption.txt","r")
#Finds number of lines in text file
Line_Count = 0
File_Content = Five_Day_Diet.read()
Content_Per_Line = File_Content.split("\n")
for line in Content_Per_Line:
    Line_Count += 1
Five_Day_Diet.close()
#Finds the name of each food and its weight from text file
Five_Day_Diet = open("Five Day Food Consumption.txt","r")
All_Food_Names = []
All_Food_Weights = []
for x in range(10):
    File_Line = Five_Day_Diet.readline()
    Food_Name_List = []
    Food_Weight_List = []
    for y in File_Line:
        if y.isalpha() == True:
            Food_Name_List.append(y)
        elif y.isdigit() == True:
            Food_Weight_List.append(y)
    Food_Name = str("".join(Food_Name_List))
    Food_Weight = int("".join(Food_Weight_List))
    All_Food_Names.append(Food_Name)
    All_Food_Weights.append(Food_Weight)
Day_1 = Day()
Day_1.add