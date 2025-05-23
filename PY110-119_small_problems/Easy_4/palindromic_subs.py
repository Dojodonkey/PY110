'''
Problem Statement:
Write a function that returns a list of all palindromic substrings of a string.
That is, each substring must consist of a sequence of characters that reads the same
forward and backward.
The substrings in the returned list should be sorted by
their order of appearance in the input string.
Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise,
you should consider all characters and pay attention to case;
that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not.
In addition, assume that single characters are not palindromes.
'''
def palindromes(strng):
    char_lst = list(strng)
    palindromes_lst = []
    sub_str = ''

    while char_lst:
        for char in char_lst:
            sub_str += char
            if sub_str == sub_str[::-1] and len(sub_str) >= 2:
                palindromes_lst.append(sub_str)
        char_lst.pop(0)
        sub_str = ''
    return palindromes_lst




print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True