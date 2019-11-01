n = int(input())
sticks = list(map(int, input().split()))
 
 
def solve(n, sticks):
	sticks = sorted(sticks, reverse=True)
	return sum(sticks[:(n + 1) // 2]) ** 2 + sum(sticks[(n + 1) // 2:]) ** 2
 
 
r = solve(n, sticks)
print(r)
