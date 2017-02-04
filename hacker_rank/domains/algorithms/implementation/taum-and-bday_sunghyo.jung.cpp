#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    long long int x, y, b, w, z;

    scanf("%d", &t);
    for(;t > 0 ; --t)
    {
        scanf("%lld %lld %lld %lld %lld", &x, &y, &b, &w, &z);
        b = b < w + z ? b : w + z;
        w = w < b + z ? w : b + z;
        cout << (x * b + y * w) << endl;
    }
    return 0;
}
