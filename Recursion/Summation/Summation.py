## Fibonacci - Recursvely  ##
def summation(inputNumber):
    # Base Case
    if inputNumber < 10:
        return inputNumber
    # Recursively call function until we hit base case.    
    else:
        return inputNumber % 10 + summation(int(inputNumber/10))

print(cumulative_sum(5))