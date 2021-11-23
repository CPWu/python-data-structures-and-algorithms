# Time Complexity O(N)
# Space Complexity O(1)

def solve(arr):
    # Initialize left and right pointers
    left_ptr, right_ptr = 0, len(arr)-1

    # While the left pointer is smaller than the right pointer
    while left_ptr < right_ptr:
        
        # Increment the left pointer if the number at that index is even
        if arr[left_ptr]%2 == 0:
            left_ptr += 1
        elif arr[right_ptr]%2 == 1:
            right_ptr -= 1
        else:
            arr[left_ptr],arr[right_ptr] = arr[right_ptr],arr[left_ptr]
    return arr