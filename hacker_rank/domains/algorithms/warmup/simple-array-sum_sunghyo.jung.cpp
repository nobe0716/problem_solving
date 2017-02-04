#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int sum = 0;
    int number;
    cin >> n;
    for(int i = 0 ; i < n ; ++i) {
        cin >> number;
        sum += number;
    }
    cout << sum << endl;
    return 0;
}
