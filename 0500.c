#include <stdio.h>

int
main(int argc, char *argv[])
{
    unsigned long n, i, score_a, score_b;
    unsigned int a, b;

    while (1) {
        if (1 != scanf("%lu\n", &n)) {
            fprintf(stderr, "Invalid number of datasets at line 0.");
            return 1;
        }
        if (0 == n) {
            break;
        }

        score_a = 0, score_b = 0;
        for (i = 1; i <= n; i++) {
            if (2 != scanf("%u %u\n", &a, &b)) {
                fprintf(stderr, "Invalid data at line %lu.", i);
                continue;
            }
            if (a < b) {
                score_b += (a + b);
                continue;
            }
            if (b < a) {
                score_a += (a + b);
                continue;
            }
            score_a += a;
            score_b += b;
        }
        printf("%lu %lu\n", score_a, score_b);
    }

    return 0;
}
