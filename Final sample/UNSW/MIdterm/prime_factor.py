# pass a value to function, and return the sum of all prime factor of the number
from math import sqrt, ceil
def prime_factor(num):
    lists = set()
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            lists.add(i)
            lists.add(num//i)
    return sum(lists) + 1
print(prime_factor(48))

