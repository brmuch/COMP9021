
# coding: utf-8

# In[64]:


from random import *
import sys
import numpy as np
import math

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
    
# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randrange(51)*(1 if np.random.rand()>0.5 else -1 )for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()

total = 0
L.sort()
for n in L:
    total += n
    
print(f"The mean is {total/len(L):.2f}")

if(len(L)%2==1):
    print(f"The median is {L[len(L)//2+1]:.2f}")
else:
    print(f"The median is {(L[len(L)//2-1]+L[len(L)//2])/2}")
    
std_dev = 0
for i in L:
    std_dev += np.square(i-total/len(L))

print(f"The standard deviation is {np.sqrt(std_dev/len(L)):.2f}\n")
    
print("Confirming with functions from the statistics module:\n")
print(f"The mean is {np.mean(L):.2f}")
print(f"The median is {np.median(L):.2f}")
print(f"The standard deviation is {np.std(L):.2f}")
    

