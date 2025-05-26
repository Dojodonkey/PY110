'''
Write a function that takes in a string of one or more words and returns the same string,
but with all words of five or more letters reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

P:
- input: string
- output: string

- explicits:
    return the input string modified so that every word with more than 5 letters is reversed.
'''
def spin_words(strng):
    result = []

    for word in strng.split():
        if len(word) >= 5:
            word = word[::-1]
        result.append(word)

    return ' '.join(result)

# using list comprehension and join
def spin_words(strng):

    return ' '.join([word[::-1] if len(word) >= 5
                     else word
                     for word in strng.split()])



print(spin_words("Hey fellow warriors")) # should return "Hey wollef sroirraw"
print(spin_words("This is a test")) # should return "This is a test"
print(spin_words("This is another test")) # should return "This is rehtona test"
