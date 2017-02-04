__author__ = "sunghyo.jung@gmail.com"

def is_pangrams(str):
    s = set()
    for ch in str.upper():
        s.add(ch)
    for ch in map(chr, range(ord('A'), ord('Z') + 1)):
        if not ch in s:
            return False
    return True

print "pangram" if is_pangrams(raw_input()) else "not pangram"