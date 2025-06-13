
'''
Write a function groupAnagrams(words) that takes an array of words
as input and groups the anagrams together. Anagrams are words that
have the same characters but in a different order.

Your function should return an array of arrays, where each inner
array represents a group of anagrams. For words that do not have
anagrams, they should be grouped into an array together.

The order of the groups and the order of words within each group
does not matter.

P:
- input: list of strings.
- output: list with nested lists.

- explicits:
    - return a list with nested lists containing words that are anagrams.
        - anagrams are words with the same chars in different order.
    - order of groups and words within nested list does not matter.
- implicits:
    - none

D:
- list to contain all words that are anagrams.
- list to contain lists of anagrams.
    - to be returned.
- range to iterate through input list.


A:
- HL -
iterate through the input list.
put the current word in a list.
check if any of the words after the current word contains all of the same letters and letter count as the current word.
if they do, add the word to the list.
add that list to another list if none of the words in that list are in a nested list in that list.

1. init 'anagrams_list' to an empty list.
2. iterate through the input list.
    - init 'checker' to the current word.
    - if 'checker' is in any list in 'anagrams_list' skip to next iteration.
    - init 'anagram' to a list containing the current word.
    - iterate through all the following words.
        - if a word contains all the letters of the current word and vice versa,
        and all the chars have the same count (helper function?):
            - append the word to 'anagram'.
    - append 'anagram' to 'anagrams_list'.
3. return 'anagrams_list'
'''

def is_anagram(checker, word):
    return all(checker.count(char) == word.count(char) for char in word)


def groupAnagrams(word_list):
    anagrams_list = []

    for i in range(len(word_list)):
        checker = word_list[i]
        if any(checker in lst for lst in anagrams_list):
            continue
        anagrams = [checker]
        for j in range(i + 1, len(word_list)):
            if is_anagram(checker, word_list[j]):
                anagrams.append(word_list[j])
        anagrams_list.append(anagrams)

    return anagrams_list


print(groupAnagrams(['listen', 'silent', 'enlist', 'hello', 'olhel']))
# Output: [['listen', 'silent', 'enlist'], ['hello', 'olhel']]

print(groupAnagrams(['abc', 'bca', 'cab', 'def', 'fed']))
# Output: [['abc', 'bca', 'cab'], ['def', 'fed']]

print(groupAnagrams(['cat', 'dog', 'tac', 'god', 'act']))
# Output: [['cat', 'tac', 'act'], ['dog', 'god']]