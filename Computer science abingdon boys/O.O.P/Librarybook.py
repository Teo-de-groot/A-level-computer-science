class Librarybook:
    def __init__(self, book_name,author,INTB,date):
        self.__book_name = book_name
        self.__author = author
        self.__intb = INTB
        self.__date = date
        self.__on_loan = False
        
    def set_on_loan(self):
        self.__on_loan = True
    def book_identifcation(self):
        print(f"{self.__book_name}, {self.__author}, {self.__intb}, {self.__date}, {self.__on_loan}")
    def return_loan(self):
        self.__on_loan = False 
    def check_loan(self):
        return self.__on_loan
caterpillar = Librarybook("The Very Hungry Caterpillar", "Eric Carle", "9780140569322", "06/11/89")
caterpillar.book_identifcation()
if caterpillar.check_loan() == False: print("Test passed")
caterpillar.set_on_loan() 
if caterpillar.check_loan() == True: print("Test passed")
caterpillar.return_loan()
if caterpillar.check_loan() == False: print("Test passed")