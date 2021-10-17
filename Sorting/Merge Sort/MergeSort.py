## Divide and Conquer Approach ##
def merge_sort(array):
    # Check the length of the array is greater than 1, if it is then we divide the array into 2
    if len(array) > 1:
        mid = len(array)//2

        # Use Slicing built-in to Python lists
        # Beginnng to middle of list
        lefthalf = array[:mid]
        # Middle to end of list
        righthalf = array[mid:]

        # Recursive call on left and right half
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # Index variables as counters
        i = 0
        j = 0
        k = 0

        # Three while loops
        # - One to check for midpoint
        # - One to check for left half
        # - One to check for right half
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i+=1
            else:
                array[k] = righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j+=1
            k+=1

array = [4,6,2,7,4,1,9,11,23]

merge_sort(array)

print(array)