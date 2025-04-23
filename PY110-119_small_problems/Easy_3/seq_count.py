'''
Problem Statement:
Create a function that takes two integers as arguments.
The first argument is a count, and the second is the starting number of a sequence that your function will create.
The function should return a list containing the same number of elements as the count argument.
The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0.
The starting number can be any integer. If the count is 0,
the function should return an empty list.

Understanding the Problem:

- input: two integers
- ouput: lst

- explicit rules:
    - the first argument is a 'count', as the function should return a list with 'count' elements.
    - the second argument is the first element in the list to be returned.
    - every element after the first, needs to be a multiple of the first element (the second argument passed in).
- implicit rules:

- questions:
    - every element can just be a multiple? Not in a sequence?

Test Cases/Examples:

```python
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
````
- observations:
    - multiples are in sequence.
    - for a negative start argument, all elements are negative

Data Structures:

    - list
    - range

Algorithm:
1. define 'sequences' to accept 2 parameters, 'length' and 'start_int'.
2. create a list.
    - the first element is 'start_int'.
    - find the remaining elements by multiplying 'start_int' by an increasing number at each.
    - do previous step until the list contains as many elements equal to 'length'.
3. return the list.

Code:
'''
def sequence(length, start):
    if length == 0:
        return []
    result = [start]
    for i in range(2, length + 1):
        result.append(start * i)

    return result

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True