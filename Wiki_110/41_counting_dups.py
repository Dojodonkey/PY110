# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the input string.
'''
P:
- input: string
- output: integer (number of duplicates)

- explicits:
    - return the amount of chars that appear more than once in the string.
    - comparisons are case-insensitive.
- implicits:
    - if string is empty, return 0.

D:
- dictionary to countain chars as keys and occurrences as values.
- integer to contain count of each char when iterating through the string.
- integer to keep count of duplicates (to be returned).
- a list to contain duplicate chars.

E:
- High Level -
iterate through the string. if the count of that char is greater than 1, add it to a list.
if it is already in the list, don't add it.
return the length of the list.

1. init 'dup_list' to an empty list.
2. iterate through the input string.
3. if a char's count is greater than 1, add it to 'dup_list'
if it is not already in that list.
4. return the length of 'dup_list'
'''
def duplicate_count(strng):
    strng = strng.lower()
    dup_list = []

    for char in strng:
        if strng.count(char) > 1:
            if char not in dup_list:
                dup_list.append(char)

    return len(dup_list)

print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)