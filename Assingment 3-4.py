#Lab Assignment-1 (simple):

import numpy as np
print(np.eye(4))

a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))

print(a)
print(b)

print(a + b)
print(a.dot(b))




#Lab Assignment-2 

import numpy as np

print("Enter 15 numbers for 5x3 matrix (space separated):")
vals1 = list(map(int, input().split()))
matrix1 = np.array(vals1).reshape(5, 3)

print("Enter 6 numbers for 3x2 matrix (space separated):")
vals2 = list(map(int, input().split()))
matrix2 = np.array(vals2).reshape(3, 2)

product = matrix1.dot(matrix2)
print(product)