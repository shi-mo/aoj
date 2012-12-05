#include <stdio.h>

void
calc_line_params(double x1, double y1, double x2, double y2, double *ap, double *bp, double *cp)
{
    *ap = y1 - y2;
    *bp = x2 - x1;
    *cp = y1*x2 - y2*x1;
}

/*
 * Determinant for maxrix:
 *   |a  b|
 *   |d  e|
 */
double
det_for(double a, double b, double d, double e)
{
    return a*e - b*d;
}

void
calc_cross_point(double a, double b, double c, double d, double e, double f, double *cxp, double *cyp)
{
    double det = det_for(a, b, d, e);
    *cxp = (c*e - b*f) / det;
    *cyp = (a*f - c*d) / det;
}

int
judge_cross_point_is_valid(double x1, double y1, double x2, double y2, double x3, double y3, double xp, double yp)
{
        double a, b, c, d, e, f, cx, cy;

        calc_line_params(x1, y1, x2, y2, &a, &b, &c);
        calc_line_params(x3, y3, xp, yp, &d, &e, &f);

        if (!det_for(a, b, d, e)) return 0;
        calc_cross_point(a, b, c, d, e, f, &cx, &cy);

        if ((x1 < cx) && (x2 < cx)) return 0;
        if ((cx < x1) && (cx < x2)) return 0;
        if ((y1 < cy) && (y2 < cy)) return 0;
        if ((cy < y1) && (cy < y2)) return 0;
        return 1;
}

int
main(int argc, char *argv[])
{
    double x1, y1, x2, y2, x3, y3, xp, yp;

    while (EOF != scanf("%lf %lf %lf %lf %lf %lf %lf %lf\n", &x1, &y1, &x2, &y2, &x3, &y3, &xp, &yp)) {
        if (judge_cross_point_is_valid(x1, y1, x2, y2, x3, y3, xp, yp)
            && judge_cross_point_is_valid(x2, y2, x3, y3, x1, y1, xp, yp)
            && judge_cross_point_is_valid(x3, y3, x1, y1, x2, y2, xp, yp)
            ) {
            puts("YES");
            continue;
        }
        puts("NO");
    }

    return 0;
}
