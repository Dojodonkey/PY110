'''
Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example: the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
*/

Understanding the Problem:
- input: string
- output: boolean value

- explicit rules:
    - if the input string contains every letter of the alphabet, return True, otherwise False.
    - numbers and punctuation is ignored.
    - case insensitive.
- implicit rules:
    - none

- questions: none

Examples/ Test Cases:

// # Python test cases:
// print(isPangram('The quick brown fox jumps over the lazy dog.') == True)
// print(isPangram('This is not a pangram.') == False)

- understanding confirmed.

Data Structures:

- string to iterate through and check for membership.

- High Level Strategy:
    - iterate through a string containing all letters of the alphabet and
    check for membership in the input string.

Algorithm:

1. create a string containing all letters of the alphabet.
2. iterate through that string and check for membership in the input string.
    - if any of the chars in 'alphabet' are not in the input string, return the bool value False.
    - otherwise return True.
'''

def is_pangram(strng):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        if char.lower() not in strng:
            return False

    return True

# Python test cases:
print(is_pangram('The quick brown fox jumps over the lazy dog.') == True)
print(is_pangram('This is not a pangram.') == False)
