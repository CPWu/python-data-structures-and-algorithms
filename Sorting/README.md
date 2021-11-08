# Sorting

In computer science, a sorting algorithm is an algorithm that puts elements of a list into an order. The most frequently used orders are numerical order and lexicographical order, and either ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists. Sorting is also often useful for canonicalizing data and for producing human-readable output.

Formally, the output of any sorting algorithm must satisfy two conditions:

- The output is in monotonic order (each element is no smaller/larger than the previous element, according to the required order).
- The output is a permutation (a reordering, yet retaining all of the original elements) of the input.

For optimum efficiency, the input data should be stored in a data structure which allows random access rather than one that allows only sequential access.

## Sorting Algorithms

- [Bubble Sort](Bubble%20Sort)
- [Selection Sort](Selection%20Sort)
- [Insertion Sort](Insertion%20Sort)
- [Merge Sort](Merge%20Sort)
- [Quick Sort](Quick%20Sort)
- [Heap Sort](Heap%20Sort)
- [Radix Sort](Radix%20Sort)
- [Three Number Sort](Three%20Number%20Sort)
- [Bucket Sort](Selection%20Sort)
- [Shell Sort](Selection%20Sort)
- [Count Sort](Selection%20Sort)
- 
## Stable Sorting

A sorting algorithm is said to be stable if two objects with equal keys appear in the same order output as they appear in the input array to be sorted. 

Suppose we have a list of 5-letter words:

```bash
preach
straw
apple
spork
```

If we sort the list by just the first letter of each word than the stable sort would produce:

```bash
apple
preach
straw
spork
```

In an unstable sort algorithm, straw or spork may be interchanged, but in a stable one, they stay in the same relative positions (that is, since straw appears before spork in the input, it also appears before spork in the output).

### Stable Sorting Algorithms

- Insertion Sort
- Merge Sort
- Bubble Sort
- Tim Sort
- Counting Sort
- Block Sort
- Quadsort
- Library Sort
- Cocktail shaker Sort
- Gnome Sort
- Odd–even Sort
  
### Unstable Sorting Algorithms

- Heap sort
- Selection sort
- Shell sort
- Quick sort
- Introsort (subject to Quicksort)
- Tree sort
- Cycle sort
- Smoothsort
- Tournament sort(subject to Hesapsort)

## Comparison of Sorts

<strong>Selection/Bubble Sort:</strong> O(n^2)

<strong>Insertion Sort:</strong> O(n^2)
- Great for small arrays
- Great for almost sorted

<strong>Merge Sort:</strong>
- O(nlogn) worst case
- stable
- uses aux space

<strong>Quick Sort:</strong>
- O(nlogn) average case
- empirically fast
- not stable
- in place

<strong>Heap Sort</strong>
- O(nlogn) worst case
- not stable
- in place

|                | (Average) Time Comepexity | (Best) Time Comepexity | (Worst) Time Comepexity | Space Comepexity | Comments |
| -------------- | ------------------------- | ---------------------- | ----------------------- | ---------------- | -------- |
| Bubble Sort    | O(n^2)                    | O(n^2)                 | O(n^2)                  | Constant         | N/A      |
| Selection Sort | O(n^2)                    | O(n^2)                 | O(n^2)                  | Constant         | N/A      |
| Insert Sort    | O(n^2)                    | O(n)                   | O(n^2)                  | Constant         | N/A      |
| Heap Sort      | O(n*log(n))               | O(n*log(n))            | O(n*log(n))             | Constant         | N/A      |
| Merge Sort     | O(n*log(n))               | O(n*log(n))            | O(n*log(n))             | Depends          | N/A      |
| Quick Sort     | O(n*log(n))               | O(n*log(n))            | O(n^2)                  | Constant         | N/A      |

## Practice Problems

- [2 Sum In A Sorted Array]
- [2 Sum In An Array]
- [Merge k Sorted Singly Linked Lists]
- [Attend Meetings]
- [Top K Frequent Elements]
- [Kth Largest In A Stream]
- [Kth Largest In An Array]
- [Online Median]
- [Intersection Of Tree Sorted Arrays]
- [Group The Numbers]
- [Implement Merge Sort]
- [Merge One Sorted Array Into Another]
- [Dutch National Flag]
  
## See Also

- [Sorting Algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Visual Algo](https://visualgo.net/en/sorting)
- [Toptal](https://www.toptal.com/developers/sorting-algorithms/bubble-sort)