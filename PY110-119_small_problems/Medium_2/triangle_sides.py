'''
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.

To be a valid triangle,
the sum of the lengths of the two shortest sides must be greater than the length of the longest side,
and every side must have a length greater than 0.
If either of these conditions is not satisfied,
the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments
and returns one of the following four strings representing the triangle's classification:
'equilateral', 'isosceles', 'scalene', or 'invalid'.

P:

- input: three integers describing the lengths of a triangle.
- output: string describing what type of triangle the three side make up.

- explicit rules:
    - to be a valid triangle:
        - the sum of the two shortest sides must be
        longer than the longest side
        - every side must be greater than 0.
    - function returns the following:
        - 'equilateral': All three sides have the same length.
        - 'isosceles': Two sides have the same length, while the third is different.
        - 'scalene': All three sides have different lengths.
        - 'invalid': if triangle not valid.
- implicit rules:
    - arguments are integers or floats

- questions: none

E:
```python
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
```
D:

- tuples to sort lengths of triangle sides.

- High-Level-Strategy:
    - First sort the triangle lengths in an array and then check:
        - if all sides are greater than 0
        - the sum of the shortest sides are longer than the longest side.
    - Create conditionals to determine what kind of triangle the sides create.

A:
1. sort the lengths by creating an array.
2. check for a valid triangle:
    - if the triangle is not valid, return 'invalid'
3. create conditionals to determine what kind of triangle the sides describe.
    - 'equilateral': All three sides have the same length.
    - 'isosceles': Two sides have the same length, while the third is different.
    - 'scalene': All three sides have different lengths.
'''
def triangle(side1, side2, side3):
    sides_arr = [side1, side2, side3]
    sides_arr.sort()
    #check for invalid triangle:
    if sides_arr[0] + sides_arr[1] < sides_arr[2] or not all(sides_arr):
        return 'invalid'
    #check what kind of triangle sides make up:
    if sides_arr[0] == sides_arr[2]:
        return 'equilateral'
    elif sides_arr[0] == sides_arr[1] or sides_arr[1] == sides_arr[2]:
        return 'isosceles'
    else:
        return 'scalene'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True