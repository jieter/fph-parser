# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from collections import namedtuple
import FPHFile

class SummaryFile(FPHFile.FPHFile):

	SUMMARY_RECORD_SIZE = 0x1d
	SUMMARY_RECORD = (
		('timestamp', '4s'),
		('runtime', 'B'),
		('usage', 'B'),
		('_', '7s'),
		('leak90', 'H'),
		('lowPressure', 'B'),
		('highPressure', 'B'),
		('_', 's'),
		('apneaEvents', 'B'),
		('hypoapneaEvents', 'B'),
		('flowlimitiationEvents', 'B'),
		('_', '3s'),
		('pressure1', 'B'),
		('pressure2', 'B'),
		('_', '2s'),
		('humiditySetting', 'B')
	)

	SummaryRecord = namedtuple('SummaryRecord',
		[x[0] for x in SUMMARY_RECORD if x[0] != '_']
	)

	def _parseBody(self):
		f = self.raw
		f.seek(self.HEADER_SIZE)

		transforms = {
			'timestamp': self._parseTimestamp,
			'runtime': self._parseDuration,
			'usage': self._parseDuration
		}

		while (True):
			record = f.read(self.SUMMARY_RECORD_SIZE)
			if record[0:2] == '\xFE\xFA':
				break

			self.records.append(
				self.SummaryRecord._make(
					self._parseRecord(self.SUMMARY_RECORD, record, transforms)
				)
			)
