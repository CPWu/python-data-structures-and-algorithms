# Branch Sums

## Problem

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum. A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. Each Binary Tree node has an integer value, a left child node, and a right child node. Children nodes can either by BinaryTree nodes themselves or None/null.

## Example

```
tree = 
               1
            /     \
          2         3
        /   \     /   \ 
      4      5   6     7
    /   \   /
   8     9 10

output = [15, 16, 18, 10, 11]
```

## Complexity

Time Complexity: O (N) N is the number of nodes.
Space Complexity: O(N) 