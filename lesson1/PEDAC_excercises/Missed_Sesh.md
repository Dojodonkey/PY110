
# /*
# Given two words, how many letters do you have to remove from them to make them anagrams?

# P - REWORD IN YOUR OWN WORDS
# Given two words, remove x amount of letters to ensure they are anagrams (the same letters, with the same frequencies).

# Requirements/Rules
# - all inputs are lower case letters or empty strings (no spaces, no punctuation)
# - empty strings count as anagrams
# - don't worry about case
# - anagrams order doesn't matter, just frequencies of letters
# - anagrams aren't real words

# Data structures
# Input: two strings
# Output: integer
# Intermediate:
#   - list of possible substrings [a, ab, b], [b, ba, a], the largest substring that is the same in both lists is the longest anagram
#   - dictionary/obj/hash to tally the frequencies of lettes {'a': 1, 'b': 3, ...}
#   - strings sorted alphabetically

# High-level strategies
# Jeff - After getting substrings for each input string, find the ones that are the same in both lists, find the longest of those, subtract that length from each of the input strings and add the remainders together.
# Zach - begin with a list of characters from the first string, iterate through the second, removing one of each character from the list (add to a counter if remove anything); then vice versa - needs some work
# Marc - sort both input alphabetically, iterate through both at the same time, counting when they match to find the anagram (then remove anagram letters from each input string to find the return number)
# Clare - Create two dictionaries for tallies of letters, iterate through a list of all letters in both inputs, add up the differences in the values


# **Algos**
# ***Marc***
# 1. Create a function called `anagram_difference` that accepts two parameters
# 2. Sort and split each string by substring:  helper?
#     -Get substring by appending each index to previous index

# 3. For both list check the match
#     - nested for loop and see when they match
#     -when they match that is `target_substring`
# 4. Minus the length of the longer string from the target_substring to get return number



# ***Zach***
# '''
# Initalize a list for each word.

# iterate through first word list
#     - compare element with each element in second word list
#     - if elements match
#         - remove each element from each list

# initalize variable number_to_remove = len(word_a) + len(word_b)
# return number_to_remove

# work backwards
# test case:
# console.log(anagram_difference('odws', 'hkrank') == 10 )
# word_1 = [o, d, w, s]
# word_2 = [h, k, r, a, n, k]
# len(word_1) + len(word_2) = 4 + 6 = 10

# word_1 = [a, b]
# word_2 = []
# counter = 1
# len(word_1) + len(word_2) = 2 + 0 = 2
# '''


# ***Jeff***
# """
# helper function: create dictionary(string as argument):
# Create dictionaries
#     using character for key and character count in each string


# function with two strings
# save dictionaries to references: using dictionary helper function 1 and 2
# create a `final_count` variable = 0

# if key in dict1 is in key in dict 2
#     subtract the value(count) to a absolutevalue whole number and store (+=) to finalcount
# if key in dict 1 or dict2 is not in use the remaining count and add += to finalcount; (can potentially pop ? )

# return the finalcount
# """

# ***Shannon***
# - initialize an integer `difference` to 0
# - create `dict1` and `dict2`, containing the characters as keys and their counts in `string1` and
# `string2`, respectively, as values.
# - for each key in `dict1`, if it is present in `dict2`, take the difference of their counts and
# add it to `difference`
# - for any keys found in `dict1` but not `dict2`, and vice versa, add their counts to `difference`
# - return `difference`


# ***Christine***
# 1. Set count = 0
# 2. Set dict1 as an empty dictionary, with the key as the letter, and value as the frequency of each letter in string 1 (helper function)
# 3. Do the same with string 2 (helper function)
# 4. Iterate through each dictionary, checking if key exists and getting the frequency of that letter in the other dictionary and adding the absolute value difference to total


# TEST CASES

# JAVASCRIPT
# console.log(anagram_difference('', '') == 0);
# console.log(anagram_difference('a', '') == 1);
# console.log(anagram_difference('', 'a') == 1);
# console.log(anagram_difference('ab', 'a') == 1);
# console.log(anagram_difference('ab', 'ba') == 0 );
# console.log(anagram_difference('ab', 'cd') == 4);
# console.log(anagram_difference('aab', 'a') == 2 );
# console.log(anagram_difference('a', 'aab') == 2 );
# console.log(anagram_difference('codewars', 'hackerrank') == 10 );
# console.log(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42);
# console.log(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50);

# PYTHON
# print(anagram_difference('', '') == 0)
# print(anagram_difference('a', '') == 1)
# print(anagram_difference('', 'a') == 1)
# print(anagram_difference('ab', 'a') == 1)
# print(anagram_difference('ab', 'ba') == 0 )
# print(anagram_difference('ab', 'cd') == 4)
# print(anagram_difference('aab', 'a') == 2 )
# print(anagram_difference('a', 'aab') == 2 )
# print(anagram_difference('codewars', 'hackerrank') == 10 )
# print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
# print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)


# RUBY
# p anagram_difference('', '') == 0
# p anagram_difference('a', '') == 1
# p anagram_difference('', 'a') == 1
# p anagram_difference('ab', 'a') == 1
# p anagram_difference('ab', 'ba') == 0
# p anagram_difference('ab', 'cd') == 4
# p anagram_difference('aab', 'a') == 2
# p anagram_difference('a', 'aab') == 2
# p anagram_difference('codewars', 'hackerrank') == 10
# p anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42
# p anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50
# */