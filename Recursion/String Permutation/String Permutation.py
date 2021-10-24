def reverse_string(string):
    # Base Case
    if len(string) <= 1:
        return string
    # Recursively call function until we hit base case.   
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("hello world"))