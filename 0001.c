#include <stdio.h>

#define NUM_RANKING 3
int
main(int argc, char *argv[])
{
    int i;
    unsigned long v, top[NUM_RANKING] = {0, 0, 0};

    while (EOF != scanf("%lu\n", &v)) {
        for (i = 0; i < NUM_RANKING; i++) {
            unsigned long tmp;
            if (v < top[i]) continue;

            tmp = top[i];
            top[i] = v;
            v = tmp;  // shift ranking
        }
    }

    for (i = 0; i < NUM_RANKING; i++) {
        printf("%lu\n", top[i]);
    }
    return 0;
}
