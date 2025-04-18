'''
Problem Statement:
In the previous exercise, you developed a function that converts simple numeric strings to integers.
In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer.
The string may have a leading + or - sign; if the first character is a +, your function should return a positive number;
if it is a -, your function should return a negative number.
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int.
You may, however, use the string_to_integer function from the previous exercise.

Understanding the Problem:

- input: string
- output: integer

- explicit rules:
    - if first char is '+' return the integer as a positive number.
    - if first char is '-' return the integer as a negative number.
    - if there is no leading character, return the integer as a positive number.
    - string will always contain a valid number. (no need to check for numeric characters).
    - use of built-in functions is prohibited.
- implicit rules:
    - none

- questions:
    - none

Examples/Test Cases:

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

- understanding confirmed

Data Structures:
- Dictionaries to store mappings of characters and integers.
- integers to store totals.

Algorithm:

1. define 'string_to_signed_integer' to accept 1 parameter, 'string_of_nums'.
2. initialize 'string_int_map' to a dictionary containing numerical chars as keys and integers as values accordingly.
    - try to use a ternary expression if possible.
3. initialize 'count' to 0.
4. initialize 'factor' to 1.
5. iterate through the 'string_of_nums' beginning at the last index and iterating backwards.
    1. if char is '-' multiply 'count' by -1 and then continue to finish iterating.
    2. if char is '+' continue to finish iterating.
    3. use the value mapped by the key, char.
        - multiply the value by factor and add it to count.
6. return count

Code:
'''
def string_to_signed_integer(string_of_nums):
    string_int_map = {str(num): num for num in range(10)}
    count = 0
    factor = 1

    for char in string_of_nums[::-1]:
        if char == '-':
            count *= -1
            continue
        if char == '+':
            continue

        value = string_int_map[char]
        count += value * factor
        factor *= 10

    return count

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
print(string_to_signed_integer("+2345332") == 2345332)   # True