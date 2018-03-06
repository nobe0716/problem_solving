"""
    s; 톱니바퀴를 나타내는 문자열 배열
    s[i]; (i + 1)번재 톱니바퀴
        s[0]; 첫 번째 톱니바퀴
"""
s = [input() for _ in range(4)]
n = int(input())


def rotate(s, n, c):
    """
    s; 톱나바퀴 배열
    n; 회전시킬 톱니바퀴 번호
    c: 시계방향(1)/반시계방향(-1) 을 의미
    """
    if c is 1:
        s[n] = s[n][7] + s[n][:7]
    else:
        s[n] = s[n][1:] + s[n][0]


def choose(candidates, cur):
    """
    회전시킬 톱니바퀴를 결정하는 함수
    candidates; 회전 시킬 톱니바퀴를 의미
    cur; 현재 인덱스
    
    현재 인덱스에서 왼쪽(cur - 1)과 오른쪽(cur + 1)을 순회한다
    방문했던 인덱스를 다시 방문하지 않기 위해 candidates 에 인덱스가 존재하는지 확인한다.

    현재 톱니바퀴의 9시 방향 s[cur][6]과 오른쪽 톱니바퀴의 3시 방향 s[cur - 1][2]이 다르면 회전
    현재 톱니바퀴의 3시 방향 s[cur][2]과 오른쪽 톱니바퀴의 9시 방향 s[cur + 1][6]이 다르면 회전
    """
    if 0 <= (cur - 1) and (cur - 1) not in candidates:
        if s[cur][6] != s[cur - 1][2]:
            candidates.add(cur - 1)
            choose(candidates, cur - 1)
    if (cur + 1) < 4 and (cur + 1) not in candidates:
        if s[cur][2] != s[cur + 1][6]:
            candidates.add(cur + 1)
            choose(candidates, cur + 1)

for _ in range(n):
    e, f = list(map(int, input().split()))
    e -= 1
    # 회전해야 될 톱니바퀴를 set에 저장한다. (l)
    l = {e}
    choose(l, e)

    # 각 톱니바퀴를 회전해야 한다.
    for candidate in l:
        """
        입력 받은 톱니바퀴 기준으로, 2의 배수 칸만큼 떨어져있으면 인력 받은 시계/반시계 방향으로 회전
        그게 아닌 경우엔 반대로 회전해야 한다.
        """

        if (candidate - e) % 2 == 0:
            rotate(s, candidate, f)
        else:
            rotate(s, candidate, f * -1)

print(int(s[3][0] + s[2][0] + s[1][0] + s[0][0], 2))