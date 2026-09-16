class Thing:
    def __init__(self):
        self.x = 10

    
    def __str__ (self):
            return "a Thing"
    
    def __repr__(self):
         return "nuh uh"
thing = Thing()
lists = [thing]

#print(lists)
#
#def intput(var):
#   return int(input(var))
#ISBN = []
#for count in range(13):
#    digit = intput("Please enter next digit of ISBN: ")
#     ISBN.append(digit)
#count = 0
#CalculatedDigit = 0
#while count<12:
#   CalculatedDigit +=ISBN[count]
#   count +=1
#   CalculatedDigit +=ISBN[count]*3
#   count+=1
#while CalculatedDigit>= 10:
#    CalculatedDigit -= 10
#CalculatedDigit = 10 - CalculatedDigit
#if CalculatedDigit == 10: CalculatedDigit = 0
#if CalculatedDigit == ISBN[12]: print("Valid ISBN")
#else: print("Invalid ISBN")
#9, 7, 8, 1, 8, 5, 7, 0, 2, 8, 8, 9, 4