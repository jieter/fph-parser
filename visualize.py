#!/usr/bin/env python2.7

# Dump file contents to CSV at stdout
#
# Fisher and Paykel CPAP .FPH file parser.
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

import os
from datetime import date
import shutil

from fph.parseFile import parseFile


def copyUSB():
	# ubuntu mounts the USB stick on /media/<user>/FPHCARE/
	srcdir = '/media/%s/FPHCARE/FPHCARE/ICON/' % os.getlogin()
	if (not os.path.isdir(srcdir)):
		return

	srcdir += os.listdir(srcdir)[0]

	dstdir = 'data/' + str(date.today())
	if (os.path.isdir(dstdir)):
		raise Exception('Directory already exists (%s)' % dstdir)

	os.mkdir(dstdir)

	for srcfile in os.listdir(srcdir):
		shutil.copy(srcdir + '/' + srcfile, dstdir)

def lastLog():
	os.chdir('data/')
	files = os.listdir('.')
	files.sort(reverse=True)
	os.chdir('../')
	return files[0]

def lastSummary():
	last = lastLog()
	f = parseFile('data/' + last + '/SUM0001.FPH')

	w = open('site/summary.csv', 'w')
	w.write(f.toCSV())

	return last

try:
	copyUSB()
	print 'Copied files from FPHCARE InfoUSB'
except Exception, e:
	print e.message + '; skipped.'

print 'Generated summary from %s in site/summary.csv' % lastSummary()
