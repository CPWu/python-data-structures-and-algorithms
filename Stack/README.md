# Stack

Goal: Use Python to Create a Stack Class. The stack abstract data type is defined by the following structure and operations. A stack is structured as decribed above, as an ordered collection of items where items are added to and removed from the end called the "top." Stacks are ordered LIFO. The stack operations are given below.

## Overview

A sequential access data structure in which we add elements and remove elements according the the Last In First Out (LIFO) Principle. Stacks are used everywhere, both in the actual writing of code as wel as in real-world situations. For example in recursion - the process of functions repeatedly calling themselves, when the function calls itself that call is added to a stack of processes. When the stack reaches the base case the functions are then popped off one by one.

Common Stack Methods: 

- Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
- push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
- pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- peek() returns the top item from the stack but does not remove it. It needs no parameteres. The stack is not moodified.
- isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
- size() returns the number of items on the stack. It needs no parameters and returns an integer.
- contains() used for searching through the stack. Takes an object as a parameter and returns a boolean value.

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
- Undo/Redo
- Back-paging

## See Also

[Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

