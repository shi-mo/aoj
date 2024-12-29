#include <stdio.h>

int
main(int argc, char *argv[])
{
    int a, b, c, d, e, f;

    while (6 == scanf("%d %d %d " "%d %d %d\n", &a, &b, &c, &d, &e, &f)) {
        double det, x, y;

        det = a*e - b*d;
        x = (c*e - b*f) / det;
        y = (-c*d + a*f) / det;
        x = (double)((long)(x * 1000)) / 1000;
        y = (double)((long)(y * 1000)) / 1000;
        printf("%.3f %.3f\n", x, y);
    }
    return 0;
}
