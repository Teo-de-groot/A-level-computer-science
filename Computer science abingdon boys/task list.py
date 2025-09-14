Tasks = []
continues = True
def Add_task():
    """Adds tasks untill no is entered, then returns Tasks as a list"""
    while True:
        New_task = input("What task would you like to add: ")
        Tasks.append(New_task)
        Continues=input("Would you like to continue: (yes/no)")
        Continues = Continues.lower()
        if Continues == "yes":
            pass
        else:
            return Tasks

        

def menu(list):
    while True:
        option = input(""" ----Options----
                   1. Add a task
                   2. show task
                   3. next task 
                   4. complete task
                   5. Quit
                    : """)
        while not option.isnumeric():
            print("Invalid choice Please enter a Number: ")
            option = input(""" ----Options----
                   1. Add a task
                   2. show task
                   3. next task 
                   4. complete task
                   5. Quit
                    : """)
        option = int(option)
        if option >5 or option < 1:
            print("Invalid option please enter a number 1-4")
        elif option =="1":
                Tasks = Add_task()
                return Tasks
        elif option =="2":
            print(list)
        elif option =="3":
            if Tasks:
                print(Tasks[0])
            else:
                print("no current Tasks")
        elif option == "4":
            if Tasks:
                del Tasks[0]
            else:
                print("no current tasks")
        else:
            quit()
while continues == True:
    Tasks = menu(Tasks)