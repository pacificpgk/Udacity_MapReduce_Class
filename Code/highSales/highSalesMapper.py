#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if (len(data)) == 6 and data[2] in ("Reno", "Toledo", "Chandler"):
		date, time, store, item, cost, payment = data
		print ("{0}\t{1}".format(store, cost))
