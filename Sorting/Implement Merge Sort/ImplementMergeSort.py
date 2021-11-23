# Time Complexity O(N Log N)
# Space Complexity O(1)
# Recursive
# Stable

def merge_sort(arr):
    # If lenth of array is one then just return the array.
    if len(arr) == 1:
        return arr

    # Find the middle of the array:
    middleIndex = len(arr) // 2

    # Get Left and Right SubArray using Slicing
    leftSubArray = arr[:middleIndex]
    rightSubArray = arr[middleIndex:]

    # Recursively call until sub arrays have single element in each and then merge.
    return mergeSortedArrays(merge_sort(leftSubArray), merge_sort(rightSubArray))

def mergeSortedArrays(leftSubArray, rightSubArray):
    # New Array that will contain the merge of the sorted arrays.
    sortedArray = [None] * (len(leftSubArray) + len(rightSubArray))
    # Index variables as counters
    # - One to check for midpoint
    # - One to check for left half
    # - One to check for right half   
    i = j = k = 0

    while i < len(leftSubArray) and j < len(rightSubArray):
        if leftSubArray[i] <= rightSubArray[j]:
            sortedArray[k] = leftSubArray[i]
            i += 1
        else:
            sortedArray[k] = rightSubArray[j]
            j += 1
        # Move to next element in sortedArray since its the current idx of k should be filled
        k += 1

    # By the time we exit the while loop above we either exhausted the elements in left or rightHalf of the sub arrays.
    while i < len(leftSubArray):
        sortedArray[k] = leftSubArray[i]
        i += 1
        k += 1
    
    while j < len(rightSubArray):
        sortedArray[k] = rightSubArray[j]
        j += 1
        k += 1

    # return array after main while loop complete with sortedArray
    return sortedArray