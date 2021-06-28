# Reverse Linked List

## Problem

Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.

## Example

Return: true
```
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1,6,-1,10] 
```

## Complexity
Time = O(n)
Space = O(1)

## Solution

To solve this problem we will have two markers traversing through the list. marker1 and marker2. We will have both makers begin at the first node of the list and traverse through the linked list. However the second marker, marker2, will move two nodes ahead for every one node that marker1 moves.

By this logic we can imagine that the markers are "racing" through the linked list, with marker2 moving faster. If the linked list has a cylce and is circularly connected we will have the analogy of a track, in this case the marker2 will eventually be "lapping" the marker1 and they will equal each other.

If the linked list has no cycle, then marker2 should be able to continue on until the very end, never equaling the first marker.