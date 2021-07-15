# Invert a Binary Tree

## Problem

Write a function that takes in a Binary Tree and inverts it. It other words, the function should swap every left node in the tree for its corresponding right node. Each Binary Tree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None/null.

## Example

```
tree = 
               1
            /     \
          2         3
        /   \     /   \ 
      4      5   6     7
    /   \
   8     9

output = 
               1
            /     \
          3         2
        /   \     /   \ 
      7      6   5     4
    /   \
   9     8
```

## Complexity

Time Complexity: O (N) N is the number of nodes.
Space Complexity: O(d) d is the depth of the tree.