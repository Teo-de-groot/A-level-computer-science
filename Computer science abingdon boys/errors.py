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

def login_unhandled2(usernumber):
    print("\n -- The Basic Version --\n")
    try: 
        number = int(usernumber)
    except ValueError:
        return "not number T-T"
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        return
    try:
        division = 301 / number
    except ZeroDivisionError or TypeError:
        print("301 is not div by entered value")
        return ""
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)
    