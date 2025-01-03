import re

def main():
    t = input()
    p = input()
    pat = re.compile(re.escape(p))

    for pos in find_all_matches_in(t, pat):
        print(pos)

def find_all_matches_in(s, pat):
    matches = []
    for i in range(len(s)):
        m = re.search(pat, s[i:])
        if m: matches.append(i+m.start())
    return list(dict.fromkeys(matches))

main()