import re
import email.utils

pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        name, email = email.utils.parseaddr(input())

        if re.match(pattern, email):
            print(email.utils.formataddr((name, email)))
