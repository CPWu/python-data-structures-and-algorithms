# Binary Tree
 
## Overview

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

Ex.
                                        1
                                    /       \
                                2               3
                            /       \
                        5              6

## Properties of Binary Tree

- At each level d, the maximum number of nodes is 2^d.
- The height of the tree is defined as the longest path from the root node to the leaf node. The tree which is shown above has a height equal to 3. Therefore, the maximum number of nodes at height 3 is equal to (1+2+4+8) = 15. In general, the maximum number of nodes possible at height h is (2^0 + 2^1 + 2^2+ + 2^h) - 1.
- The minimum number of nodes possible at height h is equal to h+1.
- If the number of nodes is minimum, then the height of the tree would be maximum. Conversely, if the number nodes is maximum, then the height of the tree would be minimum.

## Types of Binary Tree

<strong>Full/Proper/Strict Binary Tree</strong>
- The tree can only be considered as the full binary tree if each node must contain either 0 or 2 children. The full binary tree can also be defined as the tree in which each node must contain 2 children except the leaf nodes.

Ex.
                                        1
                                    /       \
                                2               3
                            /       \
                        5              6

<strong>Complete Tree</strong>
- The complete binary tree is a tree in which all the nodes are completely filled except the last level. In the last level, all the nodes must be as left as possible. In a complete binary tree, the nodes should be added from the left.

Ex.
                                            10
                                    /               \
                                  20                    30
                            /           \           /         \
                         40              50     60              70      
                     / 
                80           

<strong>Perfect Binary Tree</strong>
- A tree is a perfect binary tree if all the internal nodes have 2 children, and all the leaf nodes are at the same level.

Ex.
                                            10
                                    /               \
                                  20                    30
                            /           \           /         \
                         40              50     60              70      

<strong>Degenerate Binary Tree</strong>
- The degenerate binary tree is a tree in which all the internal nodes have only one children.

Ex.
                                        1
                                    /   
                                2             
                            /      
                        5           

<strong>Balanced Binary Tree</strong>
- The balanced binary tree is a tree in which both the left and right trees differ by atmost 1. For example, AVL and Red-Black trees are balanced binary tree.

Ex.
                                            10
                                    /               \
                                  20                   30
                            /           \                    \
                         40              50                     70   
                         
## Binary Tree Traversals 
- Process of visiting (checking and/or updating) each node in a tree data structure, exactly once.

#                                            F
#                                    /               \
#                                  B                   G
#                            /           \                   \
#                         A                 D                   I   
#                                    /            \         /        
#                                 C                  E    H              

 <strong>Depth First Search</strong>
- Preorder Traversal
    - Check if current node is empty/null
    - Display the data port of the root or node
    - Traverse the left subtree by recursively calling the preorder function.
    - Pre-order: F, B, A, D, C, E, G, I ,H
- Inorder Traversal
    - Check if the current node is empty/null
    - Traverse the left subtree by recursively calling the inorder function.
    - Display the data part of the root or current node
    - Traverse the right subtree by recursively calling the inorder function.
    - Inorder: A, B, C, D, E, F, G, H, I
- Postorder Traversal
    - Check if the current node is empty/null
    - Traverse the left subtree by recursively calling the post-order function
    - Traverse the right subtree by recursively calling the post-order function
    - Display the data part of the root (or current node)
    - 
<strong>Breadth First Search</strong>
- Level Order Traversal
  
## Complexity (Worst Case)

Task  | Big-O | Name |
------| ----- | ----- |
**Accessing** | O(n) | linear | 
**Searching** | O(n) | linear |  
**Inserting** | O(1) | constant |
**Deleting**  | O(1) | constant |

## See Also

[Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)

