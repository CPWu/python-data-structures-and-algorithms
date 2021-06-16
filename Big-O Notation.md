# Measuring Efficiency with Big-O Notation

Goal: We want a quantifiable weay to measure how efficient certain data structures are at different tasks.
- Searching
- Modfying
- Accessing

The industry standard for this kind of measurement is Big-O Notation.

## What is it?
Big-O Notation provides a way to "Score" a data structure based on 4 criteria, which are the most common functions you might want from a data structure.
- Accessing Elements
- Searching for an Element
- Insertinng an Element
- Deleting an Element

By measuring how efficiently a data structure can do these 4 things we can create a 'report card' which measures how efficient a certain data structure is. At a glance this provides us the ability to determine what a certain data structure is good at and bad at. It can help us to decide which one to use. For example, if need to store data that is easily accessible by a user then we would want to choose a data structure that is most efficient at Accessing data.

## How do we measure it?
 A Time Complexity Equation works by inserting the size of the data-set as an integer n, and returning the number of operations that need to be conducted by the computer before the function can finish.

- N = The size of the Data Set (Amount of elements contained within the Data Structure)

We always use the worst-case scenario when judging these data structures. This is because we always want to prepare for the worst. Knowing how data structures will perform under worst case scenario.

## Types of Time Complexity Equations

8 Common Time Complexity Equations

Big-O | Name | Description
------| ---- | -----------
**O(1)** | constant | **This is the best.** The algorithm always takes the same amount of time, regardless of how much data there is. Example: looking up an element of an array by its index.
**O(log n)** | logarithmic | **Pretty great.** These kinds of algorithms halve the amount of data with each iteration. If you have 100 items, it takes about 7 steps to find the answer. With 1,000 items, it takes 10 steps. And 1,000,000 items only take 20 steps. This is super fast even for large amounts of data. Example: binary search.
**O(n)** | linear | **Good performance.** If you have 100 items, this does 100 units of work. Doubling the number of items makes the algorithm take exactly twice as long (200 units of work). Example: sequential search.
**O(n log n)** | "linearithmic" | **Decent performance.** This is slightly worse than linear but not too bad. Example: the fastest general-purpose sorting algorithms.
**O(n^2)** | quadratic | **Kinda slow.** If you have 100 items, this does 100^2 = 10,000 units of work. Doubling the number of items makes it four times slower (because 2 squared equals 4). Example: algorithms using nested loops, such as insertion sort.
**O(n^3)** | cubic | **Poor performance.** If you have 100 items, this does 100^3 = 1,000,000 units of work. Doubling the input size makes it eight times slower. Example: matrix multiplication.
**O(2^n)** | exponential | **Very poor performance.** You want to avoid these kinds of algorithms, but sometimes you have no choice. Adding just one bit to the input doubles the running time. Example: traveling salesperson problem.
**O(n!)** | factorial | **Intolerably slow.** It literally takes a million years to do anything.  

## See Also

[Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation)

