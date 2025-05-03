'''
A featured number (something unique to this exercise) is an odd number that is a multiple of 7,
with all of its digits occurring exactly once each.
For example, 49 is a featured number,
but 98 is not (it is not odd), 97 is not (it is not a multiple of 7),
and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and
returns the next featured number greater than the integer.
Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

P:

- input: integer
- output: integer (next featured number)

- explicit rules:
    - a featured number is a multiple of 7 with all digits occurring only once and not even (odd).
    - function returns the next featured number after the input number.
- implicit rules:
    - none

- questions: none

E:
```python
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True
error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
```

D:

- range to iterate through a sequence of numbers until a number is a featured num.

A:

1. Determine what a featured number is. (Helper function)
2. generate numbers starting 1 after the input until a featured number occurs.

'''
error = ("There is no possible number that "
        "fulfills those requirements.")

def unique_num_check(number):
    return ((number % 7 == 0) and
            (len(list(str(number)))) == len(set(str(number))) and
            (number % 2 == 1))

def next_featured(number):
    number += 1
    # to arrange number to check every 14 ints:
    if number % 7 != 0:
        number = number + (7 - (number % 7))
    if number % 2 == 0:
        number += 7
    # generate mults of 14 until next featured number:
    while not unique_num_check(number):
        number += 14
        if number > 9876543201:
            return error

    return number

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True