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

# Implemented Using Max Value, Can be done Min (Move Item Left) or Max (Move Item Right)
def selection_sort(array):
	# Use Python Range Function
	# range(start_param, stop_param, step_param), only stop_param is required
	
	# Loop will start with length of array and step down 1 at time until first element in array.
	for move_value in range(len(array)-1, 0, -1):
		position_of_max = 0
		
		for index in range(1, move_value + 1):
			if arrayp[inde