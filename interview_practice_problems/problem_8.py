'''
Create a function that takes a non-empty string as an argument.
The string consists entirely of lowercase alphabetic characters.
The function should return the length of the longest vowel substring.
The vowels of interest are "a", "e", "i", "o", and "u".

P:
- input: string
- output: integer

- explicits:
    - find all the substrings of the input string that consist of only vowels.
    - return the length of the lowest substring.
- implicits:
    - strings with no vowels return 0.
    - a single vowel is also considered a substring.

- questions:

D:
- list containing all the vowel substrings.
- range to iterate through the input string.
- string to build substrings.
- integer to store the length of substring.
- dictionary that contains vowel substrings as keys and lengths as values.

A:
- HL -
find all the substrings in the input string and store them in a list.
return the length of the longest substring in that list.

1. init 'vow_subs' to an empty list.
2. iterate through the input string.
    - init 'sub_' to an empty string.
    - if the char is a vowel, concatenate it to 'sub_'.
    - if not, append 'sub_' to 'vow_subs' and continue to next iteration.
3. init 'longest_sub' to the longest string in 'vow_subs'.
4. return the length of 'longest_sub'.
'''
def longest_vowel_substring(strng):
    vow_subs = []
    vowels = 'aeiou'

    sub_ = ''
    for char in strng:
        if char in vowels:
            sub_ += char
        else:
            vow_subs.append(sub_)
            sub_ = ''

        if char == strng[-1]:
            vow_subs.append(sub_)

    longest_sub = max(vow_subs, key=len)

    return len(longest_sub)






print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)