'''
Create a function that takes a string argument
and returns a copy of the string with every second character
in every third word converted to uppercase.
Other characters should remain the same.

P:
- input: string
- output: string

- explicits:
    - return a string based on the input string, with every second character of every third word,
    converted to uppercase.
    - other chars, remain unmodified.
- implicits:
    - white spaces are disregarded.

D:
- list to split input string and select and transform words based on index position.
- string to join that list after index reassignment.

A:
- High Level Strategy -
iterate through a list of words based on input string, select every third word,
and transform to uppercase chars in odd indexes.

1. init 'lst_split' to a list of words
2. iterate through 'lst_split' using a count to select every third word.
3. iterate through that word, convert chars at odd indexes to upper case.
    - replace method, but set a count not to replace all occurrences of that char.
4. return a joined string based on 'lst_split'.

C:
'''
def to_weird_case(strng):
    strng_split = strng.split()

    for i in range(2, len(strng_split), 3):
        strng_split[i] = ''.join([char.upper() if j % 2 == 1
                                  else char for j, char in enumerate(strng_split[i])])

    return ' '.join(strng_split)


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
