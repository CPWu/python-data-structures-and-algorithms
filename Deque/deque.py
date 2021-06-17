class Deque():
    def __init__(self):
            # Creates an empty deque
        self.items = []
    
    def isEmpty(self):
        # Returns a boolean value representing empty or non-empty deque.    
        return self.items == []

    def addFront(self,item):
        # Use Python Lists' append method to add an object at the tail of the deque
        self.items.append(item)

    def addRear(self,item):
        # Use Python Lists' insert method to add an object at the head of the deque
        self.items.insert(0, item)

    def removeFront(self):
        # Returns the object with the first object popped off.
        return self.items.pop()

    def removeRear(self):
        # Returns the object with the tail object popped off.
        return self.items.pop(0)

    def size(self):
        # Returns the length of the Deque.
        return len(self.items)
    
# Testing

# Instantiate a Queue
d = Deque()

# Print initial size of the Queue.
print(d.size())

# Ensure Deque is empty
print(d.isEmpty())

# Add some items to the Deque
d.addFront('Front')
d.addRear('Rear')

# Check Size
print(d.size())

# Print Front
print(d.removeFront())

# Print Front
print(d.removeFront())