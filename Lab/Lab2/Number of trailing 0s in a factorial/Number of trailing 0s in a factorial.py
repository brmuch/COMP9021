# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

#divide 10 until th number of x%10 is not equal to 0
def first_computation(x):
    nb_of_trailing_0s = 0

    while(x%10 == 0):
        nb_of_trailing_0s += 1
        x = x//10
    return nb_of_trailing_0s

#Convert N! into a string and find the rightmost occurrence of a character different to 0
def second_computation(x):
    for i in range(1,len(x)):
        if(x[-i] != '0'):
            return i-1

#N! has at least as many multiples of 2 as multiples of 5.
def third_computation(x):
    nb_of_trailing_0s = 0
    power_of_five = 5

    while(power_of_five < x):
        nb_of_trailing_0s += x//power_of_five
        power_of_five = 5*power_of_five

    return nb_of_trailing_0s

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))