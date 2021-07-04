def productSum(array, multuplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multuplier + 1)
        else:
            sum += element
    return sum * multuplier