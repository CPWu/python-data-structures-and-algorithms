# Time O(N) Space O(N) Average O(log(N))
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
        else: 
            self._insert(data, self.root)
        new_node = Node(data)
        pass

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
            print ("Value is already present in tree.")

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)
        
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        if data == current_node.data:
            return True

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree = BST()
tree.root = Node(1)
tree.root.left = Node(-4)
tree.root.right = Node(3)
tree.root.left.left = Node(-5)
tree.root.left.right = Node(0)
tree.root.right.left = Node(2)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(-8)

print(tree.is_bst_satisfied())
    