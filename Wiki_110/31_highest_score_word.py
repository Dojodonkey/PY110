'''
# Find the highest scoring word in a string.
# Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26.
# Return the highest scoring word.
# If two words score the same,
# return the word that appears earliest in the string.

print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')
'''
def word_value(word):
    return sum(ord(char) - 96 for char in word)

def high(strng):
    strng_split = strng.split()
    max_ = strng_split[0]
    for i in range(1, len(strng_split)):
        if word_value(strng_split[i]) > word_value(max_):
            max_ = strng_split[i]

    return max_

print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')