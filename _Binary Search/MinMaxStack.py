# Using Recursion
# Time: O(log(n)) Space: O(log(n)) 
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2 # Python Rounds Down
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
print(binarySearch(array, 72))

# Interative Approach
# Time: O(log(n)) Space: O(1) 
def iBinarySearch(array, target):
    return iBinarySearchHelper(array, target, 0, len(array)-1)

def iBinarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else: 
            left = middle + 1
    return -1