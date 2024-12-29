#include <stdio.h>

int
main(int argc, char *argv[])
{
    int s;
    scanf("%d\n", &s);
    printf("%d:%d:%d\n", s/3600, (s/60)%60, s%60);
    return 0;
}
