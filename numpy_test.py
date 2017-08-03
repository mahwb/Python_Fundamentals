import numpy as np
from numpy.linalg import inv

# 3 by 3 matrice from 0-9
a = np.arange(9).reshape(3,3)
print a
# creates identity matrix
b = np.identity(3)
print b
# inverse of b which should still be the identity matrix
print inv(b)
# dot product
print np.dot(a,b)