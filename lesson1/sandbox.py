'''
if any of the input strings no not consist of any alphabetical letters, return an empty list.
break the input string up into a list. initialize 'count_dict' to an empty dictionary.
iterate through that list of words. build up 'count' dict using the count of each word.
    - if that word is already in the dictionary just update the value by 1.
    - if not, add that key to the dictionary with a value of 1.
then create out of the values in 'count_dict' and sort this list in descending order.
reassign it to only include the first 3 elements.
init 'max_words' to an empty list.
iterate through our value list.
    - if they match any value in 'count_dict', add that key to 'max_words'.
return 'max_words'.
'''
def top_3_words(strng):
    if all(not char.isalpha() for char in strng):
        return []

    cleaned_str_split = [word if word[-1].isalpha()
                         else word[:-1] for word in strng.split()]
    cleaned_str_split = [word for word in cleaned_str_split
                         if any(char.isalpha() for char in word)]

    count_dict = {}

    for word in cleaned_str_split:
        if word not in count_dict:
            count_dict[word] = cleaned_str_split.count(word)

    max_values = sorted((val for val in count_dict.values()),
                         reverse=True)[:3]
    max_words = []

    for m_value in max_values:
        for key, value in count_dict.items():
            if m_value == value:
                max_words.append(key)

    return max_words



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