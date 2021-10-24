# O(n*n!) time | O(n*n!) space - where n is the length of the input array
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)


array = [1, 2, 3]
print(getPermutations(array))