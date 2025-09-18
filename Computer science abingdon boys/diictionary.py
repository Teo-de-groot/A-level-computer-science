sounds = {"cat" : "meow", "dog" : "woof" }
print(sounds)
print(sounds["cat"])
print(sounds["dog"])
print(sounds.get("penguin","woof"))
test = {"lengyu" : 68}
test["lengyu"]= test.get("lengyu", 0) + 1
test["notlengyu"]= test.get("notlengyu", 0) + 1
print(test)