# Time O(N), Space O(1)
import sys

#
# Window Sliding - Static Window
#
# def maxSumSubarray(array, k):
	
# 	# Value to store the max sum, arbitrarily set to 'infinity'
# 	maxValue = float('-inf')
# 	currentWindowSum = 0

# 	for windowStart in range(len(array) - 1):
# 		currentWindowSum += array[windowStart]
# 		if (windowStart >= k - 1):
# 			maxValue = max(maxValue, currentWindowSum)
# 			currentWindowSum -= array[windowStart - (k -1)]
	
# 	return maxValue


# array = [4, 2, 1, 7, 8, 1, 2, 8, 1, 10]
# print("Max sum:", maxSumSubarray(array, 3))

#
# Window Sliding - Dynamic Window
#

# def smallestSumSubarray(array, targetSum):
# 	minWindowSize = float('inf')
# 	currentRunningSum = 0
# 	windowStart = 0
# 	for windowEnd in range(len(array) - 1):
# 		currentRunningSum += array[windowEnd]

# 		while currentRunningSum >= targetSum:
# 			minWindowSize = min(minWindowSize, windowEnd - windowStart + 1)
# 			currentRunningSum -= array[windowStart]
# 			windowStart += 1
# 	return minWindowSize

# array = [4, 2, 1, 7, 8, 1, 2, 8, 1, 10]
# print("Min window:", smallestSumSubarray(array, 8))

#
# Window Sliding - Dynamic Window + Auxiliary Data Structure
#

def lengthOfLongestSubstringKDistinct(inputString, numOfDistinctChars):
	lengthOfString = len(inputString)
	# Removes edges cases
	if numOfDistinctChars == 0 or lengthOfString == 0:
		return 0
	print(numOfDistinctChars)
	left = 0
	right = 0

	hashMap = dict()
	# We know that there is at least one char
	max_length = 1

	while right < lengthOfString:
		# add a new character and move pointer to the right
		hashMap[inputString[right]] = right
		right += 1

		if len(hashMap) == numOfDistinctChars + 1:
			# Delete the left most character
			delete_index = min(hashMap.values())
			del hashMap[inputString[delete_index]]
			# Move pointer to the right by 1
			left = delete_index + 1

		max_length = max(max_length, right - left)
	return max_length
	
myString = 'eceba'
print("Length of Longest Substring: ", lengthOfLongestSubstringKDistinct(myString, 2))