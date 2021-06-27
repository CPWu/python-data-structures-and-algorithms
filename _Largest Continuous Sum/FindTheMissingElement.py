def largest_continuous_sum(array):
    # If array is empty than result is 0
    if len(array) == 0:
        return 0
    
    # Pick first element in array to be the largest sum
    maximum_sum = array[0]

    # Rotating variable to keep track of sum
    current_sum = 0

    for element in range(len(array)-1):
        current_sum += array[element]
        # If rotating sum is greater than maximum sum, than maximum sum changes.
        if current_sum > maximum_sum:
            maximum_sum = current_sum
        # If current sum falls below 0 because of negative values we reset to 0 in case so new sequences can equal to max sum.
        elif current_sum < 0:
            current_sum = 0
    return maximum_sum

print(largest_continuous_sum([1,2,-1,-32,4,10,10,-10,-1]))