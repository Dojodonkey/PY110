'''
Problem Statement:
Write a function that takes a list of integers between 0 and 19
and returns a list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine,
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

Understanding the Problem:

- input: list
- output: list

- Explicit rules:
    - input list contains integers between 0 and 19.
    - function will return a sorted list based on the english word of each integer.
- Implicit rules:
    - a helper function will be useful to match each integer with their english word equivalent.
    - we can use the sort method or sorted function.

- Questions: none

Test Case/Example:

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

- Observations:
    - output list is sorted by ascending order of the integers english equivalent

Data Structures:

- list
- strings

Algorithm:

1. write a helper function which takes an integer and returns its english equivalent.
2. sort the input list based on the helper function.
3. return the sorted function.

Code:
'''
import inflect

p = inflect.engine()

def num_eng(num):
    return p.number_to_words(num)

def alphabetic_number_sort(lst):
    lst.sort(key=num_eng)
    return lst

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True