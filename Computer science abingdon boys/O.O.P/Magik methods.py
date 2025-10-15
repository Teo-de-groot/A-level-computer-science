class Thing:
    def __init__(self):
        self.x = 10

    
    def __str__ (self):
            return "a Thing"
    
    def __repr__(self):
         return "nuh uh"
thing = Thing()
lists = [thing]
print(lists)