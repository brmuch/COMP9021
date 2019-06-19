#python 3 written by Ran Bai
import numpy as np
from scipy.linalg import solve
a = np.array([[1/150, -1/90, -1/60, 0, 0, 0], [0, 0, 13/600, -1/90, 0, 0], [0, 0, 0, 0, -1/600, 5/180], [-1/150, 29/1800, 0, -1/60, 0, 0], [0, 0, 0, -1/300, 53/1800, -5/180], [1, 1, 1, 1, 1, 1]])
b = np.array([0, 0, 0, 0, 0, 1])
x = solve(a, b)
print("The solution is :")
print(x)