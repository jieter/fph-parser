#!/usr/bin/env python2.7

#
# Fisher and Paykel CPAP .FPH file parser.
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from fph.fphfile import parseFile
import sys

if __name__ == "__main__":
	args = sys.argv

	if args[1]:
		filename = args[1];

		print parseFile(filename)
