#include<stdio.h>
#define MAX_N 200005
#define max(a, b) (a > b ? a : b)

int n;
int a[MAX_N];
int ans[MAX_N];
int events[MAX_N][3];
int q;
int op, p, x;
int max_val = 0;

int main(int argc, char** argv) {
  scanf("%d", &n);
  for (int i = 0 ; i < n ; ++i) {
    ans[i] = -1;
  }

  for(int i = 0 ; i < n ; ++i) {
    scanf("%d", &a[i]);
  }
  scanf("%d", &q);

  for(int i = 0 ; i < q ; ++i) {
    scanf("%d", &op);
    events[i][0] = op;
    if(op == 1) {
      scanf("%d %d", &p, &x);
      events[i][1] = p - 1;
      events[i][2] = x;
    } else {
      scanf("%d", &x);
      events[i][1] = x;
    }
  }

  for(int i = q - 1 ; i >= 0 ; --i) {
    if (events[i][0] == 1) {
      if (ans[events[i][1]] == -1) {
        ans[events[i][1]] = max(max_val, events[i][2]);
      }
    } else if (max_val < events[i][1]) {
      max_val = events[i][1];
    }
  }

  for (int i = 0 ; i < n ; ++i) {
    if (ans[i] == -1) {
      printf("%d ", max(a[i], max_val));
    } else {
      printf("%d ", ans[i]);
    }
  }
  printf("\n");
  return 0;
}
