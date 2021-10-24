## Fibonacci - Recursvely  ##
def cumulative_sum(inputNumber):
    # Base Case
    if inputNumber == 0:
        return 0
    # Recursively call function until we hit base case.   
    else:
        return inputNumber + cumulative_sum(inputNumber - 1)

print(cumulative_sum(5))