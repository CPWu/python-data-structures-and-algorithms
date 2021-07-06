class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].data

    def __len__(self):
        return self.size()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.post_order(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order(tree.root)
        elif traversal_type == "reverseorder":
            return self.reverse_order(tree.root)
        else:
            print("Traversal type" + str(traversal_type) + " is not supported.")

    def preorder_print(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        # Left -> Right - Root
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal

    def level_order(self, start):
        if start is None:
            return 

        queue = Queue()
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

    def reverse_order(self, start):
        if start is None:
            return 

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.data) + "-"
        return traversal


#              1
#            /    \
#           2      3
#          / \    /  \
#         4   5  6    7
#                      
# Tree Setup
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
print(tree.print_tree("reverseorder"))