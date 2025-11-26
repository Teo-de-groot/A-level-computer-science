import math
class Vector2D:
    def __init__(self, x, y):
        self.x =x
        self.y=y
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    

    def __add__(self, second):
        return self.x + second.x, self.y + second.y
    
    def get_angle(self):
        return math.degrees(math.atan(self.x/self.y))
    def __rmul__(self, num):
         return Vector2D(num*self.x,num*self.y)
    def __mul__(self, scalar):
        return Vector2D(scalar*self.x,scalar*self.y)
    def __invert__(self):
        return Vector2D(self.y,self.x)
    


def testvec():
    vector1 = Vector2D(3,4)
    vector2 = Vector2D(4,6)
    a = vector1+vector2 
    if a == (7, 10):
        print("Passed")
    else:
        print("Failed")
testvec()
vec1 = Vector2D(3,4)
print(vec1.get_angle())
print(Vector2D(6,7))

class VectorND:
    def __init__(self, *arguments):
        self.arguments = arguments
        self.dimensions = len(self.arguments)
    def lendimension(self):
        return self.dimensions
    
    