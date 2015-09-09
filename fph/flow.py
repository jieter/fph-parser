# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from struct import calcsize, unpack
from collections import namedtuple
from datetime import timedelta, datetime

from FPHFile import FPHFile

class FlowFile(FPHFile):



	END_OF_CHUNK = 0xff7f
	CHUNK_RECORD = (
		('samples', '100s'), # 50 16bit samples
		('pressure', 'H'),
		('leakAdjustment', 'B'),
		('eor', 'H')
	)


	def _parseBody(self):
		f = self.raw
		f.seek(self.HEADER_SIZE)

		format = '<' + ''.join([x[1] for x in self.CHUNK_RECORD])

		while True:
			(samples, pressure, leakAdjustment, eor) = unpack(format, f.read(calcsize(format)))

			print pressure, leakAdjustment, eor
			if eor == self.END_OF_CHUNK:
				break;




		print self._parseTimestamp(f.read(4))