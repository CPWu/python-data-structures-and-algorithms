# # Node Class
# class Node(object):
#     def __init__(self,value):
#         self.value = value
#         self.nextNode = None

# # Instantiate 3 Instances of Node
# a = Node(1)
# b = Node(2)
# c = Node(3)

# # Set the 'pointers' of the nodes
# a.nextNode = b
# b.nextNode = c

# # Print value of Node a
# print(a.value)

# # Print the value of the node that node 'a' is pointing to
# print(a.nextNode.value)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        # If Linked List is empty
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        # While loops continues until last_node.next equals null
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
    def insert(self, prev, data):
        
        if not prev:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node
    
    def len_iterative(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def delete_data(self, data):
        current_node = self.head
        
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def delete_pos(self, position):
        current_node = self.head

        if position == 0:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        count = 1
        while current_node and count != position:
            prev = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            return
        
        prev.next = current_node.next
        current_node = None

    def swap_nodes(self, dataOne, dataTwo):
        if dataOne == dataTwo:
            return
        
        prevOne = None
        currentOne = self.head

        while currentOne and currentOne.data != dataOne:
            prevOne = currentOne
            currentOne = currentOne.next

        prevTwo = None
        currentTwo = self.head

        while currentTwo and currentTwo. data != dataTwo:
            prevTwo = currentTwo
            currentTwo = currentTwo.next

        if not currentOne or not currentTwo:
            return 

        if prevOne:
            prevOne.next = currentTwo
        else:
            self.head = currentTwo
        
        if prevTwo:
            prevTwo.next = currentOne
        else:
            self.head = currentOne

        currentOne.next, currentTwo.next = currentTwo.next, currentOne.next

    def reverse_iterative(self):
        prev = None
        currentNode = self.head
        while currentNode:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(currentNode, prev):
            if not currentNode:
                return prev
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
            return _reverse_recursive(currentNode,prev)

        self.head = _reverse_recursive(currentNode=self.head, prev=None)


# Instantiate Linked List 
linkedList = LinkedList()

# Add a few nodes
linkedList.append("A")
# linkedList.append("B")
# linkedList.append("C")
# linkedList.append("D")

# # Insert a node into linked list
# linkedList.insert(linkedList.head.next, "Z")

# Prints the contents of the linked list
linkedList.print_list()

# Two ways to find the length of a linked list (iterative, recursive)
# print(linkedList.len_iterative())
# print(linkedList.len_recursive(linkedList.head))

# # Deleting a Node by specific value
# linkedList.delete_data("Z")

# linkedList.print_list()

# # Deleting a Node by specific value
# linkedList.delete_pos(3)

# linkedList.print_list()

# # Deleting a Node by specific value
# linkedList.swap_nodes("A","C")

# linkedList.print_list()

# # Reverse Linked List (Iterative)
# linkedList.reverse_iterative()
# linkedList.print_list()

# Reverse Linked List (Recursive)
# linkedList.reverse_recursive()
# linkedList.print_list()


