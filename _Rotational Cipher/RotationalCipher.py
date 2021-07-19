# Time Complexity: O(N^2)
# Space Complexity: O(1)
def rotationalCipher(input, rotation_factor):
    lowercase = ("abcdefghijklmnopqrstuvwxyz") # 26
    uppercase = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # 26
    numbers = ("0123456789") # 10
    encryptedString = []
    # Check whether the input string is alphanumeric
    for character in input:
        if character in lowercase:
            encryptedString.append(getNewLowerValue(character, rotation_factor, lowercase))
        elif character in uppercase:
            encryptedString.append(getNewUpperValue(character, rotation_factor, uppercase))
        elif character in numbers:
            encryptedString.append(getNewNumericValue(character, rotation_factor, numbers))
        else:
            encryptedString.append(character)
    return "".join(encryptedString)

def getNewLowerValue(character, rotation_factor, lowercase):
    new_rotational_factor = rotation_factor % 26
    newValueCode = lowercase.index(character) + new_rotational_factor
    return lowercase[newValueCode] if newValueCode <= 25 else lowercase[-1 + newValueCode % 25]

def getNewUpperValue(character, rotation_factor, uppercase):
    new_rotational_factor = rotation_factor % 26
    newValueCode = uppercase.index(character) + new_rotational_factor
    return uppercase[newValueCode] if newValueCode <= 25 else uppercase[-1 + newValueCode % 25]

def getNewNumericValue(character, rotation_factor, numbers):
    new_rotational_factor = rotation_factor % 10
    newValueCode = numbers.index(character) + new_rotational_factor
    return numbers[newValueCode] if newValueCode <= 9 else numbers[-1 + newValueCode % 9]

input = "Zebra-493?"
rotationFactor = 3
print(rotationalCipher(input, rotationFactor))