# class Solution:
# 	def depthSumInverse(self, nestedList):
# 			sol = []
# 			def dfs(curr, depth) -> None:
# 				if depth > len(sol):
# 					sol.append(0)
					
# 				if curr.getInteger():
# 					sol[depth - 1] += curr.getInteger()
# 					return
# 				for i in curr.getList():
# 					dfs(i, depth + 1)
			
# 			for i in nestedList:
# 				dfs(i, 1)
			
# 			max_depth = len(sol)
# 			for i in range(max_depth):
# 				sol[i] = (max_depth - i) * sol[i]
				
# 			return sum(sol)


# solution = Solution()

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
