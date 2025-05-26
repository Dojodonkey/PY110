'''
Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.

P:

- input: string
- output: dictionary

- explicit rules:
    - count occurrences of each lowercase letter in the input string.
    - return a dictionary with letters as keys and counts as values.
- implicit rules:
    - do not need to account for punctuation or capital letters.

- questions: none

D:

- dictionary containing letters from input string as keys and their count as values.

A:

- High Level Strategy:
    - iterate through the string, counting all occurrences of that letter within the string.
    - if the key is already in the created dictionary move on, if not, add it to the dictionary.

1. create an empty dictionary
2. iterate through the string letter by letter.
    - if the letter is already a key in the dictionary, move on.
    - if not, add the letter as the key and the count as the value.

C:
'''
def letter_count(strng):
    count_dict = {}
    for letter in strng:
        if letter not in count_dict:
            count_dict[letter] = strng.count(letter)
    return count_dict

print(letter_count('launchschool')) #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 } # no 'n', no 's'
# {'l': 2, 'a': 1, 'u': 1, 'n': 1, 'c': 2, 'h': 2, 's': 1, 'o': 2}
