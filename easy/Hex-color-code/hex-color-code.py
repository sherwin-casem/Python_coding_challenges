import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        line = input()

        matches = re.findall(r'(?<!^)(#[0-9a-fA-F]{3,6})', line)

        for m in matches:
            if len(m) == 4 or len(m) == 7:  # # + 3 or 6 digits
                print(m)
