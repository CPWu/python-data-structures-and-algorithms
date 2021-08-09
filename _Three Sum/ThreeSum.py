# Time Complexity: O(N^2)
# Space Complexity: O(N)
def threeSum(nums):
    result = set()

    # Split the nums into three lists: negative numbers, positive numbers, and zeros
    negative_nums, postive_nums, zeros = [],[],[]

    for num in nums:
        if num > 0:
            postive_nums.append(num)
        elif num < 0:
            negative_nums.append(num)
        else:
            zeros.append(num)

    # Create a separate set of negatives and positives for O(1) look-up times
    negative_set, positive_set = set(negative_nums), set(postive_nums)

    # If there is at least 1 zero in the list, add all cases where -num exists in negative_set and num exists in postive_set
    # Ex. (-3, 0, 3) = 0
    if zeros:
        for num in positive_set:
            if -1 * num in negative_set:
                result.add((-1 * num, 0, num))

    # If there are at least 3 zeros in the list then include (0,0,0) = 0
    if len(zeros) >= 3:
        result.add((0,0,0))

    # For all pairs of negative numbers (-3, 1), check to see if their complement (4) exists in the postive number set
    for i in range(len(negative_nums)):
        for j in range(i+1, len(negative_nums)):
            target = -1 * (negative_nums[i] + negative_nums[j])
            if target in positive_set:
                result.add(tuple(sorted([negative_nums[i], negative_nums[j], target])))

    # For all pairs of postive numbers (1,1) check to see if their complement (-2)
    # exists in the negative number set
    for i in range(len(postive_nums)):
        for j in range(i+1, len(postive_nums)):
            target = -1 * (postive_nums[i] + postive_nums[j])
            if target in negative_nums:
                result.add(tuple(sorted(postive_nums[i], [postive_nums[j], target])))


    return result


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))