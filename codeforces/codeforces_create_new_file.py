from pathlib import Path

import requests
from bs4 import BeautifulSoup

print('# enter url of prob')
url_of_prob = input()
# url_of_prob = 'https://codeforces.com/contest/276/problem/C'
url_of_prob = url_of_prob.strip()
tokens = url_of_prob.split('/')

if 'problemset' in url_of_prob:
    contest_no = tokens[-2]
    prob_no = tokens[-1]
else:
    contest_no = tokens[-3]
    prob_no = tokens[-1]

res = requests.get(url_of_prob)
soup = BeautifulSoup(res.text, 'html.parser')

name_of_prob = soup.select('.title')[0].text

Path("contests/{}".format(contest_no)).mkdir(parents=True, exist_ok=True)

file_path = 'contests/{}/{}.py'.format(contest_no, name_of_prob)
print('# file path: {}'.format(file_path))
with open(file_path, 'w') as f:
    f.write('# {}\n'.format(url_of_prob))
