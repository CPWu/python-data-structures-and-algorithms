# Time O(nlogn) / Space O(n)
def sortedSquareArray(array):
    newArray = [0 for _ in array]

    for element in range(len(array)):
        value = array[element]
        newArray[element] = value * value
    newArray.sort()
    return newArray


# Time O(n) / Space O(n)
array = [1,2,3,5,6,8,9]
print(sortedSquareArray(array))

def optimizedSortedSquareArray(array):
    newArray = [0 for _ in array]
    smallerValueIndex = 0
    largerValueIndex = len(array) - 1

    for index in reversed(range(len(array))):
        smallerValue = array[smallerValueIndex]
        largerValue = array[largerValueIndex]

        if abs(smallerValue > abs(largerValue)):
            newArray[index] = smallerValue * smallerValue
            smallerValueIndex += 1
        else:
            newArray[index] = largerValue * largerValue
            largerValueIndex -= 1
    return newArray


array = [1,2,3,5,6,8,9]
print(optimizedSortedSquareArray(array))