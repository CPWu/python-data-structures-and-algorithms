# Time O(N), Space O(1)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(headNode):
    currentNode = headNode
    previous = None
    next = None

    while currentNode:
        next = currentNode.next
        currentNode.next = previous
        previous = currentNode
        currentNode = next

    return previous

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next = b
b.next = c
c.next = d

print(a.value)
print(a.next.value)
print(b.next.value)
print(c.next.value)

print("\n")
reverseLinkedList(a)


print(b.next.value)
print(c.next.value)
print(d.next.value)
print(d.value)