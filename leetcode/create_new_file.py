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

    if len(contents) >= 2 and len(contents[-1]) == 0:
        break

f = open(name_of_prob + '.py', 'w')
f.write('\n'.join(contents))
f.close()
print('# write finished')
