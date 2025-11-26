class Stockitem:
    def __init__(self, Title,date):
        self.__title = Title
        self.__date = date
        self.__on_loan = False
        
    def set_on_loan(self):
        self.__on_loan = True
    def return_loan(self):
        self.__on_loan = False 
    def check_loan(self):
        return self.__on_loan
    

class Librarybook(Stockitem):
    def __init__(self,title,author,intb,date):
        super().__init__(title,date)
        self.__author = author
        self.__intb = intb

    def book_identifcation(self):
        print(f"{self.__title}, {self.__author}, {self.__intb}, {self.__date}, {self.__on_loan}")


class CD(Stockitem):
    def __init__(self, Artist, Playingtime, Title, date):
        self.__Artist = Artist
        self.__Playingtime = Playingtime
        super().__init__(Title, date)

    def cd_identifcation(self):
        print(f"{self.__title}, {self.__Artist}, {self.__Playingtime}, {self.__date}, {self.__on_loan}")


def unit_testing():
    book1 = Librarybook("The Very Hungry Caterpillar", "Eric Carle", "9780140569322", "06/11/1989")
    book2 = Librarybook("The tales of the ten rings", "Longyu Cheng", "6767676767670", "01/01/100000000000000BC")
    cd1 = CD("Rick Ashley","67 years ","Never Gonna Give You Up","01/01/0101")
    

