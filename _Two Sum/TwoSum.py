# Time Complexity: O(N^2)
# Space Complexity: O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

    # No values add up so return empty list
    return []


targetSum = 10
array = [3, 5, -4, 8, 11, 1, -1, 6]
print(twoNumberSum(array, targetSum))