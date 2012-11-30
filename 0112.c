#include <stdio.h>
#include <stdlib.h>

int
read_data(FILE *fp, unsigned int n, unsigned int data[])
{
    int i;

    for (i = 0; i < n; i++) {
        if (1 != fscanf(fp, "%u\n", &data[i])) {
            fprintf(stderr, "Invalid data at line %u.\n", i+2);
            return 1;
        }
    }
    return 0;
}

unsigned long
calc_total_wait(unsigned int n, unsigned int data[])
{
    unsigned long total_wait = 0;
    int i;

    int compare(const void *a, const void *b) {
        return *((unsigned int*)a)-*((unsigned int*)b);
    };
    qsort(data, n, sizeof(data[0]), compare);
    for (i = 0; i < (n-1); i++) {
        total_wait += data[i] * (n - (i+1));
    }

    return total_wait;
}

int
main(int argc, char *argv[])
{
    int NUM_DATA_MAX = 10000;
    unsigned int n, data[NUM_DATA_MAX];

    while ((1 == scanf("%u\n", &n)) && n) {
        unsigned long total_wait;
        int ret;

        if ((ret = read_data(stdin, n, data))) {
            return ret;
        }
        total_wait = calc_total_wait(n, data);
        printf("%lu\n", total_wait);
    }

    return 0;
}
