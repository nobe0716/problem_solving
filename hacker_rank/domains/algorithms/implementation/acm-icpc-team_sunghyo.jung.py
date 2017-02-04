__author__ = 'sunghyo.jung'
import itertools
n,m = map(int, raw_input().strip().split())
topic = []
for i in xrange(n):
    topic.append(int(raw_input(), 2))
maximum_number_of_topics = 0
number_of_team = 0
for i, j in itertools.combinations(range(n), 2):
    c = bin(topic[i] | topic[j]).count('1')
    if c > maximum_number_of_topics:
        maximum_number_of_topics = c
        number_of_team = 1
    elif c == maximum_number_of_topics:
        number_of_team += 1
print maximum_number_of_topics
print number_of_team