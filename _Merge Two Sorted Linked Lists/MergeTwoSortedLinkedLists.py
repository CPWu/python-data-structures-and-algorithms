from typing import Counter


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        # What happens when linked list is empty?
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        # find the last node
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

    def length(self):
        current_node = self.head
        nodeCount = 0

        while current_node:
            nodeCount += 1
            current_node = current_node.next
        
        return nodeCount

    def merge_sorted(self, linkedList):
        p = self.head
        q = linkedList.head
        # new linked list returned
        s = None

        # if either linked list is empty
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

linkedListOne = LinkedList()
linkedListTwo = LinkedList()
linkedListOne.append("1")
linkedListOne.append("3")
linkedListOne.append("5")
linkedListOne.append("7")
linkedListOne.append("9")
linkedListOne.print()
linkedListTwo.append("2")
linkedListTwo.append("4")
linkedListTwo.append("6")
linkedListTwo.append("8")
linkedListTwo.print()
linkedListOne.merge_sorted(linkedListTwo)
linkedListOne.print()

