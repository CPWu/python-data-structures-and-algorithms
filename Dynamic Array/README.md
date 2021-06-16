# Dynamic Array

Goal: Use Python to Create a Dynamic Array that automatically allocates 2x space as we hit the storage capacity of the original array.

## Overview
An array is fundamentally a list of similar values. It can be used to store anything such as usernames, high scores, prices, etc. Arrays store values of the same type such as Integer, String, Float. Every item in the list of data referred to as an "element" and the collective total of elements is the array. 

An array usually has 3 attributes:
- Name
- A Type
- A Size

An array's size is a set integer that is fixed upon creation of the array. The array size represents the total amount of elements that are able to be stored within the array. An array size cannot be changed.

Array instantiation in Python is done with:

```
    array = [1,2,3]
```

- As Python is a dynimcally typed language the type of the array is determined at runtime. 
- Python populate later array is not conventionally possible without the advanced use of other data structures and packages.

The Concepts of a 2D, 3D and 4D Array will not be covered in this repository. 

## Complexity

Task  | Big-O | Name |
------| ----- | ----- |
**Accessing** | O(1) | constant | 
**Searching** | O(n) | linear |  
**Inserting** | O(n) | linear |
**Deleting**  | O(n) | linear |

## See Also

[Dynamic Array](https://en.wikipedia.org/wiki/Dynamic_array)

