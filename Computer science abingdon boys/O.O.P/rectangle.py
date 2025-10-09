class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        """Times The Two Values Together"""
        return self.width*self.height
    
    def getpermiter(self):
        """Doubles The Sum Of The Two Entered Values"""
        return 2*(self.width+self.height)
    
    def getdiagonal(self):
        """Does Pythagarean Theorum To Get Diagonal Length Of A Rectange"""
        return (self.width**2+self.height**2)**0.5
    
a = Rectangle(4,3)
if a.getarea() == 12:
    pass 
else:
    print("FAILED")
if a.getpermiter() == 14:
    pass 
else:
    print("FAILED")
if a.getdiagonal() == 5.0:
    pass 
else:
    print("FAILED")
