To illustrate, 15!, the factorial of 15, is equal to 1307674368000, hence has 3 trailing 0s.

There are at least three methods to compute the number of trailing 0s in the factorial of a number N at least equal to 5:

Divide N! by 10 for as long as it yields no remainder. Note that for a positive integer x, x // 10 "removes" the rightmost digit from x, that digit being equal to x % 10.

Convert N! into a string and find the rightmost occurrence of a character different to 0. A Google search, or executing dir(str) at the python prompt, suggests which string method to use. Note that negative indexes (-1 being the index of the last character in a string, -2 the index of the penultimate character in a string, etc.) is particularly convenient here.

Python computes such huge numbers as 1000!, either iteratively multiplying all numbers from 1 up to 1000 or using factorial() from the math module (executing import math and then dir(math) at the python prompt confirms that this function is available), and the first two methods work for such numbers, but there is a much better method that operates on N rather N!, hence that does not suffer the limitations of the first two, and is very efficient. The number of trailing 0s in N! is equal to the number of times N! is a multiple of 10, so to the number of times N! is a multiple of 2 x 5. It is easy to verify that N! has at least as many multiples of 2 as multiples of 5. Hence the number of trailing 0s in N!

is equal to the number of times N! is a multiple of 5

which is equal to the number of times 5 occurs in the prime decompositions of 1, 2, ..., N-1 and N

which is equal to the number of times 5 occurs at least once in the prime decompositions of 1, 2, ..., N-1 and N, plus the number of times 5 occurs at least twice in the prime decompositions of 1, 2, ..., N-1 and N, plus the number of times 5 occurs at least thrice in the prime decompositions of 1, 2, ..., N-1 and N...

which is equal to the number of multiples of 5 at most equal to N, plus the number of multiples of 5^2 at most equal to N, plus the number of multiples of 5^3 at most equal to N ...

Insert your code into trailing_0s.py so that the program prompts the user for a nonnegative integer N. If the input is incorrect then the program outputs an error message and exits. Otherwise the program computes 5! three times, using the three methods just described. See sample outputs for details on input and ouput. If you are stuck, but only when you are stuck, then use trailing_0s_scaffold_1.py. If you are still stuck, but only when you are still stuck, then use trailing_0s_scaffold_2.py.