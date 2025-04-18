'''
Problem Statement:
Write a program that solicits six (6) numbers from the user and
prints a message that describes whether the sixth number appears among the first five.

- Understanding the problem:
    - input: 6 integers
    - output: string depending on a condition.

    explicit rules:
        - user is prompted to provide 6 integers
        - output a string describing whether the 6th number is included in the 5 previous integers provided.
    implicit rules:
        - input must be integers
    questions:
        - None

- Test Cases/Examples:

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

- Data Structures:
    - list []
        - as input can repeat itself, sets or frozensets would not work.

- Algorithm:
    1. initialize 'int list' to an empty list.
    2. prompt user input and add data to 'int list'.
        - strip input data of any white space.
    3. initialize 'last num' to 6th integer of user input.
    4. initialize a 'int string' to a string containing all members of 'int list' for output message.
    5. check if 'last num' is in 'int list'.
        - output confirmation message.
        - if not:
            - output display message.

- Code:
'''
int_list = []

int_list.append(input('Enter first integer: ').strip())
int_list.append(input('Enter second integer: ').strip())
int_list.append(input('Enter third integer: ').strip())
int_list.append(input('Enter fourth integer: ').strip())
int_list.append(input('Enter fifth integer: ').strip())
last_num = (input('Enter last integer: ').strip())
# for output strings:
ints_string = ', '.join(int_list)
# conditional determining output:
if last_num in int_list:
    print(f'{last_num} appears in {ints_string}')
else:
    print(f'{last_num} does not appear in {ints_string}')

'''
Further Exploration:
Suppose we alter the problem to look for a number that satisfies a condition
(e.g., a number greater than 25) instead of a specific number?
Would the current solution still work? Why or why not?
- The current solution would not work as is because our input values are never actually converted to integers.
- We would still append input to a list but as integers.
- for the display messages we would then have to convert the elements of the list into strings and join them to make a string.
    - we could do this using the join method and passing in a ternary expression using the built-in string function.
- Lastly our conditional would be based on a comparison expression and not for membership as is currently.
'''