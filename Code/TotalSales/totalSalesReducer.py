#!/usr/bin/python

import sys
from operator import itemgetter

current_key = None
current_count = 0.0
key = None
line_count = 0

for line in sys.stdin:
	line = line.strip()
	key,count = line.split('\t')
	
	try:
		count = float(count)
	except ValueError:
		continue

	current_count += count 
	line_count += 1

print ("Total Sales: ", line_count, "Total Value of Sales: ", current_count)
