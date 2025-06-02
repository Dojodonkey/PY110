'''
Create a function that takes a list of integers as an argument
and returns the number of identical pairs of integers in that list.
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice,
count each complete pair once.
For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2],
the function should return 2.
The first list contains two complete pairs
while the second has an extra 2 that isn't part of the other two pairs.

P:
- input: list
- output: integer

- explicits:
    - return the amount of pairs in the input list.
    - a pair is two elements of the same integer.
- implicits:
    - empty list returns 0.
    - all elements in input list are positive integers.

- questions: none

D:
- set to contain all unique integers of input list.
    - as to not iterate over all integers in the list, if we already know the amount of occurrences.
- dictionary with keys being integers and occurrences being values.
- integer to keep count of pairs.
    - updates as pairs are found.

A:
- HL -
create a set containing elements of input list.
iterate through that set and find the amount of occurrences of each char.
if the count of the char is greater than 1, find pairs by returning the occurrences divided by 2 (floor division).
then update a counter by that returned value.

1. init 'unique_ints' to a set made up of elements from input list.
2. init 'pairs_count' to 0.
3. iterate through 'unique_ints'.
    - if the occurrences of that char in the input string is greater than 1.
        - 'amount' is assigned to the return value of the occurrences divided by 2 (floor division).
        - reassign 'pairs_' to the value assigned to 'pairs_' plus 'amount_of_pairs'.
4. return 'pairs_'

C:
'''
def pairs(lst):
    lst_set = set(lst)
    pairs_count = 0

    for char in lst_set:
        if lst.count(char) > 1:
            amount = lst.count(char) // 2
            pairs_count += amount

    return pairs_count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)