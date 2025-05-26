'''
# Your task is to Reverse and Combine Words.
# Input: String containing different "words" separated by spaces
# 1. More than one word? Reverse each word and combine first with second, third with fourth and so on...
# (odd number of words => last one stays alone, but has to be reversed too)
# 2. Start it again until there's only one word without spaces
# 3. Return your result…

P:
- input: string of words
- output: combined and reversed single string.

- explicits:
    - if more than one word, reverse each word and combine it with the next word.
        - like pairs, first with second, third with fourth, etc..
    - if its an odd number of words, the last word is not combined with any words,
    but does need to be reversed.
    - repeat the process until all words are combined into a single word.
- implicits:
    - if the string is a single word, return it as is.

- questions: none

D:
- list to contain words of the input string.
- list containing combined words.

A:
- High Level Strategy -
iterate through a list of words reversed words until there is only one element in the list.
reverse two elements at a time and combine them.
if the list contains an odd number of words, the last word is not combined with any other words,
but is reversed.

1. create a list of reversed words.
2. write a helper function to reverse words.
3. iterate through the list until there is only one element in the list.
    - check if the list has an odd length.
        - if so just leave the last word alone.
4. return a joined string.



p reverse_and_combine_text("abc def") == "cbafed"
p reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi"
p reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed"
p reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
"trzwqfdstrteettr45hh4325543544hjhjh21lllll"
p reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf"
'''
def reverse_and_combine_text(strng):
    s = strng.split()

    while len(s) > 1:
        s_rev = [word[::-1] for word in s]

        combined = []
        for i in range(0, len(s_rev)-1, 2):
            combined.append(s_rev[i] + s_rev[i+1])

        if len(s_rev) % 2 == 1:
            combined.append(s_rev[-1])

        s = combined

    return s[0]





print(reverse_and_combine_text("abc def") == "cbafed")
print(reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi")
print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed")
print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
"trzwqfdstrteettr45hh4325543544hjhjh21lllll")
print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")