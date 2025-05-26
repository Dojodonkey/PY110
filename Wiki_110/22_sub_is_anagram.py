'''
Write a function `scramble(str1, str2)` that returns `True` if a portion of
`str1` characters can be rearranged to match `str2`, otherwise returns `False`.

Notes:
- Only lower case letters will be used (a-z). No punctuation or digits will
	be included.
- Performance needs to be considered.
- Input strings `str1` and `str2` are null terminated.

P:
- input: 2 arguments
    - string, potential substring
- output: bool

- explicits:
    - return True if chars in str2 are found in str1.
- implicits:
    - none

questions:
    - How to test performance?

D:
- list that contain chars of strings.

A:
- high level-
iterate through 'str2' and
then let's check if all of them are in 'str1'.

C:
'''
def scramble(str1, str2):
    return all(char in str1 for char in str2)


print(scramble('rkqodlw', 'world')) # should return True
print(scramble('cedewaraarossoqqyt', 'carrot')) # should return True
print(scramble('katas', 'steak')) # should return False
print(scramble('scriptjava', 'javascript')) # should return True
print(scramble('scriptingjava', 'javascript')) # should return True