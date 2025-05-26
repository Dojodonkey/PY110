# Write a function that takes a list of words and constructs a new word by
# concatenating the nth letter from each word, where n is the position of the
# word in the list.

# Example:
# nth_char(['yoda', 'best', 'has']) # should return 'yes'

'''
P:
- input: list containing strings
- output: string

- explicit rules:
    - construct a new word by concatenating the 'nth' letter of each string in the input list.
- implicit rules:
    - the first element, use the first char.
    - the second element, use the second.... etc..
    - modification allowed of input list
- questions: none

D
 - use a list to keep track of result
 -range to access the indexes

High Level
    Marc
        - Use a loop to loop over words, and add index + 1 of word to new empty string

result = ''
for index in the range of list
    list[index][index]  = y ,




    Jerome

    - create an empty string, 'result'. Iterate through the input list and depending on the index of each string, add the 'nth' character of that element to 'result'.

    1. create an empty string 'result'.
    2. iterate over the input list.
    3. the char at the index, being the same as the index of the string (the 'nth' char) will be concatenated to 'result'
    4. return 'result'

'''


def nth_char(lst):
    result = ''
    for idx in range(len(lst)):
      result += lst[idx][idx]

    return result


print(nth_char(['yoda', 'best', 'has'])) # should return 'yes'