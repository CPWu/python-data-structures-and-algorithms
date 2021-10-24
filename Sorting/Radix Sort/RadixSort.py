def radixSort(array):
    if len(array) == 0:
        return array
    
    # get max value in array
    maxNumber = max(array)

    digit = 0
    while maxNumber / 10 ** digit > 0:
        countingSort(array, digit)
        digit += 1
    
    return array

def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10
    
    digitColumn = 10 ** digit
    for num in array:
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1
        
    for index in range(1, 10):
        countArray[index] += countArray[index - 1]
        
    for index in range(len(array) -1, -1, -1):
        countIndex = (array[index] // digitColumn) % 10
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[index]
        
    for index in range(len(array)):
        array[index] = sortedArray[index]

array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
print(radixSort(array))