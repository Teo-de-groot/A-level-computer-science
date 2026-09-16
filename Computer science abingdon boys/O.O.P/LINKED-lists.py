class Node:
    def __innit__(self,data,next_node):
        self.data = data 
        self.next_node = next_node

    def get_data(self):
        return self.data
    def set_next_node(self,next_node):
        self.next_node = next_node

class Stack:
    def __innit__(self, head ):
        pass 