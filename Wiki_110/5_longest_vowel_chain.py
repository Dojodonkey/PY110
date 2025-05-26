'''
Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).

Examples:
solve("roadwarriors") # should return 2
solve("suoidea") # should return 3

P:
- input: string
- output: integer (longest sequence of vowels in the string)

- explicit rules:
    - return the longest substring that consists entirely of vowels.
- implicit rules:
    - strings are lowercased.
    - there are no spaces.
- questions: none

D:
- list to contain vowel substrings
- integers to keep track of length of sequence

A:
- high-level-algo:
initialize a count of vowel sequences 'max_seq' to 0. Then iterate through the string. initialize 'vowels' to zero. If a letter is a vowel, update 'vowels' by 1.
if a letter is not a vowel, assign 'max_seq' to 'vowels' only if 'vowels' is greater than. then reassign 'vowels' to zero.

1. init 'max_seq' to 0.
2. iterate over 'strng'.
3. init 'vowels' to 0.
4. if 'letter' is a vowel, update 'vowels' by 1.
    if not, if 'vowels' is greater than 'max_seq', reassign 'max_seq' to 'vowels'.
    either way, after reassign 'vowels' to 0.
5. return 'max_seq'

C:
'''
def solve(strng):
    max_count = 0
    vowel_count = 0
    for letter in strng:
        if letter in 'aeiou':
            vowel_count += 1
        else:
            if vowel_count > max_count:
                max_count = vowel_count
            #either way, if a consonant occurs, reset vowel count.
            vowel_count = 0
    #check one more time, in case last letter was a vowel
    if vowel_count > max_count:
        max_count = vowel_count

    return max_count


print(solve("roadwarriors")) # should return 2
print(solve("suoideaio")) # should return 4