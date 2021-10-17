## Brute Force / Decrease and Conquer Approach ##
def insertion_sort(array)
	# Use Python Range Function
	# range(start_param, stop_param, step_param), only stop_param is required.
    # Assume first element in array is a sorted sub-list with one item.    
    for item in range(1,len(array)):
        
        # Set current value and postion
        current_value = array[item] 2
        position = item idx2

        # Sorted sub-list
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position-1]
            position = position-1

        array[position] = current_value

array = [4,6,2,7,4,1,9,11,23]

insertion_sort(array)

print(array)