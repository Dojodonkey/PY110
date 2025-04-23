'''
Problem Statement:
The time of day can be represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm).
Your function should work with any integer input.

You may not use Python's datetime module.

Understanding the Problem:

input: integer
output: string

explicit rules:
    - integer represents minutes before or after midnight.
        - positive integer means minutes after midnight.
        - negative integer means minutes before midnight.
    - the output string represents a 24-hour format (hh:mm)
implicit rules:
    - none

questions: none.

Test Cases/Examples:
```python
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
```
- observations:
    - minutes can represent hours or even days before or after midnight.
- understanding confirmed.

Data Structures:

- dictionary to map minutes into days, hours and minutes

Algorithm:
1. initialize constansts to perform calculations on 'minutes_input'.
        1. 'MINUTES_PER_HOUR' is assigned to 60.
        2. 'HOURS_PER_DAY' is assigned to 24.
        3. 'MINUTES_PER_DAY' is assigned to the value returned by 'MINUTES_PER_HOUR' multiplied by 'HOURS_PER_DAY'.
2. define a function 'organize_minutes' to accept 1 parameter, 'minutes_input'.
    1. create a dictionary, 'org_dict' and map keys 'days', 'hours', 'minutes' to 0.
    2. break down 'minutes_input' to update values in 'org_dict'.
        1. while 'minutes_input' is greater than 'MINUTES_PER_DAY':
            - update value assigned to 'days' by 1.
            - reassign 'minutes_input' to the value of 'minutes_input' minus 'MINUTES_PER_DAY'
        2. while 'minutes_input' is greater than 'MINUTES_PER_HOUR':
                - update value mapped to 'hours' by 1.
                - reassign 'minutes_input' to the value of 'minutes_input' minus 'MINUTES_PER_HOUR'.
        3. update the value mapped to 'minutes' to 'minutes_input'.
    3. return 'ord_dict'
3. Write a helper function to deal with padding single digits.
        - the return format is 'hh:mm' or '00:00'.
4. define function, 'time_of_day' to accept 1 parameter, 'minutes_input'.
    1. initialize 'min_map' to the return value of 'organize_minutes' passed in 'minutes_input'.
    2. initialize 'hour_form' to 24
    3. initialize 'minute_form' to 60
    4. if 'minutes_input' is less than 0:
        created a formatted string:
            - 'hour_form' minus the value mapped to 'hours' in 'min_map' (minus 1 due to there being minutes leftover)
            - 'minute_form' minus the value mapped to 'minutes' in 'min_map'
    5. if 'minuts_input' is greater than 0:
        - initialize 'hour_form' and 'minute_form' to 0.
        - create a formatted string:
            - 'hour_form' plus the value mapped to 'hours' in 'min_map'
            - 'minute_form' plus the value mapped to 'minutes' in 'min_map'

    7. return the return value of the helper function.


Code:
'''
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def pad_zeros(strng):
    split_str = strng.split(':')
    formatted_lst = []
    for element in split_str:
        if len(element) < 2:
            element = '0' + element
        formatted_lst.append(element)
    return ':'.join(formatted_lst)


def organize_minutes_to_dict(number):
    number = abs(number)
    org_dict = {'days': 0, 'hours': 0, 'minutes': 0}

    while number > MINUTES_PER_DAY:
        org_dict['days'] += 1
        number -= MINUTES_PER_DAY
    while number > MINUTES_PER_HOUR:
        org_dict['hours'] += 1
        number -= MINUTES_PER_HOUR
    org_dict['minutes'] = number

    return org_dict

def time_of_day(number):
    mapped_time = organize_minutes_to_dict(number)
    hour_form = 24
    min_form = 60

    if number < 0:
        formatted = f'{hour_form - mapped_time['hours'] - 1}:{min_form - mapped_time['minutes']}'
    else:
        if mapped_time['minutes'] == min_form:
            mapped_time['hours'] += 1
            mapped_time['minutes'] = 0
        formatted = f'{mapped_time['hours']}:{mapped_time['minutes']}'

    return (pad_zeros(formatted))

# a more efficient solution:
# def time_of_day(delta_minutes):
#     # Normalize minutes to a positive value within a day
#     normalized_minutes = delta_minutes % MINUTES_PER_DAY

#     hours = normalized_minutes // MINUTES_PER_HOUR
#     minutes = normalized_minutes % MINUTES_PER_HOUR

#     return f"{hours:02d}:{minutes:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True