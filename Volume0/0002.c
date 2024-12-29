#include <stdio.h>

void
print_num_digits_for(unsigned long a, unsigned long b)
{
    unsigned int num_digits, carry;

    if (0 == a && 0 == b) {
        puts("1");
        return;
    }

    num_digits = 0, carry = 0;
    while (a || b || carry) {
        int ia, ib;

        num_digits++;
        ia = a % 10, a /= 10;
        ib = b % 10, b /= 10;
        carry = (ia + ib + carry) / 10;
    }
    printf("%u\n", num_digits);
}

int
main(int argc, char *argv[])
{
    unsigned int BUF_LEN = 256;
    char buf[BUF_LEN];
    while(fgets(buf, BUF_LEN, stdin)) {
        unsigned long a, b;

        if (EOF == sscanf(buf, "%lu %lu\n", &a, &b)) break;
        print_num_digits_for(a, b);
    }

    return 0;
}
