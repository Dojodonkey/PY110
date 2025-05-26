'''
A pangram is a sentence that contains every single letter of the alphabet at
least once. Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.

P:
- input: string
- output: bool value

- explicits:
    - if the input string contains every letter of the alphabet, return True.
    if not, False.
- implicit rules:
    - case-insesitive

- questions: none

E:
panagram?("The quick brown fox jumps over the lazy dog.") # should return True
panagram?("This is not a pangram.") # should return False

D:
- string to contain all letters of the alphabet

A:
- High Lvl:
create a variable, 'alphabet' assigned to a string containing every letter of the alphabet.
then iterate through input string, ignoring spaces, and check if each char is in 'alphabet'.

1. init 'alphabet' to 'abcd...'
2. check if all letters of every word are in 'alphabet'

C:
'''

def panagram(strng):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(char in strng for char in alphabet)

print(panagram("This is not a pangram.")) # should return False
print(panagram("The quick brown fox jumps over the lazy dog.")) # should return True