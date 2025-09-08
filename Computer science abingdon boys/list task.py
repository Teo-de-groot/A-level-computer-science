name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
third = name_list[2]
print("The third name is: ", third)
length = len(name_list)
for i in range (1,8):
    print(name_list[-i])

numb=[]
for i in range(5):
    temp = int(input("Enter a number: "))
    numb.append(temp)
print(min(numb))
print(max(numb))
print(sum(numb))
mean = sum(numb)
mean1= len(numb)
mean = mean / mean1
print(mean)
    
    