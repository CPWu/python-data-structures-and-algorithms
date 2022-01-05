# # Time: O(N), Space: O(N)
# def pair_sum_sorted_array(numbers, target):
#     checkedNums = {}
    
#     for index, value in enumerate(numbers):
#         potentialValue = target - value
#         if potentialValue in checkedNums:
#             return [checkedNums[potentialValue], index]
#         else:
#             checkedNums[value] = index
#     return [-1, -1]
        
# Time: O(N), Space: O(1)
# Array already sorted
def pair_sum_sorted_array(numbers, target):
    leftPointer = 0
    rightPointer = len(numbers) - 1
    
    while leftPointer < rightPointer:
        currentSum = numbers[leftPointer] + numbers[rightPointer]
        if currentSum == target:
            return [leftPointer, rightPointer]
        if currentSum < target:
            leftPointer += 1
        if currentSum > target:
            rightPointer -= 1
    
    return [-1, -1]
