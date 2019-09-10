b = int(input())
g = int(input())
n = int(input())

# n - min(n, b) <= (actual # of girl) <= min(n, g)
print(min(n, g) - (n - min(n, b)) + 1)
