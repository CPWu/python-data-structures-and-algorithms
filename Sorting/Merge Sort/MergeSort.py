## Divide and Conquer Approach ##
def merge_sort(array):
    # If array only has element then it is sorted.
    if len(array) == 1:
        return array

    # Get index for for the middle of the array
    middleIdx = len(array) // 2

    # Get Left and Right SubArrays using Python Slicing
    leftArray = array[:middleIdx]
    rightArray = array[middleIdx:]

    # Recursively call until sub arrays have single element in each and then merge.
    return mergeSortedArrays(merge_sort(leftArray), merge_sort(rightArray))


def mergeSortedArrays(leftArray, rightArray):
    # New Array that will contain the merge of the sorted arrays.
    sortedArray = [None] * (len(leftArray) + len(rightArray))
    # Index variables as counters
    # - One to check for midpoint
    # - One to check for left half
    # - One to check for right half   
    i = j = k = 0
    
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            sortedArray[k] = leftArray[i]
            i += 1
        else:
            sortedArray[k] = rightArray[j]
            j += 1
        # Move to next element in sortedArray since its the current idx of k should be filled
        k += 1

    # By the time we exit the while loop above we either exhausted the elements in left or rightHalf of the sub arrays.
    while i < len(leftArray):
        sortedArray[k] = leftArray[i]
        i += 1
        k += 1
    
    while j < len(rightArray):
        sortedArray[k] = rightArray[j]
        j += 1
        k += 1

    # return array after main while loop complete with sortedArray
    return sortedArray

array = [4,6,2,7,4,1,9,11,23]

merge_sort(array)

print(array)
