'''
Problem Statement:
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers.
In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on)
to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str.
Your function should do this the old-fashioned way
and construct the string by analyzing and manipulating the number.

Understanding the Problem:

- input: integer
- output: string

- explicit rules:
    - convert integer value to a string representation of that integer.
    - no use of built-in functions is permitted.
- implicit rules:
    - none

- questions:
    - none

Examples/Test Cases

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

- understanding confirmed

Data Structures:
    - Dictionary to map integer values (0-9) to string equivalants ('0'-'9')
    - string to store string values (to be returned)

Algorithm:

1. define function 'integer_to_string' to accept 1 parameter, 'number'.
2. initialize 'int_str_map'
    - use integers as keys and the string equivalant as values
        - 0-9 and '0'-'9'
3. initialize 'str_result' to an empty string.
4. while 'number' is greater than 10:
    1. initialize 'digit' to the result returned by 'number' % 10.
    2. add the value represented by the key 'digit' in 'int_str_map' to 'str_result'.
        - by initializing 'value' to the value mapped to the key 'digit'.
    3. use floor division on 'number' by 'value, reassigning 'number' to the result.
5. add the value mapped to 'number' in 'int_str_map' to 'str_result'.
6. return 'str_result' in reverse order.

Code:
'''
def integer_to_string(number):
    int_str_map = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    str_result = ''
    while number > 10:
        digit = number % 10
        value = int_str_map[digit]
        str_result += value
        number //= 10

    value = int_str_map[number]
    str_result += value

    return str_result[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True