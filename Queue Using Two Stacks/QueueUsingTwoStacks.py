class QueueUsingTwoStacks(object):
    def __init__(self):

        self.inStack = []
        self.outStack = []

    def enqueue(self,element):
        self.inStack.append(element)

    def dequeue(self):
        if not self.outStack:
            while self.outStack:
                self.outStack.append(self.inStack.pop())
        
        return self.outStack.pop()


