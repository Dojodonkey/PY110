'''
Write a function that, given a string of text, returns a list of the top-3 most
occurring words, in descending order of the number of occurrences.

Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
- Matches should be case-insensitive.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words,
then either the top-2 or top-1 words should be returned,
or an empty list if a text contains no words.

P:
- input: string
- output: list

- explicit rules:
    - return a list of the top 3 most occurring words in descending order.
    - a word is a string of letters (may contain apostrophes).
    - matches are case-insensitive.
    - if a string contains fewer than 3 unique words, either top word or top 2 words should be returned.
        - if the string is empty or contains non-alpha chars return an empty list.
- implicit rules:
    - none

- questions: none

E:
top_3_words(" , e .. ") # ["e"]
top_3_words(" ... ") # []
top_3_words(" ' ") # []
top_3_words(" ' ' ' ") # []
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]

D:
- list of words from the input string.
- list of words excluding punctuation.
- list containing top 3 most used words.
- dictionary to keep track of count.

A:
- High Level:
First split the string into a list. Then create a new list containing words excluding punctuation.
Find the most used word, add it to 'max_list' and then remove it from the cleaned word list. Repeat this 3 times.
Return 'max_list'

1. split the input string and assign the list to 'split_str'.
2. create an empty list and assign is to 'cleaned_words'.
3. iterate through 'split_str' and select each word.
    - if the last char is punctuation, using selection criteria,
    removing the punction using transformation criteria.
    - add each word to 'cleaned_words'.
4. create an empty list and assign it to 'max_list'.
5. find the max count of a word in 'cleaned_words'.
    - use max function and count method using a keyword (key=).
6. remove all occurrences of max word in 'cleaned_words'
7. repeat step 5 and 6, 3 times.

C:
'''
# try a solution using recursion....

def top_3_words(strng):
    # if strng is empty
    if not strng or all(not word.isalpha() for word in strng.split()):
        return []

    split_str = strng.split()
    cleaned_words = []

    for word in split_str:
        #remove punctuation
        if not word[-1].isalpha():
            word = word[:-1]
        #if word is made up entirely of spec. chars disregard
        if all(not char.isalpha() for char in word):
            continue
        cleaned_words.append(word)

    def max_and_remove(lst):
        most_words = []
        while len(most_words) < 3:
            max_word = max(lst, key=lst.count)
            most_words.append(max_word)
            while max_word in lst:
                lst.remove(max_word)
            if not lst:
                break
        return most_words

    # max_word = max(cleaned_words, key=cleaned_words.count)
    return max_and_remove(cleaned_words)



print(top_3_words(" , e .. ")) # ["e"]
print(top_3_words(" ... ")) # []
print(top_3_words(" ' ")) # []
print(top_3_words(" ' ' ' ")) # []
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]