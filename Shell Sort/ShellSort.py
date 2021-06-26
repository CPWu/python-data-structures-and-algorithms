def shell_sort(array):
    sublistcount = len(array)//2

    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(array, start, sublistcount)

        print('After increments of size: ', sublistcount)
        print('The list is ', array)
         
        sublistcount = sublistcount//2


def gap_insertion_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        currentValue = array[i]
        position = i

        while position >= gap and array[position-gap] > currentValue:
            array[position] = array[position-gap]
            position = position-gap

        array[position] = currentValue

array = [4,6,2,7,4,1,9,11,23]

shell_sort(array)

print(array)



