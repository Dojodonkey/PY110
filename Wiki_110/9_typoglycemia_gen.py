'''
Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started


P:
- input: strng
- output: strng

- explicits:
    - return a new function based on the input function, taking evry word,
    and alphabetically it, excluding the first and last chars.
    - punctuation should remain in its original index.
- implicits:
    - many words have punctuation in the middle of the word.

D:
- list to split the string into words.
- string to contain a rebuilt word (perhaps using index reassignment).

A:
- HL -
iterate through the words in the input string.
init variables to the first letter, the middle (part to be sorted) and the last char/chars.
    - check the last chars if punctuation is the last char.
    - if punctuation is in the middle of the char, init a variable to that char and the index it is in.
        - then remove it, sort the section and insert the char at the same index.
    - append the rebuild word to a new list.
join and return the new list.

1.) init 'result_lst' to an empty list.
2.) iterate through words in the input string
    - split method.
3.) assign variables to sections of the word not being included in the sort.
4.) rebuild the word including the sorted mid-section and append it to 'result_lst'.
5.) join and return 'result_lst'.

C:
'''

def scramble_words(message):
    result_lst = []

    for word in message.split():

        #assigning slices of the word
        first = word[:1]
        if word[-1].isalpha():    # determing the middle and last slices of word based on if last char is alphabetic or not.
            middle = word[1:-1]
            last = word[-1]
        else:
            middle = word[1:-2]
            last = word[-2:]

        spec_chars_lst = []  # using a list to keep the special char and idx of each word in a tuple.
        middle_split = list(middle)    # list of chars to remove special chars and then insert them after sorting them.
        for idx, char in enumerate(middle_split):
            if not char.isalpha():    # adding non-alpha chars and index of chars to dict.
                spec_chars_lst.append((char, idx))  # char is already in dict.
                middle_split.pop(idx)

        middle_split.sort()

        if spec_chars_lst:    # if there are special chars, insert them back into the list of chars.
            for tple in spec_chars_lst:
                char_, idx = tple    # tuple unpacking
                middle_split.insert(idx, char_)

        middle = ''.join(middle_split)  # reassign to a sorted string

        result_lst.append(first + middle + last)

    return ' '.join(result_lst)


print(scramble_words('pro-fessio-nals')) # should return 'pae-filnoo-rsss'

print(scramble_words("you've gotta dance like there's nobody watching, "
"love like you'll never be hurt, sing like there's nobody listening, "
"and live like it's heaven on earth."))

# should return "you've gotta dacne like teehr's nbdooy wachintg,
#  love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg,
# and live like it's haeevn on earth."