'''
# Write a method that takes an array of consecutive (increasing) letters as input
# and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

P:
- input: list of chars
- output: string of missing char.

- explicits:
    - return the missing char from a consecutive (increasing) list of chars.
    - all chars in list are either uppercase or lowercase.
    - leng of list will be atleast 2 chars.
    - there is always exactly one char missing.

D:
- integer to contain value of chars.

A:
- High level Strategy -
iterate through the input list, each char should be one value greater than the previous char.
if it is not, return the char that is one value greater.

1. iterate over input list beginning at the first index.
    - check that it is one value greater than the previous char.
        - ord()
    - if it is not, return the char that should be there to ensure successive order.


p find_missing_letter(['a','b','c','d','f']) == 'e'
p find_missing_letter(['O','Q','R','S']) == 'P'
'''

def find_missing_letter(lst):
    for i in range(1, len(lst)):
        if ord(lst[i]) - ord(lst[i-1]) != 1:
            return chr(ord(lst[i-1]) + 1)

print(find_missing_letter(['a','b','c','d','f']) == 'e')
print(find_missing_letter(['O','Q','R','S']) == 'P')