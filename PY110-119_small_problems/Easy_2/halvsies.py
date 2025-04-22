'''
Problem Statement:

Write a function that takes a list as an argument and returns a list that contains two elements,
both of which are lists.
Put the first half of the original list elements in the first element of the return value
and put the second half in the second element.
If the original list contains an odd number of elements,
place the middle element in the first half list.

Understanding the Problem:

- input: list
- output: list containing two nested lists

- explicit rules:
    - The function should return a list containing two nested lists.
        - the first list contains elements from the first half of the input list.
        - the second list contains elements from the second half.
        - if the input list has an uneven amount:
            - the element of the middle index should be placed in the first nested list.
- implicit rules:
    - the input list can contain an odd or even amount of elements.

- questions: none

Examples/Test Cases:

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

- observations:
    - if the input list contains 1 element, it is contained in the first nested list,
    and the second nested list is empty.
    - if the input list is empty, return a list with two empty nested lists.

Data Structures:

    - lists

Algorithm:

1. define 'halvsies' to accept 1 parameter, 'input_lst'.
2. check if 'input_lst' is empty.
    - if so, return a list containing two empty lists.
3. initialize 'lst_1' to an empty list.
4. initialize 'lst_2' to an empty list.
5. check if 'input_list' contains an even amount of elements.
    - if so append the elements in the first half to 'lst_1',
    and append the elements in the second half to 'lst_2'.
    - if not, append the first half plus the next element to 'lst_1',
    and the rest of the elements to 'lst_2'.
6. return a list litural contain 'lst_1' and 'lst_2'.

Code:
'''
def halvsies(input_lst):
    if not input_lst:
        return [[], []]

    if len(input_lst) % 2 == 0:
        lst_1 = input_lst[:len(input_lst) // 2]
        lst_2 = input_lst[len(input_lst) // 2:]
    else:
        lst_1 = input_lst[:(len(input_lst) // 2) + 1]
        lst_2 = input_lst[(len(input_lst) // 2) + 1:]

    return [lst_1, lst_2]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
