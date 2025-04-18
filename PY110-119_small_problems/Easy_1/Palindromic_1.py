'''
Problem Statement:
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise.
A palindrome reads the same forwards and backwards.
For this problem, the case matters and all characters matter.

- Understanding the Problem:
    - input: string
    - output: boolean values, True or False

    explicit rules:
    - write a function
    - if the string reads the same forward as backwards, return True. Otherwise return False.
    - case matters
    - all characters matter

    implicit rules:
    - input must be a string

    questions:
    - should the function check if the input is a string and if not display a warning message?

- Examples/Test Cases:
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

- all rules confirmed

Data Structures:
- strings to compare input

Algorithm:
    1. define 'is_palindrome' function that accepts 1 parameter, 'strng'.
    2. function should return the value returns by an expression comparing 'strng' and 'strng' in reverse.

Code:
'''
def is_palindrome(strng):
    return strng == strng[::-1]

# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)