usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber: str):
    
    if usernumber.isnumeric() == True:
         print("\n -- The Basic Version --\n")
         number = int(usernumber)
         print("Welcome", usernames[number], "user number", number,".")
         if number != 0:
            division = 301 / number
            print(f"301 divided by {number} = {division}")
         else: 
            print("301 not divisible by 0")
    else:
        print("Input not a Number please enter your user number")

while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)
