filename = "moby.txt"
file = open(filename, "r")
letters ={}
words =file.read()
words = words.replace("\n", " ")
for word in words.split(): 
    word = word.lower()
    letters[word]= letters.get(word, 0) + 1
sorted = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))       
print(sorted)
