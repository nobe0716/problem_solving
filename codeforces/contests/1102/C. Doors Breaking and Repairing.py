'''
사실 매우 쉬운 문제였다.
x, y 의 대소 관계아 따라 답이 정해진다

x > y: eventually 모든 doors 는 부서진다

x <= y: 내구도가 x 이하인 문 C개를 부수고 고치는 작업이 경쟁적으로 일어난다.
    선공을 하는 X 가 1개 더 부술 수 있기 때문에 (C + 1) // 2가 필요하다.
'''
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
smaller_count = sum([1 for k in a if k <= x])
if x > y:
    print(n)
else:
    print((smaller_count + 1) // 2)
