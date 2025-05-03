'''
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.

To be a valid triangle,
the sum of the angles must be exactly 180 degrees,
and every angle must be greater than 0.
If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments
and returns one of the following four strings representing the triangle's classification:
'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values,
so you do not have to worry about floating point errors.
You may also assume that the arguments are in degrees.

P:

- input: 3 integers
- output: string representing triangles classification

- explicit rules:
    - sum of 3 integers (input) must be equal to 180 to be considered valid.
    - every integer must be greater than 0.
    - return a string classifying what type of triangle is being described.
- implicit rules:
    - 'right' describes degrees that are all less than 90 but greater than 30.
    - 'acute' describes degrees that are above 30 and less than 90.
    - 'obtuse' describes a triangle if a degree is greater than 90.

- questions: none

E:
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

D:

- an array to collect the input and check for validity.

- High-Level-Strategy:
    - After collecting the input in an array, if the sum of the array is not equal to 180,
    the function returns 'invalid'.
    - Then conditionals should check integers to classify the triange.

A:

1. Write a helper function to check if the input angles create a valid triangle.
2. use implicit rules to write a conditional to classify the triangle.

C:
'''
def valid(lst):
    return sum(lst) == 180 and all(angle > 0 for angle in lst)

def triangle(angle1, angle2, angle3):
    angles = sorted([angle1, angle2, angle3])
    #check for validity:
    if not valid(angles):
        return 'invalid'
    #classify triangle:
    if 90 in angles:
        return 'right'
    elif any(angle > 90 for angle in angles):
        return 'obtuse'
    else:
        return 'acute'


# - 'right' describes degrees that are all less than 90 but greater than 30.
# - 'acute' describes degrees that are above 30 and less than 90.
# - 'obtuse' describes a triangle if a degree is greater than 90.

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True