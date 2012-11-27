#include <stdio.h>

int
main(int argc, char *argv[])
{
    unsigned long n, i;

    if (1 != scanf("%lu\n", &n)) {
        fprintf(stderr, "Invalid number of data set.\n");
        return 1;
    }

    for (i = 1; i <= n; i++) {
        unsigned long a, b, c;
        if (3 != scanf("%lu %lu %lu\n", &a, &b, &c)) {
            fprintf(stderr, "Invalid data at line %lu\n", i);
            continue;
        }
        if (!a || !b || !c) {
            puts("NO");
            continue;
        }
        if ( (a*a == (b*b + c*c))
            || (b*b == (c*c + a*a))
            || (c*c == (a*a + b*b) )) {
            puts("YES");
            continue;
        }
        puts("NO");
    }
    return 0;
}
