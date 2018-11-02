
# coding: utf-8

# In[21]:


# Written by Eric Martin for COMP9021


'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the number of elements equal to 0, 1, 2 3 modulo 4, and prints those out.
'''


from random import seed, randrange
import sys
from math import floor

def form_print(group,length):
    if (length == 0):
        print(f"There is no elements between {5*group} and {5*group+4}")
    elif (length == 1):
        print(f"There is 1 element between {5*group} and {5*group+4} ")
    else:
        print(f"There are {length} elements between {5*group} and {5*group+4}")
    
        
        
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
    
# Generates a list of nb_of_elements random integers between 0 and 19.
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()

remainders_modulo_4 = [0] * 4
for e in L:
      if (e >= 15):
            remainders_modulo_4[3] += 1
      elif (e >= 10):
            remainders_modulo_4[2] += 1
      elif (e >= 5):
            remainders_modulo_4[1] += 1
      else:
            remainders_modulo_4[0] += 1

for i in [0,1,2,3]:
        form_print(i,remainders_modulo_4[i])
        
        

