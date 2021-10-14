def selectionSort(array):
	for fillSlot in range(len(array)-1, 0, -1):
		position_of_max = 0
		
		for index in range(1, fillSlot + 1):
			if array[index] > array[position_of_max]:
				position_of_max = index
		temp = array[fillSlot]
		array[fillSlot] = array[position_of_max]
		array[position_of_max] = temp
	return array


array = [5,8,3,10,1]

selectionSort(array)

print(array)