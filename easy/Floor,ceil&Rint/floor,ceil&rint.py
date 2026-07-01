import numpy as np
np.set_printoptions(legacy='1.13')

my_list = list(map(float, input().split()))

print(np.floor(my_list))
print(np.ceil(my_list))
print(np.rint(my_list))
