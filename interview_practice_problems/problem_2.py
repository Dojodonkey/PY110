'''
Create a function that takes a list of integers as an argument.
The function should return the minimum sum of 5 consecutive numbers in the list.
If the list contains fewer than 5 elements, the function should return None.

P:
- input: list
- ouput: integer

- explicits:
    - if the input list, contains fewer than 5 elements, return None.
    - find the minimum sum of 5 consecutive elements.
- implicits:
    - input list can contain neg nums.
        - min sum can be neg.

- questions: none

D:
- integer to keep 'minimum_sum'.
- range to find 5 consecutive elements.

A:
- High Level Strategy -
iterate through the input list, 5 consecutive elements at a time. find the sum and keep it to be compared with
the next iteration. If the sum is less, that is the new 'min_sum'.

1. if total length of input list is less than 5, return None.
2. init 'min_sum' to 0.
3. iterate through input list.
    - using 5 consecutive elements:
        - find the sum and compare to 'min_sum'.
            - if less than, reassign 'min_sum'.
4. return 'min_sum'

C:
'''

def minimum_sum(lst):
    if len(lst) < 5:
        return None

    min_sum = 0

    for i in range(0, len(lst) - 4):
        sum_ = sum(lst[i : i + 5])
        if sum_ < min_sum or min_sum == 0:
            min_sum = sum_

    return min_sum

# ExamplesCopy Code
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# The above tests should each print True.