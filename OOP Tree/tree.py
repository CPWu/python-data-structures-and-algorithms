class BinaryTree(object):
    def __init__(self, rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, object):
        self.key = object

    def getRootValue(self):
        return self.key


r = BinaryTree('a')

print(r.getRootValue())

print(r.getLeftChild())

print(r.getRightChild())


r.insertLeft('b')

print(r.getLeftChild().getRootValue())