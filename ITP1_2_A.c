#include <stdio.h>

int
main(int argc, char *argv[])
{
    int a, b;
    scanf("%d %d\n", &a, &b);

    if (a < b) {
        puts("a < b");
        return 0;
    }
    if (a > b) {
        puts("a > b");
        return 0;
    }
    puts("a == b");
    return 0;
}
