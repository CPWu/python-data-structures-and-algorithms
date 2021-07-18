# Time Complexity: O(N log N)
# Space Complexity: O(1) 
def twoNumberSum(array, targetSum):
    # Assuming its using Quicksort or MergeSort
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        elif currentSum < targetSum:
            leftPointer += 1
        elif currentSum > targetSum:
            rightPointer += 1
    return []

targetSum = 10
array = [3, 5, -4, 8, 11, 1, -1, 6]
print(twoNumberSum(array, targetSum))