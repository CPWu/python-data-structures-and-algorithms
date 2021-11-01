# Trees

Goal: Use Python for Trees.

## Overview

Trees store data hierarchically as opposed to linearly. The tree data structure has a root, branches and leaves. The difference between a tree in nature and a tree in computer science is that a tree data structure has its root at the top and its leaves at the bottom. Another property of trees is that all of the children of one node are independent of the children of another node. And finally, a third property is that each leaf node is unique.

<strong>Node</strong>
- A node is a fundamental part of a tree. It can have a name, which we call the 'key'
- A node may also have additional information. We call this additional information the 'payload'
- While the payload infomration is not central to many tree algorithms, it is often critical in applications that make use of trees.

<strong>Edge</strong>
- An edge is another fundamental part of a tree.
- An edge connects two nodes to show that there is a relationship between them.
- Every node (except the root) is connected by exactly one incoming edge from another node.
- Each node may have several outgoing edges.

<strong>Root</strong>
- The root of the tree is the only node in the tree that has no incoming edges.

<strong>Path</strong>
- A path is an ordered list of nodes that are connected by edges.

<strong>Children</strong>
- The set of nodes that have incoming edges from the same node to are said to be children of that node.

<strong>Sibling</strong>
- Nodes in the tree that are children of the same parent are said to be siblings

<strong>Sub-Tree</strong>
- A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.

<strong>Leaf Node</strong>
- A leaf node is a node that has no children.

<strong>Depth</strong>
- Number of levels in a tree.
  
### Types of Trees

#### [Binary Tree](Binary%20Tree)

A Binary Tree is a non-linear data structure in which a node can either have **0, 1** or **maximum 2 nodes.** Each node in a binary tree is represented either as a parent node or a child node. There can be two children of the parent node, i.e., **left child** and **right child.**

#### [Binary Search Tree](Binary%20Search%20Tree)

A Binary Search Tree is a tree that follows some order to arrange the elements, whereas the binary tree does not follow any order. In a Binary Search Tree, the value of the left node must be smaller than the parent node, and the value of the right node must be greater than the parent node.

Concepts:
- Dictionaries and Sets
- Array and Linked List
- Hash Tables
- Binary Search Trees
- Binary Search Tree - Search
- Binary Search Tree - Insert
- Binary Search Tree - Min and Max
- Binary Search Tree - Successor & Predecessor
- Binary Search Tree - Delete
- Hierarchical data
- Breadth First Search
- Preorder, Inorder and PostOrder Depth First Search
- Successor and Predecessor Revisted
- Reconstructing Binary Tree from Traversals

## Practice Problems
  
## See Also

[Tree](https://en.wikipedia.org/wiki/Tree_(data_structure))
