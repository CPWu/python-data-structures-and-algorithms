# Nth to Last Node

## Problem

Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list.

## Example

Return: 4
```
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 

target_node.value
```

## Complexity


## Solution

Imagine you have a bunch of nodes and a "block" which is n-nodes wide. We could walk this "block" all the way down the list, and once the front of the block reached the end, then the other end of the block would be a the Nth node!

So to implement this "block" we would just have two pointers a left and right pair of pointers. Let's mark out the steps we will need to take:

Walk one pointer n nodes from the head, this will be the right_point
Put the other pointer at the head, this will be the left_point
Walk/traverse the block (both pointers) towards the tail, one node at a time, keeping a distance n between them.
Once the right_point has hit the tail, we know that the left point is at the target.