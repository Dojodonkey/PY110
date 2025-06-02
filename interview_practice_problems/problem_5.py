'''
Create a function that takes a string argument
 and returns the character that occurs most often in the string.
If there are multiple characters with the same greatest frequency,
 return the one that appears first in the string.
 When counting characters, consider uppercase and lowercase versions to be the same.

P:
- input: string
- output: string

- explicits:
    - return the char that occurs most frequently in the input string.
    - if multiple chars occur equally as often, return the char that occurs first.
    - upper case and lower case considered the same char.
- implicits:
    - none.

- questions: none

D:
- dictionary containing chars as keys and count as value.
- list containing tuples of char and count.
- string to convert the input string to lower case.
- string to contain highest occurrence.
    - updated while iterating through input string.

A:
- HL -
init 'most_freq_char' to None.
iterate through a lower case version of the input string.
if the count of the char is greater than or 'most_freq_char' is falsy,
reassign 'most_freq_char' to point to that char.

C:
'''
def most_common_char(strng):
    most_freq_char = strng[0]
    strng = strng.lower()

    for char in strng:
        if strng.count(char) > strng.count(most_freq_char):
            most_freq_char = char
    return most_freq_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')