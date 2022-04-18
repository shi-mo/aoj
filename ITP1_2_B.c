#include <stdio.h>

int
main(int argc, char *argv[])
{
    int a, b, c;
    scanf("%d %d %d\n", &a, &b, &c);

    if ((a < b) && (b < c)) {
        puts("Yes");
        return 0;
    }
    puts("No");
    return 0;
}
