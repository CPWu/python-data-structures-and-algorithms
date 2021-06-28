# Node Class
class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

# Instantiate 3 Instances of Node
a = Node(1)
b = Node(2)
c = Node(3)

# Set the 'pointers' of the nodes
a.nextNode = b
b.nextNode = c

# Print value of Node a
print(a.value)

# Print the value of the node that node 'a' is pointing to
print(a.nextNode.value)