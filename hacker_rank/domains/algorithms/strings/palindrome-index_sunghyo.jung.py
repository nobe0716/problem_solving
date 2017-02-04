__author__ = 'sunghyo.jung'
for i in xrange(int(raw_input())):
    s = raw_input()
    if s == s[::-1]:
        print -1
        continue

    for j in xrange(len(s)):
        if s[j] != s[len(s) - 1 - j]:
            t = s[:j] + s[j + 1:]
            if t == "".join(reversed(t)):
                print j
            else:
                print (len(s) - 1 - j)
            break
