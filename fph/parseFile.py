# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

import FPHFile
from summary import SummaryFile
from detail import DetailFile

def parseFile(filename):
	parts = filename.split('/')

	prefix = parts[-1][0:3]

	if (prefix == 'SUM'):
		return SummaryFile(filename)
	elif (prefix == 'DET'):
		return DetailFile(filename)
	else:
		return FPHFile(filename)