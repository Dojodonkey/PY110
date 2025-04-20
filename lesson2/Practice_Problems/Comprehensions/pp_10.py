'''
problem statemnt:
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items,
even when some of those items were created on a different server or by a different application.
That is, without any synchronization, two or more computer systems can create new items and
label them with a UUID with no significant risk of stepping on each other's toes.
It accomplishes this feat through massive randomization.
The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number.
The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string.
The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed.
There are several UUID versions, each with some non-random characteristics in some of the bits.
These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.

Understanding the problem:

    - input: none
    - output: string

    explicit rules:
    - output string is made up of 32 random alphanumeric characters.
    - the string is seperated by '-' 4 times to create an 8-4-4-4-12 pattern.

    implicit rules:
    -none

    questions: none

Examples/Test Cases:

'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

- understanding confirmed.

Data Structures:
- lists to contain the seqments of the ouput string.
- string to be output

Algorithm:
1. import random and string modules.
2. initilalize 'str_list' to an empty list.
4. depending on the amount of elements in 'str_list':
    - if 'str_list' is empty, 'length' is 8.
    - if there is 1 element, 'length' is 4.
    - if there are 2 elements, 'length' is 4.
    - if there are 3 elements, 'length' is 4.
    - if there are 4 elements, 'length' is 12.
5. define 'uuid_segment' function to accept 0 parameters.
    1. initialize 'chars' to attributes of the string module, ascii_letters and digits.
    2. add 'segment' of randomly generated chars to 'str_list'
6. use a loop to generate 'segments' based on length of 'str_list'.
7. return a joined string of elements in 'str_result'

Code:
'''
import random
import string

# to determine how many random chars to generate:
def determine_len():
    length = len(result_list)
    match length:
        case 0:
            return 8
        case 1 | 2 | 3:
            return 4
        case 4:
            return 12

# to generate segments:
def segment_generator():
    hex_chars = 'abcdef'
    chars = hex_chars + string.digits
    result_list.append(''.join(random.choice(chars) for _ in range(determine_len())))

result_list = []

while len(result_list) < 5:
    segment_generator()

print('-'.join(result_list))
