# Example of Recursion with Factorials.

# def factorial(inputNumnber):
#     if(inputNumnber == 0):
#         return 1
#     else:
#         return inputNumnber * factorial(inputNumnber - 1)



# print(factorial(5))

# Example Problems 

# Problem 1
# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
# For example, if n=4 , return 4+3+2+1+0, which is 10.

# def cumulativeSum(inputNumber):
#     if(inputNumber) == 0:
#         return 0
#     else:
#         return inputNumber + cumulativeSum(inputNumber - 1)


# print(cumulativeSum(4))

# Problem 2
# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1

# def sumDigits(inputNumber):
#     if inputNumber < 10:
#         return inputNumber
#     else:
#         return inputNumber % 10 + sumDigits(inputNumber // 10)


# print(sumDigits(4321))

# Problem 3
# Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're ignoring strict requirements here.
# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

# def word_split(phrase, list_of_words):
#     new_list = []
    
#     for word in list_of_words:
#         if word in phrase:
#             new_list.append(word)
#     return new_list


# print(word_split("themanran",['clown','ran','man']))
# print(word_split("ilovedogsjohn", ['i', 'am', 'a', 'dogs', 'lover', 'love', 'john']))
# print(word_split("thename", ["the", "then", "name"]))