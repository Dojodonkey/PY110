'''
# Write a function that splits the string into pairs of two characters.
# If the string contains an odd number of characters,
# replace the missing second character of the final pair with an underscore ('_').

P:
- input: string
- output: list

- explicits:
    - return a list containing pairs of characters from input string.
    - if the string contains an odd amount of chars, the last char is paired with '_'.
- implicits:
    - if string is empty, return an empty list.

- questions: none

D:
- string to make pairs.
- range to iterate through input string.
- list for output.

A:
- High Level -
init 'result' to an empty list.
iterate over the string using even indexes as a step count.
    if the index is not the list index, append the char of that index + the next char.
    if it is, append just that char.
then check if any strings in 'result' do not have a length of two.
    if true, use element reassignment and add '_' to the last string.

C:
'''
def solution(strng):
    if not strng:
        return []

    result = []
    for i in range(0, len(strng), 2):
        if i + 1 < len(strng):
            result.append(strng[i] + strng[i +1])
        else:
            result.append(strng[i] + '_')

    return result



print(solution('abc') == ['ab', 'c_'])
print(solution('abcdef') == ['ab', 'cd', 'ef'])
print(solution("abcdef") == ["ab", "cd", "ef"])
print(solution("abcdefg") == ["ab", "cd", "ef", "g_"])
print(solution("") == [])