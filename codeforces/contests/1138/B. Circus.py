"""
wip
"""
n = int(input())
c = input()
a = input()

performers = []
for clowns, acrobats in zip(c, a):
    performers.append(clowns + acrobats)
performers = enumerate(performers)
print(performers)

losers = []
only_clowns = []
only_acrobats = []
winners = []

for performer in performers:
    if performer[1] == '11':
        winners.append(performer)
    elif performer[1] == '10':
        only_clowns.append(performer)
    elif performer[1] == '01':
        only_acrobats.append(performer)
    else:
        losers.append(performer)

groups = [[], []]
while len(only_clowns) > 0 and len(only_acrobats) > 0:
    groups[0].append(only_clowns.pop())
    groups[1].append(only_acrobats.pop())

while len(only_clowns) > 0 and len(winners) > 0:
    groups[0].append(only_clowns.pop())
    groups[1].append(winners.pop())

while len(only_acrobats) > 0 and len(winners) > 0:
    groups[0].append(winners.pop())
    groups[1].append(only_acrobats.pop())

while len(only_clowns) > 0 and len(losers) > 0:
    groups[0].append(losers.pop())
    groups[1].append(only_clowns.pop())

while len(only_acrobats) > 0 and len(losers) > 0:
    groups[0].append(only_acrobats.pop())
    groups[1].append(losers.pop())

if len(losers) % 2 != 0 or len(winners) % 2 != 0 or len(only_clowns) > 0 or len(only_acrobats) > 0:
    print(-1)
    exit(0)

for rest in winners, losers:
    if len(rest) > 0:
        groups[0] += losers[:len(rest) // 2]
        groups[1] += losers[len(rest) // 2:]

print(' '.join(map(lambda x: str(x[0] + 1), groups[0])))
