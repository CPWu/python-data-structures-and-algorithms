# Merge One Sorted Array Into Another

Given two arrays:
1) arr1 of size n, which contains n positive integers sorted in the ascending order.
2) arr2 of size (2*n) (twice the size of first), which contains n positive integers sorted in the ascending order in its first half. Second half of this array arr2 is empty. (Empty elements are marked by 0).
Write a function that takes these two arrays, and merges the first one into second one, resulting in an increasingly sorted array of (2*n) positive integers. 

Example
Input:
n = 3
arr1 = [1 3 5]
arr2 = [2 4 6 0 0 0]

Output: arr2 = [1 2 3 4 5 6]

Notes
Input Parameters: There are two arguments. First one is an integer array denoting arr1 and second one is also an integer array denoting arr2.

Output: You don't have to return anything. You just need to modify the given array arr2.

Constraints:
1 <= n <= 10^5
1 <= arr1[i] <= 2 * 10^9
1 <= arr2[i] <= 2 * 10^9 (for the first half)
arr2[i] = 0 (for the second half)
You can use only constant extra space.
0 denotes an empty space.

Custom Input
Input Format: The first line of input should contain an integer n, denoting size of input array arr1. In next n lines, ith line should contain an integer arr1[i], denoting value at index i of arr1. 
In next line, there should be an integer (2*n), denoting size of input array arr2. In next (2*n) lines, ith line should contain an integer arr2[i], denoting value at index i of arr2.
If n = 3, arr1 = [1, 3, 5] and arr2 = [2, 4, 6, 0, 0, 0], then input should be:
3
1
3
5
6
2
4
6
0
0
0

Output Format: There will (2*n) lines of output, where ith line contains an integer arr2[i], denoting value at index i of arr2. For input n = 3, arr1 = [1, 3, 5] and arr2 = [2, 4, 6, 0, 0, 0], output will be:
1
2
3
4
5
6