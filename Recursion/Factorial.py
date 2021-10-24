## Factorial - multiply all whole numbers from input number down to 1.
def factorial(inputNumber):

    # Base Case
    if (inputNumber == 0):
        return 1
    # Recurivelty call function until we hit base case.
    else:
        return inputNumber * factorial(inputNumber - 1)

print(factorial(5))