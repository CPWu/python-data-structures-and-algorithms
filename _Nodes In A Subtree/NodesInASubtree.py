# Time Complexity: O(N*M) O(N) for Nodes // O(M) for queries
# Space Complexity: O(N)
class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

def count_of_nodes(root, queries, s):
    myDictionary = dict()
    def depth_first_search(root, count):
        # If Root is Empty
        if not root:
            return 

        # If there is a Root but no children
        if not root.children:
            myDictionary[root.val] = s[root.val - 1]
            return

        myDictionary[root.val] = s[root.val - 1]

        for char in root.children:
            depth_first_search(char, count)
            myDictionary[root.val] += myDictionary[char.val]

        depth_first_search(root, myDictionary)

        result = []

        for query in queries:
            result.append(myDictionary[query[0]].count(query[1]))
        return result