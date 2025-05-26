'''
Write a function that takes a list of words as input and returns a list of
integers. Each integer represents the count of letters in the word that occupy
their positions in the alphabet.

The problem is asking you to count how many letters in each word are in the same position in the alphabet
 as they are in the word.

P:
- input: list containing words.
- output: list of integers.

- explicit rules:
    - each integer in the output list represents the count of letters of each word that has the same position
    in the word, as it does in the alphabet.
- implicit rules:
    - case-insensitive

- questions: none

D:
- list or string to contain letters that have the same position in the word as in the alphabet.
- integer to keep count
- list for output
- integer to find position in the alphabet
- integer to find position int the word

A:
- High Level:
we should iterate through each word in the list and find it's position in the alphabet.
If that position is the same as the letter's position in the word, increase a 'count' by 1,
or store the letter in an initialized empty array.
Place that count or total of the list into another initialized list to be returned.

1. initialize 'count_list' to an empty list.
2. iterate through each string of the input list.
3. iterate through each letter of the string.
4. initialize 'count' to 0.
5. find the position of each letter in the alphabet and compare it to the position of the letter in the string.
    - if they are equal, add 1 to 'count'
6. after the entire string is iterated over, append 'count' to 'count_list'
7. return 'count_list'

C:
'''
def solve(lst):
    count_list = []
    for strng in lst:
        strng = strng.lower()
        count = 0
        for idx, letter in enumerate(strng):
            alpha_position = ord(letter) - ord('a')
            if alpha_position == idx:
                count += 1
        count_list.append(count)
    return count_list
#Examples:
print(solve(["abode","ABc","xyzD"])) # should return [4, 3, 1]
print(solve(["abide","ABc","xyz"])) # should return [4, 3, 0]
