# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys


def sum_all_factor(n):
    total = 0
    i = 1
    while i < n:
        if n % i == 0:
            total += i 
        i += 1

    return total

try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for i in range(2, N + 1):
    if (sum_all_factor(i) == i):
        print(f"{i} is a perfect number.")
