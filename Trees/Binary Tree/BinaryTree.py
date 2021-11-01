# Stack - Needed for Reverse Level Order Traversal
class Stack(object):
    # Repurposing Python List for Stack
    def __init__(self):
        self.items = []
    
    # Add item to Stack, end of list (LIFO)
    def push(self, item):
        self.items.append(item)

    # Remove item from stack, end of list 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    # Check to see if Stack/List is empty
    def is_empty(self):
        return len(self.items) == 0

    # Python supports negative arrays indexes, -1 returns last item in list.
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Overrides length operator  
    def __len__(self):
        return self.size()

    # Helper function to support overriding len function.
    def size(self):
        return len(self.items)

# Queue - Needed for Level Order Traversal
class Queue(object):
    # Repurposing Python List for Queue
    def __init__(self):
        self.items = []

    # Add item to Queue, front of list (FIFO)
    def enqueue(self, item):
        self.items.insert(0,item)
    
    # Remove item from queue. (FIFO)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    # Check to see if list/queue is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Python supports negative arrays indexes, -1 returns last item in list.
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    # Overrides length operator
    def __len__(self):
        return self.size()

    # Helper function to support overriding len function.
    def size(self):
        return len(self.items) 

# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    # Constructor
    # Assuming that value 'root' is passed into to define Binary Tree
    # Value is thus stored by instantiating Node class and passing in value 'root'
    def __init__(self, root):
        self.root = Node(root)
    
    # Helper Print Function
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverselevelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")

    # Depth First Search - Preorder Traversal - Recursion
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
        # On every recursive call, as long as start is not null. Print out the value and concat to the string and append - for chaining/formatting.
            traversal += (str(start.value) + "-" )
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # Depth First Search - Inorder Traversal - Recursion
    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        # On every recursive call, as long as start is not null
        if start:
        # On every recursive call, as long as start is not null. Print out the value and concat to the string and append - for chaining/formatting.
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    # Depth First Search - Postorder Traversal - Recursion
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
        # On every recursive call, as long as start is not null. Print out the value and concat to the string and append - for chaining/formatting.
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    # Breadth First Search - Level Order Traversal - Iterative
    # Requires a Queue, enqueue the root, peek, check left right, if exists insert into queue and dequeue and repeat.
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()

        # Enqueue the root node
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal

    # Breadth First Search - Reverse Level Order Traversal - 
    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()

        # Enqueue the root node
        queue.enqueue(start)
        
        traversal = ""

        # If queue is not empty loop and put all the children into the stack
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            # Process right node first to ensure proper traversal
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        # While stack is not empty pop the nodes out and append to traversal for printing out the values
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    # Calculates the height of the tree
    def height(self,node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

# Example Tree:
#
#                       1
#               /               \
#           2                       3
#       /       \               /       \
#   4               5       6               7


# Setup up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Preorder Traversal: " + tree.print_tree("preorder"))
print("Inorder Travsersal: " + tree.print_tree("inorder"))
print("Postorder Travsersal: " + tree.print_tree("postorder"))
print("Levelorder Travsersal: " + tree.print_tree("levelorder"))
print("Reverse Levelorder Travsersal: " + tree.print_tree("reverselevelorder"))