'''
Write a function that takes a string as an argument and returns that string with
every occurrence of a "number word"
-- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' --
converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.
'''
def word_to_digit(line):
    digit_str = ['zero', 'one', 'two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine', 'ten']
    words_in_line = line.split()
    output_lst = []

    for word in words_in_line:
        if word not in digit_str:
            output_lst.append(word)
        else:
            match word:
                case 'zero':
                    output_lst.append('0')
                case 'one':
                    output_lst.append('1')
                case 'two':
                    output_lst.append('2')
                case 'three':
                    output_lst.append('3')
                case 'four':
                    output_lst.append('4')
                case 'five':
                    output_lst.append('5')
                case 'six':
                    output_lst.append('6')
                case 'seven':
                    output_lst.append('7')
                case 'eight':
                    output_lst.append('8')
                case 'nine':
                    output_lst.append('9')
    return ' '.join(output_lst)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
