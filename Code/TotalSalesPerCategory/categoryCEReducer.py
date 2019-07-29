#!/usr/bin/python

import sys
from operator import itemgetter

current_key = None
current_count = 0.0
key = None

for line in sys.stdin:
	line = line.strip()
	key,count = line.split('\t')
	
	try:
		count = float(count)
	except ValueError:
		continue

	if current_key == key:
		current_count += count
	else:
		if current_key:
			print ('%s   %s' % (current_key, current_count))
		current_count = count
		current_key = key

if current_key == key:
        print ('%s   %s' % (current_key, current_count))	
