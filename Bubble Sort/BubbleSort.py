def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        print ('This is the i: ',i)
        for j in range(i):
            print ('This is the j index check: ',j)
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

myArray = [5,3,7,1,4,8,2,9,6]
bubble_sort(myArray)
print(myArray)