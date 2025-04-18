'''
Problem Statement:
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise.
This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters.
If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

- Understanding the Problem:
    input: string
    output: boolean values True or False

    explicit rules:
    - if the string is a palindrome return True, otherwise False.
    - function should be case-insensitive
    - function should ignore all non-alphanumeric characters.
    implicit rules:
    - none

    questions:
    - none
- Test Cases/Examples
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

- rules confirmed.

Data Structures:
- converted strings containing only alphanumeric characters from input.

Algorithm:
    1. define 'is_real_palindrome' to accept one parameter, 'strng'.
    2. create a new string containing only alphanumeric characters and converted to lower case.
    3. function should return the return value of an expression comparing 'strng' to 'strng' in reverse.

Code:
'''
def is_real_palindrome(strng):
    alphanum_str = ''

    for char in strng:
        if char.isalnum():
            alphanum_str += char.lower()

    return alphanum_str == alphanum_str[::-1]



print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True