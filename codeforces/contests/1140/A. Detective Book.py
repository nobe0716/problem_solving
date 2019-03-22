n = int(input())
a = list(map(int, input().split()))

cur_pos = 0
current_revealed = 0
c = 0
while cur_pos < n:
    c += 1
    current_revealed += 1
    # current_revealed = max(a[cur_pos], current_revealed)
    while cur_pos < current_revealed:
        current_revealed = max(current_revealed, a[cur_pos])
        # print(cur_pos + 1, end = ' ')
        cur_pos += 1
    # print('')
    # current_revealed += 1
    # current_revealed = next_revealed
print(c)
