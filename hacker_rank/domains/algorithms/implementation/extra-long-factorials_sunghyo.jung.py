__author__ = 'sunghyo.jung'
n = int(raw_input().strip())
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print fact(n)