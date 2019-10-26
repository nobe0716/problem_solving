import math




def solve(a, b, c, d, k):
	require_min_pen = math.ceil(a / c)
	require_min_pencil = math.ceil(b / d)
	if require_min_pen + require_min_pencil > k:
		return None
	return require_min_pen, require_min_pencil


t = int(input())
for _ in range(t):
	"""
		a: lectures
		b: practical classes
		c: one pen can draw `c` blueprints of `lecture`
		d: one pencil can draw `d` practical `classes`
		k: pencilcase c+ d <= d
	"""
	a, b, c, d, k = map(int, input().split())
	e = solve(a, b, c, d, k)
	print(-1 if e is None else ' '.join(map(str, e)))
