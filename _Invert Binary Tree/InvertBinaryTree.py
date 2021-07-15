# Time Complexity: O(N) N is the number of nodes
# Space Complexity: O(d) d is the depth of thre tree

def invertBinaryTree(tree):
	# Using Python list as a Queue set root node.
	queue = [tree] 
	
	while len(queue):
		current_node = queue.pop(0) # Grab the last item like a dequeue
		if current_node is None:
			continue
		swapLeftAndRight(current_node)
		queue.append(current_node.left)
		queue.append(current_node.right)

def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




	
	
		 
