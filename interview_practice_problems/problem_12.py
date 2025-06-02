'''
Create a function that takes a string as an argument and returns True if the string is a pangram,
False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once.
For example, the sentence "Five quacking zephyrs jolt my wax bed."
is a pangram since it uses every letter at least once.
Note that case is irrelevant.

P:
- input: string
- output: bool

- explicits:
    - if every letter of the alphabet is in the input string, return True.
        - otherwise false.
    - case-insensitive
- implicits:
    - some word's have non-alpha chars.

- questions: none

D:
- string to store chars of the alphabet.

A:
- HL -
check if all the letters of the alphabet are in the string.

1. reassign input string to a lower case converted string.
2. init 'alphabet' to a string containing all chars of the alphabet.
3. check if all chars of 'alphabet' are in the input string.

C:
'''
def is_pangram(strng):
    strng = strng.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    return all(char in strng for char in alphabet)


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)