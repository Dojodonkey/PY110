'''
Create a function that takes a list of numbers,
all of which are the same except one.
Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers,
and there will always be exactly one number that is different.

P:
- input: list
- output: integer

- explicits:
    - the input list contains a single element that is not the same as the rest.
        - return it.
- implicits:
    - none

- questions: none

D:
- integer to represent occurrences of element in list.
- set as not only iterate through 2 elements, avoiding repition.

A:
- HL -
iterate through the list.
if an element only occurs once, return it.
'''
def what_is_different(lst):
    lst_set = set(lst)

    for num in lst_set:
        if lst.count(num) == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)