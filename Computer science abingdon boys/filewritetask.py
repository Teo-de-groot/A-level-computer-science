def writefile(filename):
    with open(filename, "a") as file:
        while True:
            line = input("what would you like to write? ")
            file.write(line)
            file.write("\n")
            continues=input("would you like to continue (yes/no)")
            if continues == "no":
             break
def readfile(filename):
    file = open(filename, "r")
    file =file.read()
    print(file)

writefile("write.txt")
readfile("write.txt")