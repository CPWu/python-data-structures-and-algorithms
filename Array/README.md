# Array

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

## Complexity (Worst Case)

Task  | Big-O | Name |
------| ----- | ----- |
**Accessing** | O(1) | constant | 
**Searching** | O(n) | linear |  
**Inserting** | O(n) | linear |
**Deleting**  | O(n) | linear |

## Pros 
- Good for storing similar contiguous data
- O(1) Accessing Power
- Very basic, Easy to learn and master

## Cons
- Size of the array cannot be changed onced initialized
- Inserting and Deleting are not efficient
- Can be wasted storage space

Overall, pretty reliable. Has some flaws as well as advantages. Can be used in almost any program if need be, but sometimes you may want extra functionality.

# ArrayList

An ArrayList is simply a resizable array (dynamic), behind the scenes an ArrayList is actually backed by an Array in memory. Thus an ArrayList has very similar functionality like an Array.

**Arrays and arrayLists are frankensteined together into a single data structure called Lists. Python Lists take on some functionality from both data structures.**

## Overview

An ArrayList is like an older sibling of the Array. The ArrayList belongs to the pre-built arrayList 'class' which means it has pre-built functions that we can use. If we were using an array we would have to program these functions from scratch.

The type of functionality from the ArrayList class varies depending on the language. 

Common methods in an ArrayList class is:
- Add 
- Remove 
- Get 
- Set 
- Clear 
- toArray 

## Complexity (Worst Case)

Task  | Big-O | Name |
------| ----- | ----- |
**Accessing** | O(1) | constant | 
**Searching** | O(n) | linear |  
**Inserting** | O(n) | linear |
**Deleting**  | O(n) | linear |

- Can be wasted storage space


## Pros 

## Cons

# List

In Python, there is an abstract data type of type List that allows us to implement many of the data structures in other programming languages. Lists are one of 5 built-in data types in Python used to store collections of data. (The other 3 are Tuple, Set, Dictionary)

## Overview

Python has a set of built-in methods that can be used on lists/arrays.

Method  | Big-O | Name | Description
|------| ----- |
**append()** | O(1) | constant | 
**clear()** | O(n) | linear |  
**copy()** | O(n) | linear |
**count()**  | O(n) | linear |
**extend()**  | O(n) | linear |
**index()**  | O(n) | linear |
**insert()**  | O(n) | linear |
**pop()**  | O(n) | linear |
**remove()**  | O(n) | linear |
**reverse()**  | O(n) | linear |
**sort()**  | O(n) | linear |


## Pros 

## Cons

## See Also
[Array](https://en.wikipedia.org/wiki/Array)
[ArrayList](https://en.wikipedia.org/wiki/Dynamic_array)
[List](https://en.wikipedia.org/wiki/List_(abstract_data_type))

