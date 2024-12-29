import std.algorithm;
import std.array;
import std.conv;
import std.stdio;
import std.string;

void main() {
    int n = readln().strip().to!int;
    auto p = readln().split.map!(x => x.to!double).array;
    auto q = readln().split.map!(x => x.to!double).array;

    double[][] dp = new double[][](n, n);
    double[][] sb = new double[][](n, n);

    foreach (w; 0 .. n) {
        foreach (i; 0 .. n - w) {
            if (w <= 0) {
                dp[i][i] = p[i] + (2 * (q[i] + q[i + 1]));
                sb[i][i] = p[i] + q[i] + q[i + 1];
                continue;
            }

            int j = i + w;
            double sum = sb[i][j - 1] + p[j] + q[j + 1];
            sb[i][j] = sum;

            double t = q[i] + dp[i + 1][j];
            foreach (k; i + 1 .. j) {
                double s = dp[i][k - 1] + dp[k + 1][j];
                if (s < t) t = s;
            }
            double s = dp[i][j - 1] + q[j + 1];
            if (s < t) t = s;
            dp[i][j] = sum + t;
        }
    }

    writefln("%.8f", dp[0][n - 1]);
}
