'''
Problem Statement:
Write a function that counts the number of occurrences of each element in a given list.
Once counted, print each element alongside the number of occurrences.
Consider the words case sensitive e.g. ("suv" != "SUV").

Understanding the problem:

- input: lst
- output: string

- explicit rules:
    - first count the occurrences of each element in a given list.
    - print each element alongside the number of occurrences
        - one pair at a time!
    - case matters, upper and lower case are NOT the same.
- implicit rules:
    - none

- questions: none

Examples/Test Cases:

# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

Data Structure:

- dictionary

Algorithm:

1. define 'count_occurrences' to accept 1 parameter, 'lst'.
2. use an initially empty dictionary to store elements from 'lst' as keys,
and occurrences as values.
3. iterate over the dictionary.
    - at each iteration, a key and value.

Code:
'''
def count_occurrences(lst):
    count_dict = {element : lst.count(element) for element in lst}
    for key, value in count_dict.items():
        print(f'{key} ==> {value}')



vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2