## Brute Force / Decrease and Conquer Approach ##

# Implemented Using Max Value, Can be done Min (Move Item Left) or Max (Move Item Right)
def selection_sort(array):
	# Use Python Range Function
	# range(start_param, stop_param, step_param), only stop_param is required
	
	# Loop will start with length of array and step down 1 at time until first element in array.
	# move_value indicates how many items were sorted
	for move_value in range(len(array)-1, 0, -1):
		# To find the maximum value value of unsorted segment
		# We first assume that the first element is the largest
		position_of_max = 0
		
		# We use index to loop through the remaining elements
		for index in range(1, move_value + 1):
		# Update the position_of_max if the element at index is lower than it.
			if array[index] > array[position_of_max]:
				position_of_max = index
		# After finding the largest value of the unsorted regions, swap with the first unsorted element.		
		temp = array[move_value]
		array[move_value] = array[position_of_max]
		array[position_of_max] = temp
		print(array)
	return array

# # Implemented Using Min Value, Can be done Min (Move Item Left) or Max (Move Item Right)
# def selection_sort(array):
# 	# Use Python Range Function
# 	# range(start_param, stop_param, step_param), only stop_param is required
	
# 	# Loop will start with length of array and step down 1 at time until first element in array.
# 	# move_value indicates how many items were sorted
# 	for move_value in range(len(array)-1):
# 		# To find the minimum value value of unsorted segment
# 		# We first assume that the first element is the lowest
# 		position_of_min = 0
# 		# We use j to loop through the remaining elements
# 		for j in range(move_value+1, len(array)):
# 			# Update the position_of_min if the element at j is lower than it.
# 			if array[j] < array[position_of_min]:
# 				position_of_min = j
# 			# After finding the lowest value of the unsorted regions, swap with the first unsorted element.
# 			temp = array[move_value]
# 			array[move_value] = array[position_of_min]
# 			array[position_of_min] = temp
# 			print(array)
# 	return array

array = [5,8,3,10,1]
selection_sort(array)

print(array)