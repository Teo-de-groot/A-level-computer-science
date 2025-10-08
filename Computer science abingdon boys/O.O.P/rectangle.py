import math

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getarea(self):
        return self.width*self.height
    def getpermiter(self):
        return 2*(self.width+self.height)
    def getdiagonal(self):
        return math.sqrt(self.width**2+self.height**2)
a = rectangle(4,3)
print(a.getarea())
print(a.getpermiter())
print(a.getdiagonal())
    