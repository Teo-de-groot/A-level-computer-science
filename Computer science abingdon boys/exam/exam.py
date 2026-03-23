num = int(input("Please enter An integer (0-99)"))
op = input("Calculate additive or multiplicative persistacne (a or m)")
count= 0
while num > 9:
    if op == "a":
        num = (num//10)+(num%10)
    else:
        num = (num//10)*(num%10)

        
    count += 1
print(f"the persicstance is: {count}")
