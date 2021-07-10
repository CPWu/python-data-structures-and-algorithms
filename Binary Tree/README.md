# Binary Tree

Goal: 

## Overview

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

Top Node (Root):
- Top Node of the Tree
- Binary Trees contain at most two children.

Node
- A node is a fundamental part of a tree. It can hae a name, which we call the 'key'
- A node may also have additional information. We call this additional information the 'payload'
- While the payload infomration is not central to many tree algorithms, it is often critical in applications that make use of trees.

Edge
- An edge is another fundamental part of a tree.
- An edge connects two nodes to show that there is a relationship between them.
- Every node (except the root) is connected by exactly one incoming edge from another node.
- Each node may have several outgoing edges.

Root 
- The root of the tree is the only node in the tree that has no incoming edges.

Path 
- A path is an ordered list of nodes that are connected by edges.

Children 
- The set of nodes that have incoming edges from the same node to are said to be children of that node.

Sibling
- Nodes in the tree that are children of the same parent are said to be siblings

SubTree
- A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.

Leaf Node
- A leaf node is a node that has no children.

Depth
- Number of levels in a tree.

Complete Tree
- Every level except possibly the last is completely filled and all nodes in the last level are as far left as possible.

Full Binary Tree
- A full binary tree (sometimes referred to as a proper or plane binary tree) is a tree in which every node has either 0 or 2 children.

Binary Tree Traversals 
- Process of visiting (checking and/or updating) each node in a tree data structure, exactly once.

Example Tree

```
               F
           /       \
          B         G
        /   \         \
       A     D         I
            / \       /
           C   E     H
```
Depth First Search
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
Breadth First Search


## See Also

[Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)

