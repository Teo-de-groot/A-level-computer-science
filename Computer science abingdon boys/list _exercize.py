def intput(a):
    b = int(input(a))
    return(b)
def menu():
    print("What would you like to do ? ")
    print("     1. Add new score")
    print("     2. View all scores")
    print("     3. Exit")
    Menus=(input(""))
    while not Menus.isnumeric():
        print("Invalid character, please enter a number 1-3")
        Menus=input("")
    Menus= int(Menus)
    while Menus not in range (1,4):
        print("Invalid character, please enter a number 1-3")
        Menus=input("")
        Menus= int(Menus)
    return(Menus)

    
    
    

name_list =  ['Ryansh', 'Oliver', 'Edward', 'Daniel', 'Alex', 'Ares', 'Thomas', 'Andy', 'Charlie', 'Ryan', 'Lucas']
scores_list = [[] for i in name_list]           # Create a lists of empty lists

name = input("Enter name: ")                # Get the user to enter a name
continues = "yes"
while continues != "no":
    result = menu()
    if result ==2:
        print(scores_list)
    elif result ==1:
        name_index = name_list.index(name)          # Find out which index that name appears at
        new_score = int(input("Enter score: "))     # The user enters a new score for that person
        scores_list[name_index].append(new_score)   # Append the new score to the list in the relevant location within scores
        print("The average score is: ", sum(scores_list[name_index])/len(scores_list[name_index]))
    elif result == 3:
        continues = "no"
    total_score= 0
    number_of_scores = 0
    for individual_scoes in scores_list:     #sum(sum(scores_list, []))/len(sum(scores_list, [])) iterate though list of lists and flattens into one list that you can then just sum()/len()
        for score in individual_scoes:       #didnt come up with this solution myself so i didnt use it
            total_score += score
            number_of_scores += 1
    if number_of_scores > 0:
        print(f'Average total score: {total_score/number_of_scores}')
    else:
        pass
    continues = input("would you like to continue (yes/no)")
    continues = continues.lower()