# Removed numpy dependency

def arrays(arr):
    # complete this function without numpy
    arr = [float(x) for x in arr]
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)