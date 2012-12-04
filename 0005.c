#include <stdio.h>

int
main(int argc, char *argv[])
{
    unsigned long a, b;

    while (EOF != scanf("%lu %lu\n", &a, &b)) {
        unsigned long i, gcd, lcm;

        for (gcd = 1, i = 2; (i <= a) && (i <= b); i++) {
            while (1) {
                if (a % i) break;
                if (b % i) break;
                gcd *= i;
                a /= i, b /= i;
            }
        }
        lcm = a * b * gcd;

        printf("%lu %lu\n", gcd, lcm);
    }

    return 0;
}
