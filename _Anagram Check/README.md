# Anagram Check

## Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

## Example

```
"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
```

Return: True
```
anagram('dog','god')
```

Return: True
```
anagram('clint eastwood','old west action')
```

Return: False
```
anagram('aa','bb')
```

## Solution
There are two ways of thinking about this problem, if two strings have the same frequency of letters/element (meaning each letter shows up the same number of times in both strings) then they are anagrams of eachother. On a similar vien of logic, if two strings are equal to each other once they are sorted, then they are also anagrams of each other.