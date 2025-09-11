name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
third = name_list[2]
print("The third name is: ", third)
length = len(name_list)
print("The last names are",name_list[-7:])

numb=[]
repeats = int(input("How many numbers would you like to Enter? "))
for i in range(repeats):
    temp = int(input("Enter a number: "))
    numb.append(temp)
print("\n"* 3)
print("--- Results ---")
print("\n")
print("The numbers you entered are:", numb)
print("The Smallest number is: ",min(numb))
print("The Largest number is: ",max(numb))
print("The sum of all the numbers is: ",sum(numb))
mean = sum(numb) / len(numb)
print(mean)
    
    