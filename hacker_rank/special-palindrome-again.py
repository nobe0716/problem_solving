#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
	t = []
	a = None
	c = 0
	for e in s:
		if e != a:
			if a is not None:
				t.append((a, c))
			a, c = e, 1
		else:
			c += 1
	t.append((a, c))

	r = 0
	for a, c in t:
		r += c * (c + 1) // 2

	for i in range(1, len(t) - 1):
		if t[i][1] == 1 and t[i - 1][0] == t[i + 1][0]:
			r += min(t[i - 1][1], t[i + 1][1])
	return r


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	s = input()

	result = substrCount(n, s)

	fptr.write(str(result) + '\n')

	fptr.close()