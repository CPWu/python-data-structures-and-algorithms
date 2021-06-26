def insertion_sort(array):
    for item in range(1,len(array)):
        currentValue = array[item]
        position = item

        while position > 0 and array[position-1] > currentValue:
            array[position] = array[position-1]
            position = position-1

            array[position] = currentValue

array = [4,6,2,7,4,1,9,11,23]

insertion_sort(array)

print(array)

