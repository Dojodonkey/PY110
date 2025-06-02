'''
Create a function that takes a list of integers as an argument and returns a tuple of two numbers
 that are closest together in value.
 If there are multiple pairs that are equally close,
 return the pair that occurs first in the list.

P:
- input: list
- output: tuple (containing two integers)

- explicits:
    - return a tuple with two elements from the input list that are closest in value.
        - almost the same in value.
- implicits:
    - lists contain no duplicates.

D:
- integer to keep value of two elements subtracted (to find difference).
    - the two elements with the smallest difference will be returned in the tuple.
- tuple to be returned.

A:
- HL -
iterate through the input list, comparing each integer with all the others. Find the smallest difference.
Keep track of it. Upon the next iteration, if its smaller, then reassign the tuple with integers.

1. init 'min_tup' to an empty tuple.
2. iterate through input list.
    - init 'min_diff' to 0.
    - init 'min_pair' to an empty tuple.
    - find the difference between the selected integer and all the others.
        - if the diff is smaller or 'min_diff' is assigned to 0, create an array containing those two integers.
    - if the difference is less than the difference of 'min_tup', reassign 'min_tup'
3. return 'min_tup'
'''

def closest_numbers(lst):
    # min_tup = ()
    # min_diff = 0

    # for i in range(1,len(lst)):
    #     for j in range(len(lst)-1):
    #         if i == j:
    #             continue
    #         tup_ = (lst[j], lst[i])
    #         diff_ = abs(lst[j] - lst[i])
    #         if diff_ < min_diff or min_diff == 0:
    #             min_diff = diff_
    #             min_tup = tup_


    # return tuple(sorted(min_tup, key=lst.index))

    min_diff = float('inf')
    min_pair = None

    # Compare every pair of numbers
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  # Only compare with elements after the current one
            diff = abs(lst[i] - lst[j])

            if diff < min_diff:
                min_diff = diff
                min_pair = (lst[i], lst[j])

    return min_pair

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))