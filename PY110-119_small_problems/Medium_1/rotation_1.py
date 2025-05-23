'''
Write a function that rotates a list by moving the first element to the end of the list.
Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

P:

- input: list
- output: new list

- explicit rules:
    - function returns a new list, with the first element moved to the end of the list.
    - if the list is empty, return an empty list.
    - if the input is not a list, return None.
- implicit rules:
    - empty list is an edge case.
    - the function checks for the data type of input.

- questions: none

E:
# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

- observations:
    - input list may contain different data types or a mix of data types.

D:

- a new list with the first element of the input list now as the last element.

High Level Strategy:

- Take a list and return a new list with the first element of the input list now as the last element
and all other elements in the same order.

A:
1. create a new list containing all elements of the input list except the first.
2. concatenate the new list with a list containing the the first element of the input list.

C:
'''
def rotate_list(lst):
    # edge cases:
    if lst == []:
        return []
    if isinstance(lst, list) == False:
        return None

    return lst[1:] + [lst[0]]




# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])