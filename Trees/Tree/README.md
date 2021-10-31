# Tree

Goal: 

## Overview

Trees store data hierarchically as opposed to linearly. The tree data structure has a root, branches and leaves. The difference between a tree in nature and a tree in computer science is that a tree data structure has its root at the top and its leaves at the bottom. Another property of trees is that all of the children of one node are independent of the children of another node. And finally, a third property is that each leaf node is unique.

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

## Complexity (Worst Case)

Task  | Big-O | Name |
------| ----- | ----- |
**Accessing** | O(n) | linear | 
**Searching** | O(n) | linear |  
**Inserting** | O(1) | constant |
**Deleting**  | O(1) | constant |

## Pros 

## Cons

## Use Cases

## See Also

[Tree](https://en.wikipedia.org/wiki/Tree_(data_structure))

