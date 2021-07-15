# Time Complexity: O(M * N) 
# Space Complexity: O(M * N) in the situation the whole grid is one massive island
class Solution(object):
	def numIslands(self, grid):
		# If Grid is Empty
		if not grid:
			return 0
		
		# VAR to Count Islands
		islandCount = 0

		rows = len(grid)
		columns = len(grid[0])

		for r in range(rows):
			for c in range(columns):
				if grid[r][c] == "1":
					islandCount += 1
					# Island may be larger than one cell
					self.traverseIsland(r, c, grid)

		return islandCount


	def traverseIsland(self, r, c, grid):
		rows = len(grid)
		columns = len(grid[0])

		if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
			return 

		# Mark Island as traversed
		grid[r][c] == "0"

		self.traverseIsland(r + 1, c, grid)
		self.traverseIsland(r - 1, c, grid)
		self.traverseIsland(r, c + 1, grid)
		self.traverseIsland(r, c -1, grid)
		 
