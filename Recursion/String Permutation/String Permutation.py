# Iterate through the initial string – e.g., ‘abc’.
# For each character in the initial string, set aside that character and get a list of all permutations of the string that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.
# Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.
# Return the list of final results.
def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]
    else:
        # For every letter in string
        for i, let in enumerate(s):
            # For every permutatioon resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                # Add it to output
                out += [let + perm]

    return out

print(permute('abc'))