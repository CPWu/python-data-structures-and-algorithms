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

    def add_after_node(self, key, data):
        current_node = self.head

        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next = current_node.next
                current_node.next = new_node
                new_node.next = next
                new_node.prev = current_node
                next.prev = new_node
            current_node = current_node.next
    def add_before_node(self, key, data):
        current_node = self.head

        while current_node:
            if current_node.prev is None and current_node.data == key:
                self.prepend(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                prev = current_node.prev   
                prev.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                current_node.prev = prev
            current_node = current_node.next

    def delete_node(self, key):
        current_node = self.head

        while current_node: 
            # Case 1: When there is only one node.
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                
                # Case 2: When there is two node and you want to delete the head node.
                else:
                    next = current_node.next
                    current_node.next = None
                    next.prev = None
                    current_node = None
                    self.head = next
                    return

                # Case 3: Removing a node between two nodes 
            elif current_node.data == key:
                if current_node.next:
                    next = current_node.next
                    prev = current_node.prev
                    prev.next = next
                    next.prev = next
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return 
                # Case 4:
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next
                
    def reverse(self):
        temp = None
        current_node = self.head
        while current_node:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
        if temp:
            self.head = temp.prev


    def remove_dupe(self):
        current_node = self.head
        seen = dict()
        while current_node:
            if current_node.data not in seen:
                seen[current_node.data] = 1
                current_node = current_node.next
            else:
                next = current_node.next
                self.delete(current_node)
                current_node = next

    def delete(self, node):
        current_node = self.head

        while current_node: 
            # Case 1: When there is only one node.
            if current_node == node and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                
                # Case 2: When there is two node and you want to delete the head node.
                else:
                    next = current_node.next
                    current_node.next = None
                    next.prev = None
                    current_node = None
                    self.head = next
                    return

                # Case 3: Removing a node between two nodes 
            elif current_node == node:
                if current_node.next:
                    next = current_node.next
                    prev = current_node.prev
                    prev.next = next
                    next.prev = next
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return 
                # Case 4:
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next
                
doublyLinkedList = DoublyLinkedList()
#doublyLinkedList.prepend("0")
doublyLinkedList.append(8)
doublyLinkedList.append(4)
doublyLinkedList.append(4)
doublyLinkedList.append(6)
doublyLinkedList.append(4)
doublyLinkedList.append(8)
doublyLinkedList.append(4)
doublyLinkedList.append(10)
doublyLinkedList.append(12)
doublyLinkedList.append(12)
doublyLinkedList.print()
#doublyLinkedList.prepend("5")
# doublyLinkedList.delete_node("A")
# doublyLinkedList.delete_node("Z")
# doublyLinkedList.delete_node("D")
# doublyLinkedList.delete_node("B")
#doublyLinkedList.add_before_node("C","E")
#doublyLinkedList.add_before_node("C","E")
#doublyLinkedList.reverse()
doublyLinkedList.remove_dupe()
doublyLinkedList.print()