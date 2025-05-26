'''
# Create a function that takes two integer arrays of equal length,
# compares the value of each member in one array to the corresponding member in the other,
# squares the absolute value difference between those two values,
# and returns the average of those squared absolute value differences between each member pair.

P:
- input: 2 lists
- output: integer

- explicits:
    - compare each element to the corresponding element and find the difference.
    - create a list with the absolute difference squared of the corresponding elements.
    - return the average of those squared, absolute differences.
- implicits:
    - return value could be a float

- questions: none

D:
- list containing absolute differences of corresponding elements.
- integer as average.

C:
'''
import statistics

def solution(lst1, lst2):
    return statistics.mean([abs(x - y)**2 for x, y in zip(lst1, lst2)])

print(solution([1, 2, 3], [4, 5, 6]) == 9)
print(solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5)
print(solution([-1, 0], [0, -1]) == 1)
