'''
Write a function `longest(s)` that finds and returns the longest substring of
`s` where the characters are in alphabetical order.

P:
- input: string
- output: string

- explicits:
    - return the longest possible substring in alphabetic order in the string.
- implicits:
    - strings can contain any order of chars and be any length.

- questions: none

D:
- string for output

A:
- High Level Strategy-
init 'alpha_sub' to an empty string and then iterate over the input string.
if the value of the char is less than all the chars after it, add it to 'alpha_sub'.
if not, break.

1. init 'alpha_sub' to an empty string.
2. init 'sub' to the first char of input string.
2. iterate over input string beginning with the second char.
    -if the char is greater than or equal to the previous char, add it.
    - if not, check if the length of 'sub' is greater than 'alpha_sub'.
        - if it is, 'alpha_sub' is reassigned to 'sub'.
        - 'sub' is reassigned to the char.
3. return 'alpha_sub'
'''
def longest(strng):
    if not strng:
        return ''

    sub = strng[0]
    max_sub = sub

    for i in range(1, len(strng)):
        if strng[i] >= sub[-1]:
            sub += strng[i]
        else:
            sub = strng[i]

        if len(sub) > len(max_sub):
                max_sub = sub

    return max_sub

print(longest('asd'))                  # should return 'as'
print(longest('nab'))                  # should return 'ab'
print(longest('abcdeapbcdef'))         # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf')) # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag'))        # should return 'fgikl'
print(longest('z'))                    # should return 'z'
print(longest('zyba'))                 # should return 'z'