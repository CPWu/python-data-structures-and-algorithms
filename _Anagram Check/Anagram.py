# Two approaches, if two strings are anagrams than the sorted character of the string compared to each other should be equal. Alternative the frequency of ocurrence
# for characters in one string should be equal to the frequency of ocurrence in characters in the other string.

def anagram(first_string, second_string):
    # Filter the strings removing spaces and capatilization
    filtered_first_string = first_string.replace(' ','').lower()
    filtered_second_string = second_string.replace(' ','').lower()

    return sorted(filtered_first_string) == sorted(filtered_second_string)




def anagram2(first_string, second_string):
    # Filter the strings, removing spaces and capatilization
    filtered_first_string = first_string.replace(' ','').lower()
    filtered_second_string = second_string.replace(' ','').lower()
    
    # Remove one possibility if length of strings don't match there is no way there can be an anagram.
    if len(filtered_first_string) != len(filtered_second_string):
        return False

    # Counting dictionary
    # We could use a default dictionary from the collections module but we will use the base dictionary structure
    count = {}

    # Fill dictionary with the character count of first string
    for letter in filtered_first_string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Fill the dictionary again but substracting from the count.
    for letter in filtered_second_string:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # If all counts are equal to 0 then we know its an anagram.
    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram('dog','god'))

print(anagram2('clint eastwood','old west action'))