# Time Complexity: O(N)
# Space Complexity: O(N) Because of Hash Table
def twoNumberSum(array, targetSum):
    nums = dict()
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []

targetSum = 10
array = [3, 5, -4, 8, 11, 1, -1, 6]
print(twoNumberSum(array, targetSum))