#include <stdio.h>

int
main(int argc, char *argv[])
{
    unsigned long n, m;

    scanf("%lu\n", &n);
    m = n*n*n;
    printf("%lu\n", m);
    return 0;
}
