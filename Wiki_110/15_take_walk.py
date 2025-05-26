'''
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment,
so you decided to take the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones
-- every time you press the button it sends you a list of one-letter strings
representing directions to walk (e.g., ['n', 's', 'w', 'e']).
 You always walk only a single block in a direction,
 and you know it takes you one minute to traverse one city block.
 Create a function that will return `True`
 if the walk the app gives you will take you exactly ten minutes
 (you don't want to be early or late!) and will, of course,
 return you to your starting point.
 Return `False` otherwise.

Note: You will always receive a valid list
 containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
 It will never give you an empty list (that's not a walk, that's standing still!).

P:

- input: list containing directions
- output: bool

- explicits:
    - it takes 1 min to walk a city block.
    - you always walk a single city block in a direction.
    - return True, if you return to the starting point in exactly 10 minutes
- implicits:
    - directions can repeat themselves.

- questions: none

E:
is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
is_valid_walk(['w']) # should return False
is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return False

D:
- integers to keep track of directions walked.

A:
- High Level Strategy:
The starting point is 0. 'n' and 's' correlate to each other as do 'e' and 'w'.
if the corresponding variables when subtracted result to the starting point,
return True. The directions list may not contain more than 20 steps.

1. init 'start' as a constant to 0.
2. init directions 'n_blocks', etc... to 0.
3. if the list contains more than 20 elements, return False.
4. iterate over the list and add +1 to the corresponding variable.
5. if the corresponding 'blocks' subtracted result to 0, return True,
otherwise, False.

C:
'''
def is_valid_walk(directions):
    START = 0

    n_blocks = 0
    s_blocks = 0
    e_blocks = 0
    w_blocks = 0

    if len(directions) != 10:
        return False

    for block in directions:
        match block:
            case 'n':
                n_blocks += 1
            case 's':
                s_blocks += 1
            case 'e':
                e_blocks += 1
            case 'w':
                w_blocks += 1

    return (
        n_blocks - s_blocks == START
        and e_blocks - w_blocks == START
    )
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # should return True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # should return False
print(is_valid_walk(['w'])) # should return False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # should return False
