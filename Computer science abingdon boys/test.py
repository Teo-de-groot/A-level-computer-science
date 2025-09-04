import random
#green
#print("\U0001F7E9")
#red
#print("\U0001F7E5")
Answer=[]
Attempt=[]
result=[]
correct=False
win_condition=0
colour_easy=["red","green","blue","orange","yellow"]
difficulty=input("what difficulty")
difficulty =difficulty.lower()
if difficulty == "easy":
    for i in range (0,5):
     x = random.randint(0,4)
     Answer.append(colour_easy[x])
    while correct!=True:
        for i in range (0,5):
            guess=input("colour guess? ")
            guess=guess.lower()
            Attempt.append(guess)
            if Answer[i]==Attempt[i]:
                result.append("\U0001F7E9")
                win_condition = win_condition+1
            else:
                result.append("\U0001F7E5")
        print(result)
        Attempt=[]
        result=[]
        if win_condition==5:
            correct= True
        else:
            win_condition=0
    
print("You win!")


        
            