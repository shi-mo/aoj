import string

def main():
    c = input()
    if c in string.digits:
        print('digit')
        return
    if c in string.ascii_lowercase:
        print('lower')
        return
    if c in string.ascii_uppercase:
        print('upper')
        return
    print('other')

main()