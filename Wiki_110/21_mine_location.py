'''
You've just discovered a square (NxN) field and you notice a warning sign.
The sign states that there's a single bomb in the 2D grid-like field in front
of you.

Write a function `mine_location` that accepts a 2D array, and returns the
location of the mine. The mine is represented as the integer 1 in the 2D array.
Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array where the first element is the row index,
and the second element is the column index of the bomb location (both should be 0 based).
All 2D arrays passed into your function will be square (NxN),
and there will only be one mine in the array.

P:
- input: list
- ouput: list ([row, column])

- explicits:
    - return a list containing the row and column of the mine.
        - the row is the index of the list the mine is in.
        - column is the index within that list that the mine is in.
- implicits:
    - can contain any number of sublists and amount of elements within those lists.

- questions: none

D:
- list to contain row and column indexes.
- range to iterate through sublists (or not?)

A:
- High Level-
iterate through the input list, find the row and column containing 1 and return those in a list.

1. iterate through input list.
2. if 1 is in the sublist, assign 'row' is assigned to the index of the sublist.
'column' is assigned to the index of 1 within that sublist.
3. return a list containing 'row' and 'column'

C:
'''
def mine_location(minefield):
    for row in minefield:
        if 1 in row:
            mine_row = minefield.index(row)
            mine_column = row.index(1)
    return [mine_row, mine_column]

print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # should return [1, 1]
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]])) # should return [2, 1]
print(mine_location([[1, 0], [0, 0]])) # should return [0, 0]
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])) # should return [2, 2]
