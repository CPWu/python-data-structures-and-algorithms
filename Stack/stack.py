class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        # Returns a boolean value representing empty or non-empty queue.
        return self.items == []

    def push(self,item):
        # Adds object at the end of the stack.
        self.items.append(item)

    def pop(self):
        # Removes the last object that added to stack.
        return self.items.pop()

    def peek(self):
        # Returns the last object added to stack unmodified.
        return self.items[len(self.items)-1]

    def size(self):
        # Returns the length of the stack.
        return len(self.items)

# Testing

# Instantiate a Stack
s = Stack()

# Verify that the Stack is empty
print (s.isEmpty())

# Add two items to the Stack.
s.push(1)
s.push('two')

# Peek into the last object added to Stack.
print(s.peek())

# Add another item into the Stack
s.push(True)

# Check the length of the stack
print(s.size())

# Check if Stack is empty.
print(s.isEmpty())

# Remove last item added to stack.
print(s.pop())
