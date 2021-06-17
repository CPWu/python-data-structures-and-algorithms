# Queue

Goal: Use Python to Create a Queue Class. 

## Overview

A sequential access data structure in which we add elements and remove elements according the the First In First Out (LIFO) Principle. The first element added to the queue is the first one coming out, similar to a line to a child lining up for an amusement ride. The Queue adds elements at the back (Tail) and we remove from the front (Head), this ensures that the FIFO methodology is followed. 

Common Queue Methods: 

- Enqueue() adds a new item to the tail of the queue. It takes an object and increases the size of the Queue by one.
- Dequeue() removes the item from the head of the queue. It removes an object and decreases the size of the Queue by one.
- peek() returns the forefront item from the queue but does not remove it. It needs no parameteres. The queue is not moodified.
- contains() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.

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
- Job Scheduling
- Printer Queueing
- Modern Smartphone Cameras 

## See Also

[Stack](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

