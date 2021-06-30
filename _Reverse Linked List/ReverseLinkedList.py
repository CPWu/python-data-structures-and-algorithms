class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        # If Linked List is Empty
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Can be done recursively but choosing to do it iteratively for this demo
    def length(self):
        nodeCount = 0
        current_node = self.head

        while current_node.next:
            nodeCount += 1
            current_node = current_node.next
        return nodeCount

    def insert(self, prev, data):
        if not prev:
            print("Previous node not in the linked list.")
            return
        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node

    def reverse(self):
        # Create a variable that the last node will pont to.
        prev = None
        
        currentNode = self.head
        while currentNode:
            # Temporary variable to hold the pointer to the next node as we are reversing it
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev
# Test Linked List Here:       
linkedList = LinkedList()
linkedList.append("A")
linkedList.append("B")
linkedList.append("C")
linkedList.append("D")
linkedList.print()
print("Reversed")
linkedList.reverse()
linkedList.print()
# print(linkedList.length())