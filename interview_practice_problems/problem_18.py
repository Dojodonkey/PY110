'''
Create a function that takes a list of integers as an argument.
Determine and return the index N for which all numbers with an
index less than N sum to the same value as the numbers with an index greater than N.
If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0.
Likewise, the sum of the numbers to the right of the last element is 0.

P:
- input: list
- output: integer

- explicits:
    - return the index of which the sum of all indexes to the left and right of it are equal.
    - if this is not possible, return -1.
    - if there are two indexes at which both left and right sums are equal,
    return the lower value index.
    - the sum left of index 0 and the last index is 0.
- implicits:
    - input list may contain both pos and neg numbers.

D:
- list to contain all elements of indexes left and the right of an index.
- integer to represent the sum of lists.
- range to iterate through input list.

A:
- HL -
iterate through the input list, using the values of all indexes to the left and right of each index.
if those values are ever equal, return that index. Otherwise return -1.

1. iterate through input list.
    - if at the first index, the sum of 'left_sum' is 0.
    - if at the last index, the sum of 'right_sum' is 0.
    - 'left_sum' assigned to the sum of all elements to the left,
    'right_sum' assigned to the sum of all elements to the right.
    - if these two variables are ever equal, append them to an array.
2. if that array is empty, return -1.
    - if there are more than 1 element in it, return the smaller value.
    - there is only one element in the array, return it.

C:
'''
def equal_sum_index(lst):
    equalizers = []

    for i in range(len(lst)):
        if i == 0:
            left_sum = 0
            right_sum = sum(lst[1:])
        elif i == len(lst) - 1:
            left_sum = sum(lst[:-1])
            right_sum = 0
        else:
            left_sum = sum(lst[:i])
            right_sum = sum(lst[i+1:])

        if left_sum == right_sum:
            equalizers.append(i)

    if not equalizers:
        return -1
    else:
        return min(equalizers)

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)