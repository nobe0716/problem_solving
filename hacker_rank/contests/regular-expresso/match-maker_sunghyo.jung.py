Regex_Pattern = r'^(a+([^fi]|b[cf])$|ag|be|bhd|d[^id]|e[^h]|h[be]|i[^f]|j[^h])'


positive_inputs = ['bhdgffhfa', 'aggjjaaga', 'hbefebhfi', 'dbceeabih', 'ihifdbhhf', 'djacfjbae', 'ibjbeigac', 'jaffigdad', 'aaaaaaaaj', 'dgifecchi', 'dcbhgjaaf', 'eedfbcedb', 'aaaaaaabf', 'beaajbihg', 'aaaaaaaag', 'eacccdjeh','aaaaaaaad', 'hehcijfhc', 'aaaaaaaaa', 'aaaaaaabc', 'jfdhdeice']
negative_inputs = ['aaaaaaaai', 'ehigcbgjd', 'hgjdeajec', 'aaaaaaabe', 'haebgiggc', 'aaaaaaaba','aaaaaaaaf', 'bfjhehbcf', 'diieabefh', 'jhjcaeead', 'ifbjdgibf','dddbgcgai', 'bbcafhcif', 'hfjciccbi', 'fdbgidjdj', 'aaaaaaabb', 'jhdibgbfj','cfjbaijad', 'bhgjfacgi', 'ehhieihhh', 'abijjabda']

import re

def test_one(s):
    return bool(re.search(Regex_Pattern, s))


if len(Regex_Pattern) > 60:
    print "Warning : Length of regular expression greater than 60 characters."

for s in positive_inputs:
    if not test_one(s):
        print "Problem with: " + s
for s in negative_inputs:
    if test_one(s):
        print "Problem with: " + s
