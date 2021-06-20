class DoublyLinkedListNode(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.previous_node = None



a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)


a.next_node = b
b.next_node = c
b.previous_node = a
c.previous_node = b