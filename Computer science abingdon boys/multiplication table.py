multiply=input("What times table would you like to veiw: ")
test =multiply.isnumeric() 
while test != True:
    multiply=input("Input was not Valid. What times table would you like to veiw: ")
    test =multiply.isnumeric() 
Multiple =input("How many Values would you like to see: ")
test =Multiple.isnumeric() 
while test != True:
    Multiple =input("How many Values would you like to see: ")
    test =Multiple.isnumeric() 
Multiple = int(Multiple)
multiply = int(multiply)
Multiple = Multiple+1 
for i in range(1,Multiple):
    final = i * multiply
    print(str(i)+"x"+str(multiply)+"="+str(final))
