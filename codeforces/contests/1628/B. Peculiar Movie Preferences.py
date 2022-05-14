# 2022-05-14T19:00:54.921Z
import sys
from collections import Counter
from functools import lru_cache

input = sys.stdin.buffer.readline


@lru_cache(None)
def reverse(s: str):
    return s[::-1]


def proc(n, movies) -> bool:
    def is_palindrome(s: str) -> bool:
        return s == reverse(s)

    if any(is_palindrome(s) for s in movies):
        return True

    original_counter = Counter(movies)
    current_counter = original_counter.copy()
    for prefix in movies:
        if reverse(prefix) in current_counter:
            return True
        if len(prefix) == 3 and reverse(prefix[:2]) in current_counter:
            return True

        if current_counter[prefix] == 1:
            del current_counter[prefix]
        else:
            current_counter[prefix] -= 1

    current_counter = original_counter.copy()
    for suffix in movies[::-1]:
        if reverse(suffix) in current_counter:
            return True
        if len(suffix) == 3 and reverse(suffix[1:]) in current_counter:
            return True

        if current_counter[suffix] == 1:
            del current_counter[suffix]
        else:
            current_counter[suffix] -= 1

    return False


# assert proc(2, ["ab", "bad"]) is False

for _ in range(int(input().strip())):
    n = int(input().strip())
    movies = [input().strip() for _ in range(n)]

    print('YES' if proc(n, movies) else 'NO')
