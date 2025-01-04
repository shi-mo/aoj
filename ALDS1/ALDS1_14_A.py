import re

def main():
    t = input()
    p = input()
    pat = re.compile(re.escape(p))

    for i in range(len(t)):
        if t[i:].startswith(p):
            print(i)

main()