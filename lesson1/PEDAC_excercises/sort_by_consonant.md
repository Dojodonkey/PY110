# Sort by Adjacent Consonants

## Problem Statement:
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

## Understanding the Problem
Input: List containing strings
Output: Ordered List based on amount of adjacent consonants in each string.

Explicit Rules:
- adjacent consonants are next to each other or last char in a word and first char in next word seperated by a space.
- if two strings have the same amount of adjacents consonants, original order of the list determines order.

Implicit Rules:
- None

Questions:
- Strings can contain multiple words? regarding spacing
- sorted in ascending or descending order? Highest amount to lowest amount or opposite?
- is letter case important?

## Examples / Test cases

```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```
confirmed rules:
- sorted by descending order
- strings may contain seperate words
- case is not relevant as all strings are lower cased
- there are no empty strings

## Data Structures

- maybe need to create an empty list and add elements when iterating through the passed in list.
- maybe a dictionary to count adjacent consanents in each string.

## Algorithm
1. count all adjacent consonants in the string
    1. remove spaces from string.
    2. initialize 'counter' to 0.
    3. initialize 'consonant streak' to an empty string.
    4. iterate through the string:
        1. if char is not a vowel:
            - reassign 'consonant streak' to include the char.
        2. if it is a vowel:
            - check if the length of 'consonant streak' is greater than 'counter'.
                - if it is check if the length of 'consonant streak' is greater than 1.
                    - if it is update counter to include the length of 'consonant streak'.
            - update 'consonant streak' to an empty list to reset it.
    5. return 'counter'
2. sort the list based on adjacent consonants
    - sort the list using the key argument and reverse the order as we want a descending list.
    return the sorted list


## Code
```python
def consonant_counter(string_from_list):
    # remove spaces from string if any:
    string_from_list = string_from_list.replace(' ', '')
    # variable to track adjacent consonants and total count:
    counter = 0
    con_streak = ''

    for char in string_from_list:
        if char not in 'aeiou':    #check if char is a vowel
            con_streak += char
            if len(con_streak) > counter:    # if con_streak contains more than one char, consonant is found.
                if len(con_streak) > 1:      # if con_streak is greater than one, adjacent consonants have been found.
                    counter = len(con_streak)    # reassign counter to the length of con_streak.
        # if char is a vowel
        else:
            if len(con_streak) > counter:    # if con_streak is greater than than counter it needs to be updated
                if len(con_streak) > 1:      # if con_streak is greater than one adjacent consonants have been found.
                    counter += len(con_streak)    # reassign counter to the length of con_streak
            # reset con_streak for next set of adjacent consonants
            con_streak = ''

    return counter

def sort_by_consonant_count(list_of_strings):
    # sort argument passed in
    list_of_strings.sort(key=consonant_counter, reverse=True)
    return list_of_strings

# Test cases:
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```