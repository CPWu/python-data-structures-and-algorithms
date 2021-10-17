## Brute Force / Decrease and Conquer Approach ##

def bubble_sort(array):
	# Use Python Range Function
	# range(start_param, stop_param, step_param), only stop_param is required
	
	# Loop will start with length of array and step down 1 at a time until first element in array.
	# move_value indicates how many items were sorted
    for i in range(len(array)-1):
        # Last i elements are already in place
        for j in range(0, len(array)-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1]:
                # Swap values if prior element is bigger than the next element.
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


array = [5,3,7,1,4,8,2,9,6]
bubble_sort(array)
print(array)