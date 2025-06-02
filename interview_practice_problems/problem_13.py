'''
Create a function that takes two strings as arguments
and returns True if some portion of the characters
in the first string can be rearranged to match the characters in the second.
Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters.
Neither string will be empty.

P:
- input: 2 strings
- output: bool

- explicits:
    - if a substring of the first string can be rearranged to match chars of second string,
    return True, otherwise False.
    - both strings are all lower case and never empty.
- implicits:
    - none

- questions: none

D:
- list to contain chars.

A:
- check if all the chars in the second string and in the first string.

C:
'''
def unscramble(str1, str2):
    # check if chars in str1 can be rearranged to match str2.
    return all(char in str1
               and str1.count(char) == str2.count(char)
               for char in str2)

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)