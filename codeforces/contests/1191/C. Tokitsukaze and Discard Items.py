n, m, k = map(int, input().split())
p = list(map(int, input().split()))

page_num = 1
shifted = 0
removed_without_shift = 0
num_of_operation = 1
for e in p:
    relative_pos = e - shifted
    if relative_pos <= page_num * k:  # this special pos removed without any shift
        removed_without_shift += 1
    else:
        if removed_without_shift > 0:
            num_of_operation += 1
            shifted += removed_without_shift
            relative_pos = e - shifted
        page_num = (relative_pos + k - 1) // k
        removed_without_shift = 1
print(num_of_operation)
