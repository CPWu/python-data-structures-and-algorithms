# Sentence Reversal

## Problem

Given a string of words, reverse all the words.

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

## Example

Return: 'best the is This'
```
'This is the best'
```

## Solution

We could take advantage of Python's abilities and solve the problem with the use of split() and some slicing or use of reversed:

```
def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])
```
```
rev_word1('Hi John,   are you ready to go?')
```
```
rev_word2('Hi John,   are you ready to go?')
```

