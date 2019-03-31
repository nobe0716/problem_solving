"""
## Name of Prob
Common Anagrams

## Link
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/00000000000510f2

## Note
### anagrammatic
String A의 문자들을 재배치 했을 때, String B와 일치하는 경우가 있다.
String A와 String B가 정확하게 같은 문자의 수로 이뤄져있다.

### anagrammatic substrings
String B의 부분문자열(substring) 중에서, String A와 anagrammatic 한 것이 있을 때
String A를 String B의  anagrammatic substrings 이라 한다.

## Input

l; length of string
a, b ; 문자열 a, b가 line 마다 주어짐

## Output

a의 문자열 중에서, b의 anagrammatic substring 인 것의 수

## Strategy
input string 이 대문자로만 이뤄져 있기 때문에,
string 하나를 26-size의 tuple로 표현할 수 있다. (encoding)
B 를 해부해서, size 별로 substring을 구한 다음 tuple 로 encoding
encoding 한 tuple 을 앞의 size 별로 나눈 bucket(set)에 저장한다.

A 의 substring 마다 tuple을 만들어보며,
substring의 길이에 맞는 bucket에 일치 여부를 확인
"""
import string
from collections import Counter

_DEBUG = False
num_of_test = int(input())


def encode_counter(c):
    return tuple(c[e] for e in string.ascii_uppercase)


def solve(length_of_str, a, b):
    b_counter_sets = [set() for _ in range(length_of_str + 1)]
    for i in range(1, length_of_str + 1):
        for j in range(0, length_of_str - i + 1):
            counter = Counter(b[j:j + i])
            b_counter_sets[i].add(encode_counter(counter))

    if _DEBUG:
        for i in range(length_of_str + 1):
            print("{} => {}".format(i, b_counter_sets[i]))

    num_of_ana_substr = 0
    for i in range(1, length_of_str + 1):
        for j in range(0, length_of_str - i + 1):
            counter = Counter(a[j:j + i])
            encoded_counter = encode_counter(counter)

            if _DEBUG:
                print("{} => {}".format(a[j:i], encoded_counter))

            if encoded_counter in b_counter_sets[i]:
                num_of_ana_substr += 1

    return num_of_ana_substr


for test_num in range(1, num_of_test + 1):
    solution = None
    length_of_str = int(input())
    a, b = input(), input()

    solution = solve(length_of_str, a, b)
    print("Case #{}: {}".format(test_num, solution))
