n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

index_of_book = {}
book_of_index = {}

for i in range(n):
    index_of_book[a[i]] = i
    book_of_index[i] = a[i]

last_index = 0
r = []
for book in b:
    if book not in index_of_book:
        r.append(0)
        continue
    new_last = index_of_book[book] + 1
    r.append(new_last - last_index)
    for i in range(last_index, new_last):
        del index_of_book[book_of_index[i]]
    last_index = new_last

print(" ".join(map(str, r)))
