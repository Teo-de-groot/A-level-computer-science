vowels = ['a', 'e', 'i', 'o', 'u']
index = []
word = list(input("Enter a word: "))
for i in range(len(word)):
    if word[i].lower() in vowels:
        index.append(int(i))


for i in range(len(index) // 2):
    length = len(index)
    temp = word[index[i]]  
    word[index[i]] = word[index[length - 1 - i]] 
    word[index[length - 1 -i]] = temp

print("".join(word))