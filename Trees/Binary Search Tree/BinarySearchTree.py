## Creation of Binary Search Tree ##

## Valid BST 
#                8
#              /   \
#           3        10
#         /   \     /   \
#       1      6   9     11 

## Invalid BST ##
#                12
#              /   \
#           3        14
#         /   \     /   \
#       1      13  11    15 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    # Class Constructor
    def __init__(self):
        self.root = None

    # Insertion - Recursion
    def insert(self, data):
        # If tree is empty
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else: 
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already present in tree.")

    # Find value - Recursion
    def search(self, data):
        if self.root:
            is_found = self._search(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _search(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        if data == current_node.data:
            return True

    # Print Binary Tree (Inorder)
    # Can be done preorder or postorder also.
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, current_node):
        if current_node:
            self._inorder_print_tree(current_node.left)
            print(str(current_node.data))
            self._inorder_print_tree(current_node.right)   
             
# Instantiate Binary Search Tree
binarySearchTree = BinarySearchTree()

binarySearchTree.insert(2)
binarySearchTree.insert(3)
binarySearchTree.insert(1)
binarySearchTree.inorder_print_tree()
print(binarySearchTree.search(3))
print(binarySearchTree.search(4))