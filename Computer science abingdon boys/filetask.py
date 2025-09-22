filename = "book.txt"
file = open(filename, "r")
letters ={}
for word in file:
    for char in word: 
        test = char.isalpha()
        if test == True:
           letters[char]= letters.get(char, 0) + 1
sorted = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))       
print(sorted)
