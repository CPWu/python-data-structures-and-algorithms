# Time Complexity O(N)
# Space Complexity O(N)
# Auxiliary Space O(1)

def merger_first_into_second(arr1, arr2):
    # Lengths of Array with Values
    number_of_nums = len(arr1)

    full_final_array_length = number_of_nums + number_of_nums - 1
    elements_in_array1 = len(arr1)-1
    elements_in_array2 = len(arr1)-1 # We know that number of elements in array2 is equal to elements in array1 plus buffers

    # Array 2 is the larger array which has a large enough buffer to hold array 1.
    # We will compare which one is larger and then insert that element at the end of second array.
    while elements_in_array1 >= 0:
        
        if elements_in_array2 >= 0 and arr2[elements_in_array2] > arr1[elements_in_array1]:
            arr2[full_final_array_length] = arr2[elements_in_array2]
            elements_in_array2 -= 1
        else:
            arr2[full_final_array_length] = arr1[elements_in_array1]
            elements_in_array1 -= 1
        full_final_array_length -= 1

def printArray(arr):
    print("Array B after merging A in sorted order: ")
    for idx in range(len(arr)):
        print(arr[idx], end =" ")

a = [16, 17, 19, 20, 22]
b = [10, 12, 13, 14, 18, None, None, None, None, None]
merger_first_into_second(a, b)
printArray(b)