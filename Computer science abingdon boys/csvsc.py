import csv 
names= ["a","B","c"]
numbs = [1,2,3]
age = [10,20,"megaknight"]
with open("hello.csv") as csv:
    for i in range(3):
        csv.write(names[i], ",", numbs[i], "," , age[i], ".")
        