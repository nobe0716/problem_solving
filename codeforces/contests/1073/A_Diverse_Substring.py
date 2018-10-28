n = int(input())
s = input().strip()

for i in range(n - 1):
    if s[i] != s[i + 1]:
        print("YES\n" + s[i:i + 2])
        exit()
print("NO")
