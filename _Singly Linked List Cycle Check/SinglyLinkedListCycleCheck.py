# Time O(N), Space O(1)
class Node(object):

    def __init__(self,value):
        self.value = value
        self.next = None
    
def cycle_check(node):
    # Create two markers
    marker1 = node
    marker2 = node

    # Go until the end of the list
    while marker2 != None and marker2.next != None:

        # Note
        marker1 = marker1.next
        marker2 = marker2.next.next

         # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


