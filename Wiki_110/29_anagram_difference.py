# Given two words, determine the number of letters you need to remove from them to make them anagrams.

'''
P:
- input: two strings.
- output: integer

- explicit rules:
    - determine the number of letters you need to remove from both strings to make them anagrams.
- implicit rules:
    - none

questions: none

E:
print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba')  == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)

- observations:
    - strings can be of different lengths.
    - one or both strings can be empty.

D:
- list to contain different chars between both strings.

A:
- High Level:
firstly, check for edge cases, being when one or both strings are empty.
if both are empty, return 0.
if one is empty, return the length of the other.
Then we need to compare each letter from one string to the other.
    - if a letter is not in the other, append it to list.
return the length of that list after both strings have been compared to each other.

1. check for edge cases.
    if both strings are empty, return 0.
    if one string is empty, return the length of the other.
2. init an empty list to 'diff_chars'.
3. compare chars of 'str1' to 'str2'.
    if a char is not in 'str2' append it to 'diff_chars'
4. do step 3 comparing 'str2' to 'str1'
5. return the length of 'diff_chars'

C:
'''

def anagram_difference(str1 , str2):
    if not str1 and not str2:
        return 0
    if not str1 and str2:
        return len(str2)
    if not str2 and str1:
        return len(str1)

    diff_chars = []
    str_1_split = list(str1)
    str_2_split = list(str2)

    for char in str1:
        if char not in str2:
            diff_chars.append(str_1_split.pop(str_1_split.index(char)))

    for char in str2:
        if char not in str1:
            diff_chars.append(str_2_split.pop(str_2_split.index(char)))

    if len(str_1_split) > len(str_2_split):
        while len(str_1_split) != len(str_2_split):
            diff_chars.append(str_1_split.pop())
    if len(str_1_split) < len(str_2_split):
        while len(str_2_split) != len(str_1_split):
            diff_chars.append(str_2_split.pop())

    return len(diff_chars)

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba')  == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)