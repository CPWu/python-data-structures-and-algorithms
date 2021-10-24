# O(n) time | O(d) space - where n is the total number of elements in the array, including sub-elements, and id is the greatest depth of "special" arrays in the array.
def productSum(array, multiplier = 1):
    # Variable to keep track of sum
    sum = 0   
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))