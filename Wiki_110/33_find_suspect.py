'''
# Sherlock has to find suspects on his latest case. He will use your method.
# Suspect in this case is a person which has something not allowed in his/her
# pockets.
# Allowed items are defined by an array of numbers.
# Pockets contents are defined by map entries where key is a person and
# value is one or few things represented by an
# array of numbers (can be nil or empty array if empty).

P:
- input: dictionary containing names of suspects mapped to a list containing integers (items allowed).
- ouput: list of suspects w/ items not allowed.

- explicits:
    - if a suspect (in 'pockets') has an item that is not listed in input list, add 'suspect' to list.
    and return list of suspects.
- implicits:
    - allowed item list can be any length, including empty.

- questions: none

D:
- list to contain 'suspects' that have items that are not allowed (ouput)

A:
- High Level Strategy -
iterate through 'pockets'. if an item in value not in input list, append the key to 'suspects'.

1. init 'suspects' to an empty list.
2. iterate through 'pockets' using key and value.
    - iterate through the value and if any element is not in 'allowed_items',
    append key to 'suspects'.
3. return 'suspects'

C:
'''
def find_suspects(pockets, allowed_items):
    suspects = []

    for suspect, pocket in pockets.items():
        for item in pocket:
            if item not in allowed_items:
                suspects.append(suspect)
                break

    return suspects if len(suspects) > 0 else None

pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])