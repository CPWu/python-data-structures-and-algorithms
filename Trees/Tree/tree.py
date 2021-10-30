# List of Lists Tree, we will store the value of the root node as the first element of the list.
# The second element of the list will itself be a list that represents the left subtree.
# The third element of the list will be another list that represents the right subtree.

def BinaryTree(root):
    return [root,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    
    if len(t) > 1:
        root.insert(2,[newBranch,[],[t]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootValue(root):
    return root[0]

def setRootValue(root, newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)

print(insertLeft(r, 4))

print(insertLeft(r,5))

print(insertRight(r,6))

print(insertRight(r,7))

l = getLeftChild(r)

print(l)

setRootValue(l,9)

print(r)