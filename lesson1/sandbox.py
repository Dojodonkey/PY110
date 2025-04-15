'''
Algorithm:
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
'''
def consonant_counter(string_from_list):
    string_from_list = string_from_list.replace(' ', '')
    counter = 0
    con_streak = ''
    for char in string_from_list:
        if char not in 'aeiou':
            con_streak += char
            if len(con_streak) > counter:
                if len(con_streak) > 1:
                    counter = len(con_streak)
        else:
            if len(con_streak) > counter:
                if len(con_streak) > 1:
                    counter += len(con_streak)
            con_streak = ''
    return counter

def sort_by_consonant_count(list_of_strings):
    list_of_strings.sort(key=consonant_counter, reverse=True)
    return list_of_strings

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
