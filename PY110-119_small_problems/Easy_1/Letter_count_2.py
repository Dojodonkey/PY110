'''
Problem Statement:
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size.
For instance, the word size of "it's" is 3, not 4.

Understanding the Problem:
- input: string
- output: dictionary

- explicit rules:
    - strings contain 0 or more words seperated by spaces.
    - the keys of the dictionary are the lengths of words in the string.
    - the values of the dictionary is how many words of that length occur in the string.
    - special characters should not be included in determining the length of the word in the string.
- implicit rules:
    - none

- questions:
    - none

Example/Test Cases:

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

Data Structures:
    - dictionaries for the output
    - lists to contain words from the string

 Algorithm:
    1. define 'word_sizes' to accept 1 parameter, 'strng'.
    2. initialize 'split_strng' to a list containing words from 'strng'.
    3. initialize 'cleaned_list' to an empty list.
    4. iterate over every word in 'split_strng'.
        1. initialize an empty string to 'clean_word'.
        2. iterate over every character in word.
            1. if the character is alphabetical, add it to 'clean_word'.
        3. add 'clean_word' to 'cleaned_list'.
    5. initialize 'count_dict' to an empty dictionary.
    6. iterate through 'cleaned_list'.
        1. if the length of word is already in 'count_dict' update its value by 1.
        2. if not add the length of word as a key mapped to the value 1.
    7. return 'count_dict'

Code:
'''
def word_sizes(strng):
    split_strng = strng.split()
    cleaned_list = []

    for word in split_strng:
        clean_word = ''
        for char in word:
            if char.isalpha():
                clean_word += char
        cleaned_list.append(clean_word)

    count_dict = {}

    for word in cleaned_list:
        if len(word) in count_dict:
            count_dict[len(word)] += 1
        else:
            count_dict[len(word)] = 1

    return count_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})