class Wagon:
    def __init__(self,name):
        self.name = name 

    def __str__(self):
        return f"<Wagon: {self.name}>"

class OpenWagon(Wagon):
    def __init__(self,name):
        super().__init__(name)
        pass

class ClosedWagon(Wagon):
    def __init__(self,name):
        super().__init__(name)
        pass

class Siding:
    def __init__(self):
        self._top_of_stack =-1
        self._wagon_array = [None] * 30

    def push_wagon(self, wagon):
        if self._top_of_stack != (len(self._wagon_array)-1):
            self._wagon = wagon
            self._top_of_stack+=1
            self._wagon_array[self._top_of_stack] = self._wagon
        else:
            return f"Siding full cannot add {self._wagon}"
          
    def pop_wagon(self):
        if self._top_of_stack != -1:
            self._wagon_exiting = self._wagon_array[self._top_of_stack]
            self._wagon_array[self._top_of_stack] = None
            self._top_of_stack -= 1
            return self._wagon_exiting
        else:
            return "Siding empty"

def testing():
    wagon1 = OpenWagon("jeramiah")
    wagon2 = ClosedWagon("joseppi spagetti")
    wagon3= Wagon("thomas whyte the tank engine")

    john = Siding()    
    john.push_wagon(wagon1)
    john.push_wagon(wagon2)
    john.push_wagon(wagon3)
    print(john.pop_wagon())
    print(john.pop_wagon())

testing()