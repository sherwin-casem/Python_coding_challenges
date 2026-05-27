import re

pattern = r"^[789]\d{9}$"

for _ in range(int(input())):
    number = input()
    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")
