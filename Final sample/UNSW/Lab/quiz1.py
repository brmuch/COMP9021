import sys
from random import seed, randrange

#define court_alphabets to court the number of alphabet in a digits
def court_alphabets(digits):
    court = set()
    while (digits > 0):
        court.add(digits % 10)
        digits = digits // 10
    return len(court)

try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()
dicts = {}
# REPLACE THIS COMMENT WITH YOUR CODE

print()
print('x is:', x)
print('L is:', L)
print()


#sum every digits in x
sum_of_digits_in_x = sum([int(str(x)[e]) for e in range(len(str(x)))])
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()

for e in L:
    #court the number of first_digit_greater_than_last and same_first_and_last_digits and last_digit_greater_than_first
    if (e // 10 ** (len(str(e)) - 1) > e % 10):
        first_digit_greater_than_last += 1
    elif (e // 10 ** (len(str(e)) - 1) == e % 10):
        same_first_and_last_digits += 1
    else:
        last_digit_greater_than_first += 1

    #calculate the max_gap and min_gap between first digit and last digit
    if abs((e // 10 ** (len(str(e)) - 1)) - e % 10) > max_gap:
        max_gap = abs((e // 10 ** (len(str(e)) - 1)) - e % 10)
    if abs((e // 10 ** (len(str(e)) - 1)) - e % 10) < min_gap:
        min_gap = abs((e // 10 ** (len(str(e)) - 1)) - e % 10)

	#calculate the different number among a digit
    distinct_digits[court_alphabets(e)] += 1

	#calculate the number of same pairs in 10 random numbers
    try:
        dicts[(e // 10 ** (len(str(e)) - 1), e % 10)] += 1
    except KeyError:
        dicts[(e // 10 ** (len(str(e)) - 1), e % 10)] = 0

for key,value in dicts.items():
    if(value == max(dicts.values())):
        first_and_last.add(key)

#Output according to the corresponding format
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
      )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
      )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
      )