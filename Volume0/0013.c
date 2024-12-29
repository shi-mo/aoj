#include <stdio.h>

int
main(int argc, char *argv[])
{
    unsigned int NUM_CARS_MAX = 10;
    unsigned int id, stack[NUM_CARS_MAX], top;

    top = 0;
    while (1 == scanf("%u\n", &id)) {
        if (id) {
            stack[top++] = id;
            continue;
        }
        printf("%u\n", stack[--top]);
    }

    return 0;
}
