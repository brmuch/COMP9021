# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.

from math import sqrt, ceil


def is_form_number(num):
    list1 = sorted(range(0, floor(sqrt(num)) - 1), reverse= True)
    list2 = sorted(range(0, floor(sqrt(num))))
    for i in list1:
        for j in list2:
            if i*i + j*j == num:
                if i < j:
                    return True,i,j
                else:
                    return True,j,i
    return False,-1,-1

for i in range(100, 998):
      judge1,m1,n1 = is_form_number(i)
      judge2,m2,n2 = is_form_number(i+1)
      judge3,m3,n3 = is_form_number(i+2)
      if judge1 and judge2 and judge3 :
          print(f"({i}, {i+1}, {i+2}) (equal to ({m1}^2+{n1}^2, {m2}^2+{n2}^2, {m3}^2+{n3}^2)) is a solution.")