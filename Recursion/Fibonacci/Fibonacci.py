## Fibonacci - Recursvely  ##
def fibonacci_recursion(inputNumber):
    # Base Case(s)
    # If input number is 0, return is 0
    # If input number is 1, return is 1
    # If input number is 2, return is 2
    # Cast to int to prevent decimals.
    if (inputNumber <= 2):
        return int((inputNumber+1)/2)
    # Recurivelty call function until we hit base cases.
    else:
        return fibonacci_recursion(inputNumber - 1) + fibonacci_recursion(inputNumber -2)

print(fibonacci_recursion(2))

## Fibonacci - Dynamically ##
def fibonacci_dynamically(inputNumber):
    # Create a cache of length of input
    cache = [None] * (inputNumber + 1)
    if cache[inputNumber] is not None:
        return cache[inputNumber]
    # Base Case(s)
    # If input number is 0, return is 0
    # If input number is 1, return is 1
    # If input number is 2, return is 2
    # Cast to int to prevent decimals.
    if inputNumber <= 2:
        cache[inputNumber] = int((inputNumber + 1)/2)
    # Recurivelty call function until we hit base cases.
    else:
        cache[inputNumber] = fibonacci_dynamically(inputNumber - 1) + fibonacci_recursion(inputNumber - 2)
    return cache[inputNumber]

print(fibonacci_dynamically(10))

## Fibonacci - Iteratively ##
def fibonacci_iteratively(inputNumber):
    # Set starting values
    a = 0
    b = 1

    # Follow Algorithm
    for i in range(inputNumber):
        a, b = b, a + b
    return a

print(fibonacci_iteratively(6))