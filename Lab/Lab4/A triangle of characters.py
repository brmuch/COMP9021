# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.
import sys

def print_space(num):
    for _ in range(0, num):
        print(" ", end = '')

def tract_list(lists):
    temp = lists[::-1]
    lists.pop()
    return lists + temp

N = int(input("Enter strictly positive number: "))
lists = [65]
num = 1

for i in range(0, N):
    print_space(N-1-i)
    next = lists[-1]
    lists = tract_list(lists)

    for j in range(0, len(lists)):
        if j != len(lists)-1:
            print(f"{chr(lists[j])}", end="")
        elif i != N-1:
            print(f"{chr(lists[j])}")
        else:
            print(f"{chr(lists[j])}")

    lists.clear()
    for j in range(1, 3+i):
        if next < ord("Z"):
            next = next + num
            lists.append(next)
        else:
            next = ord("A")
            lists.append(next)