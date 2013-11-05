#!/usr/bin/env python2.7

# Dump a list of sleep sessions (not CPAP sessions) to stdout
#
# Fisher and Paykel CPAP .FPH file parser.
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

import sys
from fph.parseFile import parseFile
from fph.summary import SummaryFile, SleepsSummary


if __name__ == "__main__":
	args = sys.argv

	if len(args) > 1 and args[1]:
		filename = args[1];

		f = parseFile(filename)
		if (not isinstance(f, SummaryFile)):
			raise 'Supplied file is not a summary file'

		print SleepsSummary(f).toCSV()

	else:
		print 'No file supplied.'
		print 'Usage: ./sleeps.py <SUM????.FPH>'
