'''
Problem Statement:
Write a function that takes a string of digits and returns the appropriate number as an integer.
You may not use any of the standard conversion functions available in Python, such as int.
Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs,
nor should you worry about invalid characters; assume all characters are numeric.

Understanding the Problem:
- input: string
- output: int

- explicit rules:
    - input is a string.
    - output is the char of the string converted to an integer.
    - no use of built-in functions is permitted.
- implicit rules:
    - none

- questions:
    - none

Test Cases/Examples:

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

- understanding confirmed.

Data Structures:
    - Dictionaries
        - mapping strings to integers

Algorithm:

    1. define 'string_to_integer' to accept 1 parameter, 'strng_of_nums'.
    2. initialize 'str_int_map' to a dictionary.
        - keys are string values '0'-'9'.
        - values are integer values 0-9.
    3. initialize 'count' to 0.
    4. initialize 'factor' to 1.
    5. iterate through 'strng_of_nums' beginning at the last index and iterating backwards.
        1. use the value in 'str_int_map' mapped to the char in 'strng_of_nums'.
        2. multiply that value by 'factor' and add it to 'count'.
        3. reassign 'factor' to 'factor' times 10.
    6. return 'count'

Code:
'''
def string_to_integer(strng_of_nums):
    str_int_map = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    count = 0
    factor = 1

    for num in strng_of_nums[::-1]:
        value = str_int_map[num]
        count += value * factor
        factor *= 10

    return count

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("10403") == 10403) # True