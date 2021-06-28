# Time O(N), Space O(N)
def findSignatureCounts(arr):
	length_of_array = len(arr)
	result = [0] * length_of_array

	# set of visited students
	visited = set()

	for i in range(len(arr)):
		j = i
		# the students of the same group as student i
		group = set([i])
		# keep passing the yearbook until it goes back to i
		while arr[j]-1 != i:
			j = arr[j]-1
			group.add(j)
		# update the visite set
		visited.update(group)
		for k in group:
			result[k] = len(group)
	return result


n = 2
arr = [2, 1]

print(findSignatureCounts(arr))


