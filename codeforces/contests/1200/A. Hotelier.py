rooms = [None] * 10
n = int(input())
s = input()


def find_from_left():
    for i in range(10):
        if rooms[i] == None:
            return i
    return None


def find_from_right():
    for i in range(9, -1, -1):
        if rooms[i] == None:
            return i
    return None


for e in s:
    if e == 'L':
        room_no = find_from_left()
        rooms[room_no] = e
    elif e == 'R':
        room_no = find_from_right()
        rooms[room_no] = e
    else:
        room_no = int(e)
        rooms[room_no] = None
print(''.join(map(lambda x: '0' if x is None else '1', rooms)))
