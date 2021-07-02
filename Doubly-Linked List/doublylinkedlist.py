class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if Doubly Linked List is empty
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None


    def prepend(self, data):
        new_node = Node(data)

        # Prepend onto an empty list
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_node(self):
        pass

    def delete_node(self):
        pass

    def reverse(self):
        pass

    def remove_dupe(self):
        pass
    
doublyLinkedList = DoublyLinkedList()
doublyLinkedList.prepend("0")
doublyLinkedList.append("A")
doublyLinkedList.append("B")
doublyLinkedList.append("C")
doublyLinkedList.prepend("5")
doublyLinkedList.print()