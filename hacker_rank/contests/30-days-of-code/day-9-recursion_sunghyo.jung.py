def find_gcd(a,b):
    if b == 0:
        return a
    return find_gcd(b,a%b)
#Take input
a, b = map(int, raw_input().split())
gcd=find_gcd(a,b)
print gcd