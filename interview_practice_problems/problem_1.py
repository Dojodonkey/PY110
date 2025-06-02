'''
Create a function that takes a list of numbers as an argument.
 For each number, determine how many numbers in the list are smaller than it,
and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values.
 That is, if a number occurs multiple times in the list,
 it should only be counted once.

ExamplesCopy Code
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
The above tests should each print True.

P:
- input: list
- output: list

- explicits:
    - iterate through the input list. for each number, determine how many unique numbers are smaller than it.
        - no not include duplicates of smaller numbers.
    - place that count into a list to be returned.
- implicits:
    - if theres only one element in the list, return a list with 0 in it.
    - Theres always as many elements in the returned list as in the input list.

D:
- set to contain unique characters of the list.
- an integer to contain a count of smaller numbers.

A:
- High Level Strategy -
iterate through the input string. using a set, containing unique chars, check ordered comparison. if the element in the set,
is smaller, increase a 'counter' by 1.

1. init 'smaller_count' to an empty list.
2. init 'uniques' to a set based on input list.
3. iterate through input list.
    - init 'count' to 0.
    - compare to 'uniques' to find smaller elements.
        - if so, update, 'count' by 1.
    - append 'count' to 'smaller_count'
4. return 'smaller_count'.

C:
'''
def smaller_numbers_than_current(lst):
    smaller_count = []
    uniques = set(lst)

    for num in lst:
        count = 0
        for uni_num in uniques:
            if num > uni_num:
                count += 1
        smaller_count.append(count)

    return smaller_count


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)