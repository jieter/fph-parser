#!/usr/bin/env python2.7

# Dump file contents to CSV at stdout
#
# Fisher and Paykel CPAP .FPH file parser.
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

import sys
from fph.parseFile import parseFile

if __name__ == "__main__":
	args = sys.argv

	if len(args) > 1 and args[1]:
		filename = args[1];

		print parseFile(filename).toCSV()

	else:
		print 'No file supplied.'
		print 'Usage: ./dumpcsv.py <file.FPH>'
