'''
Author: Spencer Norris
File: contributions_by_industry.py
Description: Accepts an industry ID and a year, queries
the OpenSecrets API for all candidate contributions
in the given year to candidates from that particular industry.
'''

import json
import sys
import os

def query(industry_code, cycle):
	pass


if __name__ == '__main__':
	code = sys.argv[1]
	cycle = sys.argv[2]
	query(code, cycle)
	sys.exit(0)