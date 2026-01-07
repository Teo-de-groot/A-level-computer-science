import random 
class Board:
    def __init__(self):
        self.data = [" "]*9
        self.boardcheck = ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]
    def checkcoord(self):
        """ Shows the Coordidinates of the Board with any changed markers e.g X or O"""
        print(" | ".join(self.boardcheck[0:3]))
        print("---------------")
        print(" | ".join(self.boardcheck[3:6]))
        print("---------------")
        print(" | ".join(self.boardcheck[6:9]))
        print()
    def checkdraw(self, win):
        c=0
        for i in range(0,9):
            posibilites = ["X","O"]
            if self.data[i] in posibilites:
                c+=1
            if c ==9 and win ==False:
                return True   
        return False
    def display(self):
        """ Shows the current board with any changed markers e.g X or O"""
        print(" | ".join(self.data[0:3]))
        print("---------")
        print(" | ".join(self.data[3:6]))
        print("---------")
        print(" | ".join(self.data[6:9]))
        print()
    def checkrow(self):
        """iterates through every row in the array 
        returns True if Win is found else returns False, 
        slow may replace later with numpy"""
        if ''.join(self.data[0:3])  == "X"*3 or ''.join(self.data[0:3]) == "O"*3:
            return True
        elif ''.join(self.data[3:6])  == "X"*3 or ''.join(self.data[3:6]) == "O"*3:
            return True
        elif ''.join(self.data[6:9])  == "X"*3 or ''.join(self.data[6:9]) == "O"*3:
            return True
        else:
            return False  
    def checkcol(self):
        """iterates through every collum in the array 
        returns True if Win is found else returns False, 
        slow may replace later with numpy"""
        for i in range(0,3):
            arr = [self.data[i],self.data[i+3],self.data[i+6]]
            if ''.join(arr) == "X"*3 or ''.join(arr) == "O"*3:
                return True
        return False  
    def checkdiag(self):
        """iterates through every diagonal in the array 
        returns True if Win is found else returns False, 
        slow may replace later with numpy"""
        arr = self.data[0],self.data[4],self.data[8]
        if ''.join(arr) == "X"*3 or ''.join(arr) == "O"*3:
            return True
        arr = self.data[2],self.data[4],self.data[6]
        if ''.join(arr) == "X"*3 or ''.join(arr) == "O"*3:
            return True
        else:
            return False
    def checkwin(self):
        row = self.checkrow()
        col = self.checkcol()
        diag = self.checkdiag()
        if col == False and row == False and diag == False:
            return False
        else:
            return True
    def set_cell(self, x:int, y:int, marker):
        """ Updates the board with the marker specified, i.e. 'X' or 'O'.
        Returns True if successful. """
        if self.data[(x -1)*3 + (y-1)] == " ":
            self.data[(x -1)*3 + (y-1)] = marker
            self.boardcheck[(x -1)*3 + (y-1)] = marker
            return True
        else: 
            return False
player1 = input("Who is playing?")
win = False
board=Board()
test = False
while test == False:
    play = input("type 1 for play vs Ai type 2 for play vs Human: ")
    gamemodes =["1","2"]
    if play in gamemodes:
        test = True
if play == "1":
    while win == False: 
        print(f"{player1}'s turn")
        board.display() 
        coord_check = False
        while coord_check == False:
            coords = input("What coordinates would you like to place your marker at?(col,row)")
            if len(coords) ==3:
                xcoord = coords[0]
                ycoord = coords[2]
                cells = ["1", "2","3"]
                if xcoord in cells and ycoord in cells:
                    xcoord = int(xcoord)
                    ycoord = int(ycoord)
                    coord_check = board.set_cell(xcoord,ycoord,"X")
                else:
                    print("enter number 1-3 only")
            else:
                print("Please enter in format {row},{col}")
        winner =player1
        win = board.checkwin()
        draw = board.checkdraw(win)
        if draw == True:
            print("Draw no possible moves left")
            break
        board.display()
        if win == False:
            coord_check = False
            while coord_check == False:
                x =random.randint(1,3)
                y = random.randint(1,3)
                coord_check = board.set_cell(x,y,"O")
            winner ="AI"
            win = board.checkwin()
            draw = board.checkdraw(win)
            if draw == True:
                print("Draw no possible moves left")
                break
    print(f"player{winner} won the game")
if play == "2":
    player2 =input("who is player 2: ")
    while win == False: 
        board.checkcoord()
        print(f"{player1}'s turn")
        board.display() 
        coord_check = False
        while coord_check == False:
            coords = input("What coordinates would you like to place your marker at?(col,row)")
            if len(coords) ==3:
                xcoord = coords[0]
                ycoord = coords[2]
                cells = ["1", "2","3"]
                if xcoord in cells and ycoord in cells:
                    xcoord = int(xcoord)
                    ycoord = int(ycoord)
                    coord_check = board.set_cell(xcoord,ycoord,"X")
                else:
                    print("enter number 1-3 only")
            else:
                print("Please enter in format {row},{col}")
        winner =player1
        win = board.checkwin()
        draw = board.checkdraw(win)
        if draw == True:
            print("Draw no possible moves left")
            break
        if win == False:
            print(f"{player2}'s turn")
            board.display() 
            coord_check = False
            while coord_check == False:
                coords = input("What coordinates would you like to place your marker at?(col,row)")
                if len(coords) ==3:
                    xcoord = coords[0]
                    ycoord = coords[2]
                    cells = ["1", "2","3"]
                    if xcoord in cells and ycoord in cells:
                        xcoord = int(xcoord)
                        ycoord = int(ycoord)
                        coord_check = board.set_cell(xcoord,ycoord,"O")
                    else:
                        print("enter number 1-3 only")
                else:
                    print("Please enter in format {row},{col}")
            winner =player2
            win = board.checkwin()
            draw = board.checkdraw(win)
            if draw == True:
                print("Draw no possible moves left")
                break
    if draw == False:
        print(f"player: {winner} won the game")