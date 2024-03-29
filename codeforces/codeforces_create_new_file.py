import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

print('# enter url of prob')
print('# time: {}'.format(datetime.datetime.now()))
url_of_prob = input()
url_of_prob = url_of_prob.strip()
if url_of_prob.endswith('#'):
    url_of_prob = url_of_prob[:-1]
# url_of_prob = 'https://codeforces.com/contest/276/problem/C'
tokens = url_of_prob.split('/')

if 'problemset' in url_of_prob:
    contest_no = tokens[-2]
    prob_no = tokens[-1]
else:
    contest_no = tokens[-3]
    prob_no = tokens[-1]

res = requests.get(url_of_prob, allow_redirects=True)
soup = BeautifulSoup(res.text, 'html.parser')

name_of_prob = soup.select('.title')[0].text

Path("contests/{}".format(contest_no)).mkdir(parents=True, exist_ok=True)

file_path = 'contests/{}/{}.py'.format(contest_no, name_of_prob)
print('# file path: {}'.format(file_path))

FILE_TEMPLATE = """# {}
# {}
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    #print = sys.stdout.write

for _ in range(int(input())):
"""

with open(file_path, 'w') as f:
    f.write(FILE_TEMPLATE.format(datetime.datetime.now(), url_of_prob))
