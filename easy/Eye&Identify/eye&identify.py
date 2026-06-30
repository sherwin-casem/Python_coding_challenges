import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
mat = np.eye(n, m, k=0)
print(mat)