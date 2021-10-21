## Divide and Conquer Approach ##
def heapSort(array):
    buildMaxHeap(array)
    
    # Use Python Range Function
	# range(start_param, stop_param, step_param), only stop_param is required
    # Reversed so it will go 9, 8, 7, etc
    for endIndex in reversed(range(1, len(array))):
        swap(0, endIndex, array)
        siftDown(0, endIndex - 1, array)
    return array


# Build a Map Heap
def buildMaxHeap(array):
    firstParentIndex = (len(array) - 2) // 2
    for currentIndex in reversed(range(firstParentIndex + 1)):
        siftDown(currentIndex, len(array) - 1, array)

def siftDown(currentIndex, endIndex, heap):
    childOneIndex = currentIndex * 2 + 1
    while childOneIndex <= endIndex:
        childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
        
        if childTwoIndex > -1 and heap[childTwoIndex] > heap[childOneIndex]:
            indexToSwap = childTwoIndex
        else:
            indexToSwap = childOneIndex
        if heap[indexToSwap] > heap[currentIndex]:
            swap(currentIndex, indexToSwap, heap)
            currentIndex = indexToSwap
            childOneIndex = currentIndex * 2 + 1
        else:
            return

# Swap Function
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
heapSort(array)
print(array)