import re

t = int(input())
for _ in range(t):
    s = input()
    if (len(s) == 10 and
        re.search(r"[A-Z].*[A-Z]", s) and
        len(re.findall(r"\d", s)) >= 3 and
        s.isalnum() and
        len(set(s)) == 10):
        print("Valid")
    else:
        print("Invalid")
