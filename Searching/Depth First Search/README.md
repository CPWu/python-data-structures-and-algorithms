# Depth First Search

## Problem

You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like tructure. 

Implement depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-First Search approach (specifically navigating the tree from left to right), stores all of the nodes names in the input array, and returns it.


## Example

Output: target = ["A", "B","E","F","I","J","C","D","G","K","H"]
```
                A
            /   |    \
           B    C     D
          / \        / \
         E   F      G   H
            / \      \
           I   J      K
```

## Complexity
Time
- O(V)
Space
- O(V+E)


## Solution

