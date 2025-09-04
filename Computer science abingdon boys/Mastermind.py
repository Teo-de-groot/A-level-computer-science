import random
import csv
#green box for easy mode
#print("\U0001F7E9")
#red box for easy mode
#print("\U0001F7E5")


def is_valid_colour(colour, valid_colours):
    # Colour has been specified, check if valid
    if colour not in valid_colours or not colour:
        print(f"Colour choice is not valid, valid choices are: {", ".join(valid_colours)}")
        return False
    else:
        #Colour has been specified, and is valid
        return True
    
def read_high_score():
    scores = {}
    with open('leaderboard.csv', newline='') as csvfile:
        score_reader = csv.reader(csvfile, delimiter=',')
        for player, score in score_reader:
            scores[player] = score
    return scores

def write_high_score(player, score):
    #to add difficulty to leaderboard to allow highscore compatability with every difficuty
    scores = {}
    with open('leaderboard.csv', 'a', newline='') as csvfile:
        score_writer = csv.writer(csvfile, delimiter=',')
        score_writer.writerow([str(player), str(score)])

def low_score():
    scores = {}
    with open('leaderboard.csv', newline='') as csvfile:
        score_reader = csv.reader(csvfile, delimiter=',')
        for row in score_reader:
            if len(row) == 2:
                player, score = row
                scores[player] = int(score)
        if scores:
            #will only be called if high score is avalible
            min_score = min(scores.values())
        else:
            min_score = None
    return min_score

attempts=0
restart="yes"
Answer=[]
Attempt=[]
result=[]
correct=False
win_condition=0
current_difficulties=["easy","normal","hard"]
colour_easy=["red","green","blue","orange","yellow"]
colour_hard=["red","blue","yellow","green","indigo","orange","violet","white"]
print("Easy difficulty will triple attempts before adding to leaderboard.")
print("Normal difficulty will double attempts before adding to leaderboard.")
print("Hard difficulty will not change attempts before adding to leaderboard.")
print("A result will only be added to the leaderboard if it is a new highscore.")
while restart == "yes":
    attempts = 0
    Answer = []
    Attempts = []
    current_leader = low_score()
    if current_leader:
        print(f"Current Highscore: ",current_leader)
    else:
        print("No current highscore, Please enjoy the game.")
    difficulty=input("what difficulty? ")
    difficulty =difficulty.lower()
    while difficulty not in current_difficulties:
        if difficulty not in current_difficulties or not guess:
         print(f"Difficulty choice is not valid, valid choices are: {", ".join(current_difficulties)}")
         difficulty=input("what difficulty? ")
        difficulty =difficulty.lower()
    if difficulty == "easy":
        for i in range (0,4):
            x = random.randint(0,4)
            Answer.append(colour_easy[x])
        while correct!=True:
            for i in range (0,4):
                guess=input("colour guess? ")
                while not is_valid_colour(guess, colour_easy):
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
            if win_condition==4:
                print("You win!")
                attempts= attempts+1
                print(f"it took you",attempts,"attempts")
                attempts=attempts*3
                correct= True
            else:
                win_condition=0
                attempts= attempts+1
    elif difficulty == "normal":
        for i in range (0,5):
            x = random.randint(0,4)
            Answer.append(colour_easy[x])
        while correct!=True:
            for i in range (0,5):
                guess=input("colour guess? ")
                while not is_valid_colour(guess, colour_easy):
                    guess=input("colour guess? ")
                guess=guess.lower()
                Attempt.append(guess)
                if Answer[i]==Attempt[i]:
                    win_condition = win_condition+1
            if win_condition==5:
                print("You win!")
                attempts= attempts+1
                print("it took you"+ attempts+"attempts")
                attempts=attempts*2
                correct= True
            else:
                print(win_condition)
                win_condition=0
                attempts= attempts+1
                Attempt=[]
    elif difficulty == "hard":
        for i in range (0,6):
            x = random.randint(0,7)
            Answer.append(colour_hard[x])
        while correct!=True:
            for i in range (0,6):
                guess=input("colour guess? ")
                while not is_valid_colour(guess, colour_easy):
                    guess=input("colour guess? ")
                guess=guess.lower()
                if Answer[i]==Attempt[i]:
                    win_condition = win_condition+1
                else:
                    pass
            if win_condition==6:
                print("You win!")
                attempts= attempts+1
                print("it took you"+ attempts+"attempts")
                correct= True
            else:
                print(win_condition)
                attempts= attempts+1
                win_condition=0
                Attempt=[]
    score_to_beat =low_score()
    if score_to_beat:
        if attempts < score_to_beat: #ensures there is a score so no incompatability occurs
            print("New highscore!")
            name=input("What name would you like to use on the leaderboard? ")
            attempts=str(attempts)
            write_high_score(name, attempts)
    else:
        #adds any result to leaderboard if game hasnt been played yet
        print("New highscore!")
        name=input("What name would you like to use on the leaderboard? ")
        write_high_score(name, str(attempts))
    continues=input("Do you want to play again? ")
    replay=continues.lower()
    if replay=="yes":
        correct=False
        win_condition=0
    restart=replay