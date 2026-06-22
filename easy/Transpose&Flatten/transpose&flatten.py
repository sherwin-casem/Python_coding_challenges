import numpy as np

# Read input
n, m = map(int, input().split())

# Read the matrix
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Convert to numpy array
np_arr = np.array(arr)

# Print transpose
print(np.transpose(np_arr))

# Print flattened array
print(np_arr.flatten())
