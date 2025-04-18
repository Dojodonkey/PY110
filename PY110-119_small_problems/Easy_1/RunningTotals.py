'''
Problem Statement:
Write a function that takes a list of numbers and returns a list with the same number of elements,
but with each element's value being the running total from the original list.

- Understanding the Problem:
    input: list
    output: list

    explicit rules:
    - function is passed in a list
    - return a new list with the same number of elements as the list passed in.
    - new list elements are the running total from the original list.

    implicit rules:
    - the first element in the new list is the same as the first element of the original list.

    questions:
    - none

- Examples/Test Cases:
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

- if an empty list is passed, return an empty list.
- rules confirmed.

Data Structures:
- List

Algorithm:
1. function 'running_total' accepts 1 parameter, 'lst'.
2. if 'lst' is empty, return an empty list.
3. initialize 'running_lst' to list containing only the first element of 'lst'.
4. iterate through 'lst' beginning at the second index ([1]).
5. each iteration should take the element in 'lst', add it to previous element in 'running_list',
and append that total to 'running_lst'.
6. the function returns 'running_lst'.

code:
'''
def running_total(lst):
    #check if lst is empty
    if not lst:
        return []
    running_lst = [lst[0]]
    for i in range(1, len(lst)):
        running_lst.append(running_lst[i - 1] + lst[i])
    return running_lst

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True