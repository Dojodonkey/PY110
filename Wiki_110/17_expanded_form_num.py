'''
You will be given a number, and you need to return it as a string in
expanded form. For example:

expanded_form(12) # should return '10 + 2'
expanded_form(42) # should return '40 + 2'
expanded_form(70304) # should return '70000 + 300 + 4'

Note: All numbers will be whole numbers greater than 0.

P:
- input: integer
- output: string

- explicits:
    - turn an integer into an expanded string.
    - an expanded string is made of integers, using their place,
    to describe their values when added up.
- implicits:
    - none

- questions: none

D:
- string to use the integer as a sequence.
- strings to describe 'places' in that string.

A:
- High Level Strategy:
first convert the input integer into a string.
then beginning from the last char, the ones place, determine its value.
do this for all the places in the string.
if any of the values are a 0, upon hitting a char that is not 0, add those 0's passed over.
return all the places with a '+' between them.

1. convert input int into a string and assign it to 'str_value'.
2. iterate over 'str_value' beginning with the last char.
3. 'one' is the first char, 'ten' the second', etc..
    - if any char is 0, move to the next iteration.
    - when a non-0 char is encountered, add the amount of 0's skipped.
4. return variables seperated by '+'.

# for some reason ended up using a dictionary. unnecessary, but kind of a cool solution.
C:
'''
def expanded_form(number):
    num_str = str(number)
    places = {}

    for idx, num in enumerate(num_str[::-1]):
        places[idx] = num + str('0' * idx)


    return ' + '.join(sorted([value for value in places.values()
                              if any(char != '0' for char in value)],
                              key =int, reverse=True))


print(expanded_form(12)) # should return '10 + 2'
print(expanded_form(42)) # should return '40 + 2'
print(expanded_form(70304)) # should return '70000 + 300 + 4'
