'''
Problem 1: Count Character Frequency
Difficulty​: Intermediate
Create a function that takes a string argument
and returns a dictionary where the keys are the lowercase letters
in the string and the values represent how often each letter occurs.
Ignore non-alphabetic characters.

P:
- input: string
- output: dictionary

- explicits:
    - return a dictionary with lower case chars as keys and occurrences as values.
- implicits:
    - some strings contain only none alphabetic keys.
        - guard clause

D:
- dictionary to be returned.
- integer to represent occurrences of lower case char.
- string to represent lower case char.
- bool to check if a char is lower case and alphabetic.
- set containing unique chars of input string.
    -avoid unnecessary iterations.

A:
-HL-
iterate through set of chars based on input string.
if a char is lower case and alphabetic, add that char as a key and occurrences as value.

- guard clause: if all chars in input string are non-alpha, return an empty dict.
1. init 'strng_set' to a set based on chars from input string.
2. init 'lower_dict' to an empty dict.
3. iterate through 'strng_set'.
    - add char as a key mapped to occurrences as values.
4. return 'lower_dict'.

C:
'''
def count_letters(string):
    """
    Count the frequency of each letter in a string, ignoring non-alphabetic characters.
    Letters are case-insensitive (a and A count as the same letter).

    Args:
        string: A string to analyze

    Returns:
        A dictionary with lowercase letters as keys and their frequency as values
    """
    if all(not char.isalpha() for char in string):
        return {}

    string = string.lower()
    return {char: string.count(char) for char in set(string)
            if char.isalpha()}

# Test cases
print(count_letters('woebegone') == {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1})
print(count_letters('lowercase/uppercase') == {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2, 'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2})
print(count_letters('W. E. B. Du Bois') == {'u': 1, 'o': 1, 'i': 1, 's': 1, 'b': 2, 'd': 1, 'e': 1, 'w': 1})
# test case still incorrect as 'B' occurs twice.
print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
'''Problem 2: Even-Numbered Substrings
Difficulty​: Advanced
Create a function that takes a string of digits as an argument
and returns the number of even-numbered substrings that can be formed.
If a substring occurs more than once, count each occurrence as a separate substring.
For example, in the string '1432':
•   Even-numbered substrings: '14', '1432', '4', '432', '32', '2'
•   Total: 6 substrings
'''
# def even_substrings(string):
#     """
#     Count the number of even-numbered substrings that can be formed from a string of digits.

#     Args:
#         string: A string containing only digits

#     Returns:
#         An integer representing the count of even-numbered substrings
#     """
#     # Your solution here
#     pass

# # Test cases
# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)