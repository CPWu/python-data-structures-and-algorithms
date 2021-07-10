class Solution:
	def depthSumInverse(self, nestedList):
			sol = []
			def dfs(curr, depth) -> None:
				if depth > len(sol):
					sol.append(0)
					
				if curr.getInteger():
					sol[depth - 1] += curr.getInteger()
					return
				for i in curr.getList():
					dfs(i, depth + 1)
			
			for i in nestedList:
				dfs(i, 1)
			
			max_depth = len(sol)
			for i in range(max_depth):
				sol[i] = (max_depth - i) * sol[i]
				
			return sum(sol)


solution = Solution()
print(solution.depthSumInverse([[1,1],2,[1,1]]))
