'''
n; total action
k; # of candies in the box

x; # of ate
y; # of input

k = y * (y + 1) // 2 - x
  = (y**2 + y) // 2 - x


0 = y**2 + y - 2x -2k (x + y = n => x = n - y)

0 = y**2 + y - 2(n - y) - 2k
0 = y**2 + -y - 2k - 2n

y = (1 +- sqrt(1 + 8k + 8n)) /2

y must be positive => y = (1 + sqrt(1 + 8k + 8n)) // 2



'''
import math

n, k = map(int, input().split())

y = (-3 + math.sqrt(9 + 8 * (k + n)))
y //= 2
print(int(n - y))
