'''
# Write a function that finds all the anagrams of a word from a list.
# Two words are anagrams of each other if they both contain the same letters.

# Examples
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

p anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
p anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
p anagrams('laser', ['lazing', 'lazy', 'lacer']) == []

A:

High Level Strategy:
first create an empty list, 'ana_lst'. Then iterate through the input list
and check if length is the same and if all letters are in the input string.
if so, add that word to 'ana_lst'.

1. init 'anagrams_lst' to an empty list.
2. iterate through input list.
    - if all characters in a word are in the input str, append word to 'ana_lst' and all characters in the word are in the input string.
        - using all function.
3. return 'anagrams_lst'
'''

def anagrams(strng, lst):
    ana_lst = []

    for word in lst:
        if all(letter in strng for letter in word) and all(letter in word for letter in strng):
            ana_lst.append(word)

    return ana_lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])