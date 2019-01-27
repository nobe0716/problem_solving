s = input()
l = len(s)

left_colon_pos = None
left_bracket_pos = None
right_colon_pos = None
right_bracket_pos = None

for i in range(l):
    if left_bracket_pos is None and s[i] == '[':
        left_bracket_pos = i
    if left_bracket_pos is not None and s[i] == ':':
        left_colon_pos = i
    if left_bracket_pos is not None and left_colon_pos is not None:
        break

for i in range(l - 1, 0, -1):
    if right_bracket_pos is None and s[i] == ']':
        right_bracket_pos = i
    if right_bracket_pos is not None and s[i] == ':':
        right_colon_pos = i
    if right_bracket_pos is not None and right_colon_pos is not None:
        break

if left_colon_pos is None or right_colon_pos is None or not (left_colon_pos < right_colon_pos):
    print(-1)
else:
    c = len(list(filter(lambda x: x == '|', s[left_colon_pos:right_colon_pos])))
    print(c + 4)
