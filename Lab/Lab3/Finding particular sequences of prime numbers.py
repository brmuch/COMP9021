# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here
import math

def generate_prime(number):
    return list(filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(10000, number + 1)))

prime_set = generate_prime(100_000)

print("The solutions are:\n")

for i in range(0, len(prime_set) - 4):
   if prime_set[i+1] == prime_set[i] + 2 and prime_set[i+2] == prime_set[i] + 6 and prime_set[i+3] == prime_set[i] +12 and prime_set[i+4] == prime_set[i] + 20 and prime_set[i+5] == prime_set[i] + 30:
        print(f"{prime_set[i]} {prime_set[i+1]} {prime_set[i+2]} {prime_set[i+3]} {prime_set[i+4]} {prime_set[i+5]}")
