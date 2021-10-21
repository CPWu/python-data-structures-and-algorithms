## Decrease and Conquer Approach ##
# O(n) time | O (1) - where n is the length of the array

def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]
    
    for element in array:
        orderIndex = order.index(element)
        valueCounts[orderIndex] += 1
    
    for i in range(3):
        value = order[i]
        count = valueCounts[i]
        
        numberOfElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIndex = numberOfElementsBefore + n
            array[currentIndex] = value
            
    return array



array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array,order)
print(array)