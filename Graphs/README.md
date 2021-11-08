# Graph

## Overview

A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices (V) and the edges (E) are lines or arcs that connect any two nodes in the graph. Formally, a graph is a pair of sets (V,E) where V is the set of vertices and E is the set of edges, connecting the pairs of vertices.

### Concepts of Graph Data Structure

<strong>Vertex</strong> - Each node of the graph is represented as a vertex. In the following example two vertices, the labeled circle represents vertices. Thus, A to G are vertices. We can represent them using an array as shown in the following image. Here A can be identified by 0. B can be identified using index 1 and so on.

<strong>Edge</strong> - Edge represents a path between two vertices or a line between two vertices. In the following example, the lines from A to B, B to C and so on represents edges. We can use a two-dimensional array to represent an array as shown in the following image. Here AB can be represented as 1 

<strong>Adjacency</strong> - Two nodes or vertices are adjacent if they are connected to each other through an edge. In the following example, B is adjacent to A, C is adjacent to B, and so on.

<strong>Path</strong> - Path represents a sequence of edges between the two vertices. In the following example, ABCD represents a path from A to D.

![Graph](https://www.tutorialspoint.com/data_structures_algorithms/images/graph.jpg)

### Directed and Undirected Graph

A graph can be directed or undirected. However, in an undirected graph, edges are not associated with the directions with them. An undirected graph is shown in the above figure since its edges are not attached with any of the directions. If an edge exists between vertex A and B then the vertices can be traversed from B to A as well as A to B.

## Graph Representation

By Graph representation, we simply mean the technique which is to be used in order to store some graph into the computer's memory.

### Sequential Representation

In sequential representation, we use an adjacency matrix to store the mapping represented by vertices and eddges. In an adjacency matrix, the rows and columns are represented by the graph vertices. A graph having n vertices, will have a dimension n * n.

### Linked Representation

In the linked representation, an adjacency list is used to store the Graph into the computer's memory. 

## See Also

[Graphs](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))

