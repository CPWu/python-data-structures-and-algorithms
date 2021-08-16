class Stack(object):
    def __init__(self):
    # Instantiate the Stack with a Python List
        self.items = []

    # Adds object at the end of the stack.  
    def push(self, item):
        self.items.append(item)

    def pop(self):
        # Removes the last object that added to stack.
        self.items.pop()
    
    def peek(self):
        # Returns the last object added to stack unmodified.
        return self.items[len(self.items)-1]

    def size(self):
        # Returns the length of the stack.
        return len(self.items)

    def is_empty(self):
        # Returns a boolean value representing empty or non-empty queue.
        return self.items == []