#include<stdio.h>

#define MAX_N 300000
#define MAX_T 150000
#define MAX_V 1000000000000
#define min(a, b) (a < b ? a : b)

long long int solve(int n, long long int *a, long long int *b) {
    long long int x, y;
    long long int rest_point = 0;
    long long int min_rest_point = MAX_V;
    for (int i = 0; i < n; ++i) {
        x = a[i];
        y = b[(i == 0) ? (n - 1) : (i - 1)];
        if (x > y) {
            rest_point += (x - y);
            min_rest_point = min(min_rest_point, y);
        } else {
            min_rest_point = min(min_rest_point, x);
        }
        //printf("%lld %lld\n", x, y);
    }
    //printf("rest_point: %lld min_rest_point: %lld = %lld\n", rest_point, min_rest_point, rest_point + min_rest_point);
    return rest_point + min_rest_point;
}

int main(int argc, char **argv) {
    int n, t;
    long long int a[MAX_N];
    long long int b[MAX_N];
    long long int r[MAX_T];
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        scanf("%d", &n);
        for (int j = 0; j < n; ++j) {
            scanf("%lld %lld", &a[j], &b[j]);
        }
        r[i] = solve(n, a, b);
    }
    for (int i = 0; i < t; ++i) {
        printf("%lld\n", r[i]);
    }
    return 0;
}