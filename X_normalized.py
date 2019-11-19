import numpy as np
a = np.random.random((5,5))
b = np.mean(a)
c = np.std(a)
d = (a-b)/c

print(d)