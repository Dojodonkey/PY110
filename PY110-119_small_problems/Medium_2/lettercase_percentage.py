'''
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively.
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

P:

- input: string
- output: dictionary

- explicit rules:
    - return a dictionary with 3 key/value pairs:
        - 'lowercase', 'uppercase' and 'neither' mapped to a string containg digits to the second dec place.
- implicit rules:
    - spaces count as characters.

- questions: none


E:
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

D:

- dictionary to keep keys and values regarding amount characters of a certain case.

- High-Level-Strategy:
    - First we must find the length of the string and then count the characters,
    keeping count of type in a dictionary.
    Then we will change that value of a dictionary into a string
    while formatting the integer to keep only 2 decimal numbers.

A:

1. find the length of the string.
2. create an empty dictionary.
3. iterate through the string.
    - use conditionals to categorize case of character and keep a count.
4. find the percentages using the values in the dict and the length of the string.
    - those percentages are now the new values mapped to keys in dict.
5. format this values to have only 2 decimal places.
6. convert them into a string.

C:
'''

def letter_percentages(strng):
    length = len(strng)
    char_dict = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0
    }

    for char in strng:
        if char.islower():
            char_dict['lowercase'] += 1
        elif char.isupper():
            char_dict['uppercase'] += 1
        else:
            char_dict['neither'] += 1


    for key, value in char_dict.items():
        char_dict[key] = f'{(value / length) * 100 if value != 0 else 0:.2f}'

    return char_dict








expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)