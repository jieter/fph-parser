# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from collections import namedtuple
from datetime import timedelta, datetime
from FPHFile import FPHFile

class SummaryFile(FPHFile):

	END_OF_DATA = '\xFE\xFA'

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

		while True:
			record = f.read(self.SUMMARY_RECORD_SIZE)
			if record[0:2] == self.END_OF_DATA:
				break

			self.records.append(
				self.SummaryRecord._make(
					self._parseRecord(self.SUMMARY_RECORD, record, transforms)
				)
			)

class SleepsSummary(FPHFile):
	def __init__(self, summaryFile, split_threshold = 2):
		self.split_threshold = split_threshold

		self.header = summaryFile.header
		self.records = self._group(summaryFile)

	def _group(self, summaryFile):
		sleeps = []
		end = None

		keys = 'runtime apneaEvents hypoapneaEvents flowlimitiationEvents'.split(' ')

		Sleep = namedtuple('Sleep', ['timestamp'] + keys)
		make = lambda start, values: Sleep._make([start] + values)

		threshold = timedelta(hours = self.split_threshold)

		for s in summaryFile.records:
			start = s.timestamp
			if (end is None or end + threshold < start):
				if (end is not None):
					sleeps.append(make(first, sleep))

				sleep = [0] * len(keys)
				first = start

			for i, k in enumerate(keys):
				sleep[i] += getattr(s, k)

			end = start + timedelta(seconds = s.runtime)

		# also add last one
		sleeps.append(make(first, sleep))

		return sleeps
