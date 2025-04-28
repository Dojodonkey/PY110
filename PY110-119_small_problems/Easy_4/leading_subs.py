'''
Leading Substrings

Strategy:
return a list containing the first char in the string
with every element after adding a char to the sub string.
'''
def leading_substrings(strng):
    sub_lst = []
    sub = ''
    for char in strng:
        sub += char
        sub_lst.append(sub)

    return sub_lst


print(leading_substrings('abc') == ['a', 'ab', 'abc'])