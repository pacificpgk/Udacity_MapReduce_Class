#!/usr/bin/python

import sys
from operator import itemgetter

current_key = None
max_count = 0.0
key = None

for line in sys.stdin:
	line = line.strip()
	key,count = line.split('\t')
	
	try:
		count = float(count)
	except ValueError:
		continue

	if current_key == key:
		if (max_count > count):
			continue
		else:
			max_count = count
	else:
		if current_key:
			print ('%s   %s' % (current_key, max_count))
		max_count = count
		current_key = key

if current_key == key:
        print ('%s   %s' % (current_key, max_count))

