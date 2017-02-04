#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

queue<int> q;

int main() {
    int t;
    cin >> t;
    for(; t > 0 ; --t) {
        int n, m;
        int s;
        int pivot;
        int map[1001][1001] = {0};
        int visited[1001] = {0};
        int cost[1001] = {0};

        cin >> n >> m;
        for(int i = 0 ; i < m ; ++i) {
            int a, b;
            cin >> a >> b;
            
            map[a][b] = 6;
            map[b][a] = 6;
        }
        cin >> s;
        
        q.push(s);
        do {
            pivot = q.front();
            q.pop();
            
            for(int i = 1 ; i <= n ; ++i) {
                if(visited[i] == 0 && map[pivot][i] != 0) {
                    visited[i] = 1;
                    q.push(i);
                    cost[i] = cost[pivot] + map[pivot][i];
                }
            }
        } while(!q.empty());
     
        for(int i = 1 ; i <= n ; ++i) {
            if(i == s) continue;
            if(cost[i] == 0) {
                cout << -1 << " ";
            }
            else {
                cout << cost[i] << " ";
            }
        }
        cout << endl;
    }
    
    
    return 0;
}