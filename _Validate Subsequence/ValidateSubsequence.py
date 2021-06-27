def isValidSubsequence(array,sequence):
    arrayIndex = 0
    sequenceIndex = 0

    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex+=1
            print(sequenceIndex)
        arrayIndex+=1
    return sequenceIndex == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1,6,-1,10] 

print(isValidSubsequence(array,sequence))