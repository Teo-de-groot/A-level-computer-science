class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def set_next(self, node):
        self._next_node = node 

    def get_next(self):
        return self._next_node

    def get_data(self):
        return self._data

class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        """ Allows the use of len(stack) to find the number of elements in the stack """
        return self._size

    def push(self, data):
        next_node = self._head_node
        new_node = Node(data, next_node)
        self._head_node = new_node
        self._size += 1
    def pop(self):
        data = self._head_node.get_data()
        new_head = self._head_node.get_next()
        self._head_node=new_head
        self._size-=1
        return data

    def peek(self):
        return self._head_node
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        """ Defines what should be displayed when the user prints a linked list object. """
        return self.data

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    # my_stack.append(4)

    print(my_stack, len(my_stack))

    while not my_stack.is_empty():
        print(my_stack.pop())
print(my_stack)