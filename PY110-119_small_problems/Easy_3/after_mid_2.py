'''
Problem Statement:
As seen in the previous exercise,
the time of day can be represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format,
and return the number of minutes before and after midnight, respectively.
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Understanding the Problem:

- input: string in 24 hour format
- output: number of minutes

- explicit rules:
    - write 2 functions:
        - one returns the number of minutes before midnight,
        the other the number of minutes after midnight.
    - both functions return a value in the range of 0 and 1439.
- implicit rules:
    - none

- questions: none

Examples/Test Cases:
```python
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
```
- observations:
    - only '00:00' and '24:00' do both functions return the same number, 0.
- understanding confirmed

Data Structures:

    - integers
    - lists to split the input string

Algorithm:

1. define two functions to each accept one parameter, a string.
2. 'after_midnight' returns the amount of minutes in the input string.
3. 'before_midnight' returns the amount of minutes left between 'after_midnight' and 'midnight'.

Code:
'''
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = MINUTES_PER_HOUR * 24

def after_midnight(time):
    split_time = time.split(':')
    hour = int(split_time[0])
    minute = int(split_time[1])
    result = (hour * MINUTES_PER_HOUR) + minute
    while result >= 1440:
        result = result - 1440
    return result

def before_midnight(time):
    result = MINUTES_PER_DAY - after_midnight(time)
    while result >= 1440:
        result = result - 1440
    return result

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True