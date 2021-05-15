from bisect import bisect
from collections import defaultdict

numbers = input()

number_occurrences = defaultdict(list)

for i, e in enumerate(numbers):
    number_occurrences[e].append(i)

bloom_filter = set()
res = None


def is_found(i):
    if i % 100 in bloom_filter or i % 10 in bloom_filter:
        return False

    token = str(i)

    if len(number_occurrences[token[0]]) == 0:
        bloom_filter.add(i)
        return False

    idx = number_occurrences[token[0]][0]

    for e in token[1:]:
        new_idx = bisect(number_occurrences[e], idx)
        if new_idx == len(number_occurrences[e]):
            bloom_filter.add(i)
            return False
        idx = number_occurrences[e][new_idx]

    return True


for i in range(0, 1001, 8):
    if is_found(i):
        res = i
        break

if res is None:
    print('NO')
else:
    print('YES\n{}'.format(res))
