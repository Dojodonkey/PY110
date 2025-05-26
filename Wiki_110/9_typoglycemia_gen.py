'''
Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started

P:
- input: string.
- output: new string.

- explicit rules:
    - for each word in a string, the first and last char of each word remains in its position,
    while all chars are sorted alphabetically.
    - punctuation chars remain in original location in order.
- implicit rules:
    - all chars are lowercase.
    - some inputs contain punction while others don't.

- questions: none

E:

scramble_words('professionals') # should return 'paefilnoorsss'

scramble_words("you've gotta dance like there's nobody watching,
love like you'll never be hurt, sing like there's nobody listening,
and live like it's heaven on earth.")

# should return "you've gotta dacne like teehr's nbdooy wachintg,
#  love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg,
# and live like it's haeevn on earth."

- observations:
    - non-alphabetic chars include commas, apostrophes, and periods.

D:
- lists to split the string into words and modify them word by word.
- string for output

A:
- High Level:
    - split a string into a list of words. Then modify each word one at a time. Write conditionals
    for the first and last chars of a word and if there are non-alpha chars in the word.
    Then join the words in the list and return them.

1. split the string into a list of words.
2. iterate through the list word by word.
    - using slicing, sort the word ignoring the first, last and non-alpha chars.
    - create conditionals as words containing punctuation, the slice is set differently.
        - if it's a period or comma at the end of the word, the last char is -2.
        - if it's an apostraphe, location remains, might have to use 2 slices?
3. join the words of the list back together and return.
'''
def scramble_words(strng):
    word_lst = strng.split()
    scrammed_lst = []
    for word in word_lst:
        # pure alpha chars
        if word.isalpha():
            slice_ = sorted(list(word[1:-1]))
            word = word[0] + ''.join(slice_) + word[-1]
        # if punctiation is the last char
        elif not word[-1].isalpha():
            slice_ = sorted(list(word[1:-2]))
            word = word[0] + ''.join(slice_) + word[-2:]
        # if apostrophe in word (punctuation mid-word)
        else:
            spec_char = word.index("'")
            slice_ = sorted(list(word[1:spec_char] + word[spec_char + 1: -1]))
            word = [word[0]] + slice_ + [word[-1]]
            word.insert(spec_char, "'")
        #add scrambled word to new list
        scrammed_lst.append(''.join(word))

    return ' '.join(scrammed_lst)


print(scramble_words('professionals')) # should return 'paefilnoorsss'

print(scramble_words("you've gotta dance like there's nobody watching, "
"love like you'll never be hurt, sing like there's nobody listening, "
"and live like it's heaven on earth."))

# should return "you've gotta dacne like teehr's nbdooy wachintg,
#  love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg,
# and live like it's haeevn on earth."