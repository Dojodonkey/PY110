'''
Write a function that takes a list of target letters and a list of characters and returns a dictionary that tracks if a given letter from letters is present in the list of target letters and the counts the number of times it is present.

P:
- input: 2 arguments
    - list of target letters.
    - list of letters.
- output: dictionary

- explicits:
    - return a dictionary with target letters as keys mapped to a dictionary.
        - dict value contains:
            - 'present' mapped to a bool.
            - 'count' mapped to occurrences of in letter list.
- implicits:
    - 'target_letters' contains unique chars.

D:
- dictionary containing 'present' and 'count'.
- dictionary with chars from 'target_list' as keys.
    - mapped to dict above.
- integer to represent occurrences of 'letter_char' in 'letters'.
- strings to create keys of nested dicts.

A:
- HL -
iterate through 'target_letters'.
add current char as key mapped to a dictionary.
    - 'present' mapped to True if occurrences in 'characters'
    returns greater than 0.
    - 'count' mapped to occurrences.
return dictionary.

1. init 'target_dict' to an empty dict.
2. iterate through 'target_letters'.
    - find occurrences of char in 'characters'.
    - add key (char) and map it to a dict with
    'present' and 'count' as keys.
        - 'present' mapped to True if occurrences greater than 0.
        - 'count' mapped to occurrences.
3. return 'target_dict'.

C:
'''

def count_letters(targets, letters):
    target_dict = {}

    def get_count(char):
        return letters.count(char)

    for char in targets:
        target_dict[char] = {'present': get_count(char) > 0,
        'count': get_count(char)}

    return target_dict

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']


print(count_letters(target_letters, characters) == {
    'a': { 'present': True, 'count': 1 },
    'b': { 'present': True, 'count': 2 },
    'c': { 'present': False, 'count': 0 },
    'd': { 'present': True, 'count': 1 },
    'e': { 'present': False, 'count': 0 }
} )