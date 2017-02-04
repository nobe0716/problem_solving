import re
s = raw_input()
#s = 'a b c ddd'
tok = re.findall('([a-zA-Z]+)', s)
print len(tok)
for s in tok:
    print s