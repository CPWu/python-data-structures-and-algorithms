# Sorting

In computer science, a sorting algorithm is an algorithm that puts elements of a list into an order. The most frequently used orders are numerical order and lexicographical order, and either ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists. Sorting is also often useful for canonicalizing data and for producing human-readable output.

Formally, the output of any sorting algorithm must satisfy two conditions:

- The output is in monotonic order (each element is no smaller/larger than the previous element, according to the required order).
- The output is a permutation (a reordering, yet retaining all of the original elements) of the input.

For optimum efficiency, the input data should be stored in a data structure which allows random access rather than one that allows only sequential access.

## Comparison of Sorts

- [Bubble Sort](Bubble%20Sort)
- [Selection Sort](Selection%20Sort)
- [Insertion Sort](Insertion%20Sort)
- [Merge Sort](Merge%20Sort)
- [Quick Sort](Quick%20Sort)
- [Heap Sort](Heap%20Sort)
- [Radix Sort](Selection%20Sort)
- [Count Sort](Selection%20Sort)
- [Bucket Sort](Selection%20Sort)
- [Shell Sort](Selection%20Sort)

|                | (Average) Time Comepexity | (Best) Time Comepexity | (Worst) Time Comepexity | Space Comepexity | Comments |
| -------------- | ------------------------- | ---------------------- | ----------------------- | ---------------- | -------- |
| Bubble Sort    | O(n^2)                    | O(n^2)                 | O(n^2)                  | Constant         | N/A      |
| Selection Sort | O(n^2)                    | O(n^2)                 | O(n^2)                  | Constant         | N/A      |
| Insert Sort    | O(n^2)                    | O(n)                   | O(n^2)                  | Constant         | N/A      |
| Heap Sort      | O(n*log(n))               | O(n*log(n))            | O(n*log(n))             | Constant         | N/A      |
| Merge Sort     | O(n*log(n))               | O(n*log(n))            | O(n*log(n))             | Depends          | N/A      |
| Quick Sort     | O(n*log(n))               | O(n*log(n))            | O(n^2)                  | Constant         | N/A      |

## See Also

- [Sorting Algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Visual Algo](https://visualgo.net/en/sorting)
- [Toptal](https://www.toptal.com/developers/sorting-algorithms/bubble-sort)