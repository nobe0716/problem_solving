#include<stdio.h>
#define MAX_L 131073


int main(int argc, char** agv) {
    int n, m;
    int a[17][MAX_L] = {0};
    int p, b;
    int l = 1;

    scanf("%d %d", &n, &m);
    for (int i = 0 ; i < n ; ++i) {
        l *= 2;
    }

    for (int i = 1 ; i <= l ; ++i) {
        scanf("%d", &a[0][i]);
    }
    for (int i = 1, k = l / 2 ; i <= n ; ++i, k /= 2) {
        for (int j = 1 ; j <= k ; ++j) {
            if (i % 2 == 1) {
                a[i][j] = a[i - 1][j * 2 - 1] | a[i - 1][j * 2];
            } else {
                a[i][j] = a[i - 1][j * 2 - 1] ^ a[i - 1][j * 2];
            }
        }
    }

    for (int i = 0 ; i < m ; ++i) {
        scanf("%d %d", &p, &b);

        if (a[0][p] != b) {
            a[0][p] = b;
            for (int j = 0 ; j < n ; ++j) {
                int k = (p % 2 == 1) ? p + 1 : p - 1;
                if (j % 2 == 0) {
                    b = a[j][k] | b;
                } else {
                    b = a[j][k] ^ b;
                }
                p = (p + 1) / 2;
                if (a[j + 1][p] == b) {
                    break;
                }
                a[j + 1][p] = b;
            }
        }
        printf("%d\n", a[n][1]);
    }
}