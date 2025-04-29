'''
Our countdown to launch isn't behaving as expected.
Why? Change the code so that our program successfully
counts down from 10 to 1 before launching.
'''
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)
    counter -= 1 # implemented code

print('LAUNCH!')

# The variable 'counter' is never reassigned to a decreasing integer throughout the for loop.