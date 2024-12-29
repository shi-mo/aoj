#include <stdio.h>
#include <string.h>

int
main(int argc, char *argv[])
{
    const int INPUT_LEN_MAX = 20 + 1; /* +1 for \n */
    char buf[INPUT_LEN_MAX+1];
    int n, i;

    fgets(buf, INPUT_LEN_MAX, stdin);
    buf[INPUT_LEN_MAX] = '\0';

    n = strlen(buf);
    if (feof(stdin)) return 0;
    for (i = n-1; 0 <= i; i--) {
        int c = buf[i];
        if ('\n' == c) continue;
        putchar(c);
    }
    putchar('\n');
    return 0;
}
