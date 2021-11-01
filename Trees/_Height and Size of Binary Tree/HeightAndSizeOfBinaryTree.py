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

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def recursive_size(self, node):
        if node is None:
            return 0
        
        return 1 + self.recursive_size(node.left) + self.recursive_size(node.right)

    def size(self):
        if self.root is None:
            return 0
        
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

# Example Tree:
#
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
print(tree.height(tree.root))
print(tree.size())
print(tree.recursive_size(tree.root))