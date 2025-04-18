'''
Problem Statement:
Write a function that takes a string consisting of zero or more space-separated words
and returns a dictionary that shows the number of words of different sizes.

Understanding the Problem:
- input: string
- output: dictionary

- explicit rules:
    - strings contain 0 or more words seperated by spaces.
    - the keys of the dictionary are the lengths of words in the string.
    - the values of the dictionary is how many words of that length occur in the string.
- implicit rules:
    - commas and punctuations in the string are included in the length of words.

- questions:
    - none

Example/Test Cases:

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

- Observations:
    - commas and punctuations are included.

Data Structures:
    - dictionaries for the output
    - lists to contain words from the string

Algorithm:
    1. define 'word_sizes' to accept 1 parameter, 'strng'.
    2. create a list, 'split_string' containing all the words in 'string'.
    3. initialize 'dict_count' to an empty dictionary.
    4. iterate through 'split_string'.
        1. find the length of each word in 'split_string'
        2. if that length already exists as a key in 'dict_count', update the value by 1.
        3. if that length does not exist as a key in 'dict_count', add that length as a key and map it to the value 1.
    5. return 'dict_count'

Code:
'''
def word_sizes(strng):
    split_strng = strng.split()
    count_dict = {}

    for word in split_strng:
        if len(word) in count_dict:
            count_dict[len(word)] += 1
        else:
            count_dict[len(word)] = 1

    return count_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})