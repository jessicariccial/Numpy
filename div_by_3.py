import numpy as np
J = np.arange(1,101)
E = np.reshape(J,(10,10))
C = np.square(E)
A = J[J%3==0]

print(A)