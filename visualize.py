#!/usr/bin/env python2.7

# Dump file contents to CSV at stdout
#
# Fisher and Paykel CPAP .FPH file parser.
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

import os
from fph.parseFile import parseFile

def lastLog():
	os.chdir('data/')
	files = os.listdir('.')
	files.sort(reverse=True)
	os.chdir('../')
	return files[0]


f = parseFile('data/' + lastLog() + '/SUM0001.FPH')

w = open('site/summary.csv', 'w')
w.write(f.toCSV())
