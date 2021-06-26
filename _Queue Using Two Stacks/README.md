# Queue Using Two Stacks

## Problem

Given the Stack class below, implement a Queue class using two stacks. Note, this is a 'classic' interview problem. 

## Example

```
stack1 = []

stack2 = []
```

```
class QueueUsingTwoStacks(object):
    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        # Tell me again what enqueue does
    

    def dequeue(self):
        # Tell me again what dequeue does
```

## Example

```
for i in xrange(5):
    q.enqueue(i)
```

```
for i in xrange(5):
    q.dequeue()
```

## Solution

The key insight is that a stack reverses order (while a queue doesn't). A sequence of elements pushed on a stack comes back in reversed order when popped. Consequently, two stacks chained together will return elements in the same order, since reversed order reversed again is original order.

We use an in-stack that we fill when an element is enqueued and the dequeue operation takes elements from an out-stack. If the out-stack is empty we pop all elements from the in-stack and push them onto the out-stack.