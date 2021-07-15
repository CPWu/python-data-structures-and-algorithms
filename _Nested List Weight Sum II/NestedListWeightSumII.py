# Nested List Weight Sum II
# Time(D) D = Depth of Nested Lists
# Time(N) N = Number of items in List

class Solution(object):
	def depthSumInverse(self, nestedList):
		return self.calculateSum(nestedList, self.getMaxDepth(nestedList))

	def getMaxDepth(self, nestedList):
		depth_value = 0
		for value in range(nestedList):
			if not value.isInteger():
				depth_value = max(depth_value, self.getMaxDepth(value.getList()))
		
		return depth_value + 1 

	def calculateSum(self, nestedList, depth):
		sum = 0

		for value in range(nestedList):
			if value.isInteger():
				sum += value.getInteger() * depth
			else:
				sum += self.calculateSum(value.getList(), depth -1)
