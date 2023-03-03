myList=[57,43.36,"prasant",31.72,"sabir",95,"ajay",12,"Dinesh",28.32,51]
intList=[]
flotList =[]
stringList =[]
for i in myList:
    if type(i) == int:
        intList.append(i)
    
    if type(i) == float:
        flotList.append(i)
    if type(i) == str:
        stringList.append(i)
        
        
print(intList)
print(flotList)
print(stringList)   

        
