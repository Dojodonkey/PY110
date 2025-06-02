'''
Create a function that takes a list of integers as an argument
and returns the integer that appears an odd number of times.
There will always be exactly one such integer in the input list.

P:
- input: list
- output: integer

- explicits:
    - there will always be an integer in the input list that occurs three times.
        - return it.
- implicits:
    - if the list contains less than 3 elements, return the first one.

- questions:
    - the first test case only contains one element, it is returned.
        - what to do if the input list contains 2 elements? (not relevant for these test cases)

D:
- integer to represent the amount of occurrences we are looking for.
- set to iterate through unique elements avoiding repition.
    - or just short-circuit the return.
A:
- HL -
iterate through the input list. if an element occurs 3 times, return that element.

1. if the input list does not contain 3 elements, return the first element.
2. iterate through input list.
    - if an element occurrs 3 times, return it.

C:
'''
def odd_fellow(lst):

    return [num for num in lst if lst.count(num) % 2 != 0][0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)