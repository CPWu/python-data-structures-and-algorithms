# Sum of Linked Lists

## Problem

You're given two LinkedLists of potentially unequal length. Each linked list represents a non-negative integer, where each node in the Linked List is a digit of that integer, and the first none in each Linked List always represents the least signficant digit of the integer. Write a function that returns the head of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list. The value of each Linked List node is always in the range of 0-9.

Note: Your function must create and return a new Linked List, and you're not allowed to modify either of the input LinkedList

## Example

```
linkedListOne = 2 -> 4 -> 7 -> 1
linkedListTwo = 9 -> 4 -> 5

output: 1 -> 9 -> 2 -> 2
```

## Complexity

Time Complexity: O(max(n, m)) n is the length of the first linked list and m is the second linked list
Space Complexity: O(max(n,m))