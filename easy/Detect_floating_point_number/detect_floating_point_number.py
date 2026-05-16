import re

pattern = r'^[+-]?\d*\.\d+$'

T = int(input())

for _ in range(T):
    N = input()
    print(bool(re.match(pattern, N)))
