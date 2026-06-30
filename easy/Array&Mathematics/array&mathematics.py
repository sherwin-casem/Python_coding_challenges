import numpy as np
n, m = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(A//B)
print(np.mod(A, B))
print(np.power(A, B))
