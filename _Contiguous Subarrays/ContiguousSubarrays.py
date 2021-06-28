# Time O(nlog n), Space O(1)
def count_subarrays(arr):
  n = len(arr)
  ans = []
  L = [0] * n
  R = [0] * n
  
  stack = [(arr[0], 0)]
  for i in range(1, n):
    while stack and arr[i] > stack[-1][0]:
      e = stack.pop()
      L[e[1]] = i - e[1]
    stack.append((arr[i], i))
    
  while stack:
    e = stack.pop()
    L[e[1]] = n - e[1]
      
  stack = [(arr[n - 1], n - 1)]
  for i in range(n - 2, -1, -1):
    while stack and arr[i] > stack[-1][0]:
      e = stack.pop()
      R[e[1]] = e[1] - i
    stack.append((arr[i], i))
    
  while stack:
    e = stack.pop()
    R[e[1]] = e[1] + 1
        
  return [n1 + n2 - 1 for (n1, n2) in zip(L, R)]

arr = [3, 4, 1, 6, 2]

print(count_subarrays(arr))