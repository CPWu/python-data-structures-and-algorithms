class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        # Empty Linked List
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head
        
        if self.head is None:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def remove(self, node):
        if self.head == node:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            current_node = self.head
            prev = None
            while current_node.next != self.head:
                prev = current_node
                current_node = current_node.next
                if current_node == node:
                    prev.next = current_node.next
                    current_node = current_node.next

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def josephus_circile(self, step):
        current_node = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                current_node = current_node.next
                count += 1
                print("REMOVED: " + str(current_node.data))
            self.remove(current_node)
            current_node = current_node.next

circularLinkedList = CircularLinkedList()
circularLinkedList.append("1")
circularLinkedList.append("2")
circularLinkedList.append("3")
circularLinkedList.append("4")

circularLinkedList.josephus_circile(2)
circularLinkedList.print()


