def selection_sort(array):
    for fillslot in range(len(array)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if array[location] > array[positionOfMax]:
                positionOfMax = location

        temp = array[fillslot]

        array[fillslot] = array[positionOfMax]
        array[positionOfMax] = temp




array = [5,8,3,10,1]

selection_sort(array)

print(array)