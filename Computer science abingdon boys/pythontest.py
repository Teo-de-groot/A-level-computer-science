#word1 = input("What word would you like to check is in another word: ")
#word2 = input("What word would you like to check if it contains another Word: ")
#letters1=[]
#letters2=[]
#count=0
#for letter in word1:
#    letters1.append(letter)
#for letter in word2:
#    letters2.append(letter)
#for term in letters1:
#    if term in letters2:
#        count+=1
#if count == len(letters1):
#    print("true")
#else:
#    print("false")
x = int(input("Enter an integer greater than 1: ")) 
Product =1
Factor = 0
while Product < x:
    Factor = Factor + 1
    Product = Product * Factor
if x == Product:
    Product = 1
    for n in range(1,Factor+1):
        Product = Product * n
        print(n)
else:
    print("no result")