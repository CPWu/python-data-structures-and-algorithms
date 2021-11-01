# Node Class
class Node(object):
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

print(tree.height(tree.root))