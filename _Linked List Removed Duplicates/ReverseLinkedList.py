class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def print(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # This time using recursive
    def length(self,linkedList):
        if linkedList is None:
            return 0
        return 1 + self.length(linkedList.next)

    def remove_duplicates(self):
        current_node = self.head
        prev = None
        duplicate_values = dict()

        while current_node:
            if current_node.data in duplicate_values:
                prev.next = current_node.next
                current_node = None
            else:
                # Have not encountered element before
                duplicate_values[current_node.data] = 1
                prev = current_node
            current_node = prev.next
            

linkedList = LinkedList()
linkedList.append("A")
linkedList.append("B")
linkedList.append("B")
linkedList.append("C")
linkedList.print()
print(linkedList.length(linkedList.head))
linkedList.remove_duplicates()
linkedList.print()