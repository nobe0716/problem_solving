print('# enter url of prob')
url_of_prob = input()
url_of_prob = url_of_prob.strip()
name_of_prob = url_of_prob.split('/')[-2]
print('# file name will be `{}.py`'.format(name_of_prob))
print('# past contents her. trl-D or Ctrl-Z ( windows ) to save it.')
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

    if len(contents) >= 2 and len(contents[-1].strip()) == 0:
        break

f = open(name_of_prob + '.py', 'w')
if any('List' in _ for _ in contents):
    print('# append typing import')
    contents = ["from typing import List\n\n"] + contents
f.write('\n'.join(contents))
# for test creation
f.write('\n        return None\n')
f.write('\n\ns = Solution()\nassert s.\n')
f.close()
print('# write finished go to file:\n{}'.format(name_of_prob))
print('')
