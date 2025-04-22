'''
Problem Statement:
Write a function that takes a floating point number representing an angle between 0 and 360 degrees
and returns a string representing that angle in degrees, minutes, and seconds.
You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes,
and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
DEGREE = "\u00B0"

Understanding the Problem:

- input: float (between 0 and 360)
- output: string representing that angle in degrees, minutes and seconds.

- explicit rules:
    - use a degree symbol to represent degrees.
    - use a single quote to represent minutes. (There are 60 minutes in a degree)
    - use double quote to represent seconds. (There are 60 seconds in a minute)
- implicit rules:
    - the number before the decimal is represented as a degree.

- questions:
    - how do you calculate minutes and seconds?
        - for minutes multiply the decimal point by 60.
        - for seconds, take the decimal point from minutes and multiply by 60.

Test Cases/Examples:

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

- observations:
    - 0 returns all zeros
    - 360 returns 360 but is accepted as all zeros.
    - the length of decimal number has no correlation to minutes and seconds.

- Data Structures:
    - integers to round out return values
    - output as a string.

Algorithm:

1. initialize 'DEGREE' to '\u00B0'
2. initialize 'MINUTES' to 60.
3. initialize 'SECONDS' to 60.
4. initialize 'SECONDS_PER_DEGREE' to 'MINUTES' times 'SECONDS'.
5. define 'dms' to accept 1 parameter, 'float_input'.
    1. initialize 'dms_list' to an empty list.
    2. initialize 'degree' to a converted integer of 'float_input'.
        - then append it to 'dms_list'.
    3. initialize 'minute_float' to the return value of (float_input - degree) multiplied by MINUTES .
    4. initialize 'minute' to a converted integer of ('minute_float' - 'minute') multiplied by SECONDS.
        - then append it to 'dms_list'.
    5. initialize 'seconds' to a converted integer of
    'float_input minus degree minus ('minute' divided by 'MINUTE') multiplied by SECONDS_PER_DEGREE.
        - then append it to 'dms_list'.
    6. convert all the integers in 'dms_list' to a string type.
    7. check that all the elements in 'dms' are a length of 2 chars.
        - if not, add a '0' as the first char of element.
    8. return a formatted string with the degree code after 'degree',
    a single qoute after 'minute' and a double quote after 'second'.

Code:
'''
DEGREE = '\u00B0'
MINUTE = 60
SECOND = 60
SECOND_PER_DEGREE = MINUTE * SECOND

def dms(float_input):
    # function to append numbers
    def add_el(number, lst):
        lst.append(number)

    # calculations
    dms_lst = []
    degree = int(float_input)
    add_el(degree, dms_lst)
    minute_float = (float_input - degree) * MINUTE
    minute = int(minute_float)
    add_el(minute, dms_lst)
    second = int((float_input - degree - (minute / MINUTE)) * SECOND_PER_DEGREE)
    add_el(second, dms_lst)

    # convert numbers to strings
    stringed = [str(num) for num in dms_lst]

    # check for padded zeros
    result_lst = [stringed[0]]
    for i in range(1, len(stringed)):
        if len(stringed[i]) < 2:
            stringed[i] = '0' + stringed[i]
            add_el(stringed[i], result_lst)
        else:
            add_el(stringed[i], result_lst)

    result = f'{result_lst[0]}{DEGREE}{result_lst[1]}\'{result_lst[2]}\"'
    print(result)
    return result

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")