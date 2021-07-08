# Using Recursion
# Time: O(V+E) Space: O(V) 

class Node(object):
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current_node = queue.pop(0)
            array.append(current_node.name)
            for child in current_node.children:
                queue.append(child)
        return array
        