## Divide and Conquer Approach ##

def quickSort(array):
	# Initially pass the original array with the start end index
	quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIndex, endIndex):
	# Base case:
	# If left(start) index is greater or equal to the right(end) index then we return
	# This usually means there is one element or array is empty.
	if startIndex >= endIndex:
		return
	# Some variations of this algorithm use last item in array or randomized pivotValue 
	# For this one we will use first element in the array/subarray.
	pivotIndex = startIndex
	leftIndex = startIndex + 1
	rightIndex = endIndex
	
	while rightIndex >= leftIndex:
		# This algorithm works by verifying
		# Smaller values goes on left of pivot
		# Biger values goes on right of pivot
		if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
			swap(leftIndex, rightIndex, array)
		# Move left Index to the left until above condition is met.
		if array[leftIndex] <= array[pivotIndex]:
			leftIndex += 1
		# Move right Index to the left until above condition is met.
		if array[rightIndex] >= array[pivotIndex]:
			rightIndex -= 1
	# Move the pivot value to its rightful place on the right Index.
	# This algorithm will make the rightIndex the rightful position 
	# of the pivot value after the while loop.
	swap(pivotIndex, rightIndex, array)
	leftSubArrayIsSmaller = rightIndex - 1 - startIndex < endIndex - (rightIndex + 1)
	# To ensure this algorithm runs in O(log(N))
	if leftSubArrayIsSmaller:
		# Left SubArray
		quickSortHelper(array, startIndex, rightIndex - 1) 
		# Right SubArray
		quickSortHelper(array, rightIndex + 1, endIndex)
	else: 
		# Right Sub Array
		quickSortHelper(array, rightIndex + 1, endIndex)
		# Left Sub Array
		quickSortHelper(array, startIndex, rightIndex - 1)
		
def swap(i, j, array):
	array[i],array[j] = array[j], array[i]	



array = [4,6,2,7,4,1,9,11,23]

quickSort(array)

print(array)