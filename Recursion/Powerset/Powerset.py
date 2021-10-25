# O(n*2^n) time | O(n*2^n) space - where n is the length of the input array
def powerset(array, index = None):
    if index is None:
        index = len(array) - 1
    elif index < 0:
        return [[]]
    element = array[index]
    subsets = powerset(array, index - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [element])
    return subsets

array = [1, 2, 3]
print(powerset(array))