'''
# Create a function that turns a string into a Wave. You will be passed a string
# and you must return that string in an array where an uppercase letter is a person standing up.

P:
- input: string
- ouput: list

- explicits:
    - return a list, beginning with the first char capitalized and the rest lower is the first element.
    Then the second char is capititalized and the rest lowered, etc...
- implicits:
    - string may be empty or contain spaces.
        - spaces are included in the returned list.

- questions: none

D:
- range to iterate through string, setting the index of the char to be capitalized.
- list to contain strings to be returned.

A:
- High Level Strategy -
create an empty list, then iterate over the input string using a range (beginning at 0, stopping at the len of list).
create an empty string. iterate through all the chars in the string. Those that are not at the index from the range,
convert to lowercase, the char that is, convert to uppercase. add the char to initialized string. Then append that string
to the list initialized. Return that list.

1. init 'wave_list' to an empty list.
2. iterate over the input string using a range.
    - init 'word' to an empty string.
    - iterate over every char in the input string.
        - if the char is not at the index referenced by the range, convert it to lowercase.
        - if it is, convert it to uppercase.
            - either way, add it to word.
    - append 'word' to 'wave_list'
3. return 'wave_list'

C:
'''
def wave(strng):
    wave_list = []
    # create wave
    for i in range(len(strng)):
        word = ''
        for j in range(len(strng)):
            if j == i:
                char = strng[j].upper()
            else:
                char = strng[j].lower()
            word += char
        wave_list.append(word)
    # clean wave_list
    wave_list = [wave_word for wave_word in wave_list if any(char.isupper() for char in wave_word)]

    return wave_list

print(wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
print(wave("") == [])
print(wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])