def integer_to_string(number):
    int_str_map = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    str_result = ''
    while number > 10:
        digit = number % 10
        value = int_str_map[digit]
        str_result += value
        number //= 10

    value = int_str_map[number]
    str_result += value

    return str_result[::-1]

def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True