class Queue():
    def __init__(self):
        # Creates an empty queue.
        self.items = []

    def isEmpty(self):
        # Returns a boolean value representing empty or non-empty queue.
        return self.items == []

    def enqueue(self,item):
        # Use Python Lists' insert method to insert the item at the head of the list otherwise known as enqueue in a Queue.
        self.items.insert(0,item)
    
    def dequeue(self):
        # Returns the object with the first item popped off.
        return self.items.pop()

    def size(self):
        # Returns the length of the Queue.
        return len(self.items)

    
# Testing

# Instantiate a Queue
q = Queue()

# Print initial size of the Queue.
print(q.size())

# Ensure Queue is empty
print(q.isEmpty())

# # Add some items to the Queue
q.enqueue(1)
q.enqueue(2)

# Output what is removed if we dequeue
print(q.dequeue())

