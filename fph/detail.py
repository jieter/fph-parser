# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from collections import namedtuple
from struct import calcsize, unpack

from FPHFile import FPHFile

class DetailFile(FPHFile):

	INDEX_SIZE = 0x800

	INDEX_RECORD_SIZE = 7
	INDEX_RECORD = (
		('timestamp', '4s'),
		('index', 'H'),
		('count', 'B')
	)

	DETAIL_RECORD_SIZE = 5
	DETAIL_RECORD = (
		('pressure', 'B'),
		('totalLeak', 'B'),
		('apneaDuration', 'B'),
		('hypoapneaDuration', 'B'),
		('flowLimitiationDuration', 'B')
	)

	DetailRecord = namedtuple('DetailRecord',
		['timestamp'] +	[x[0] for x in DETAIL_RECORD]
	)

	# create a pointer from an index pointer.
	def _detailPointer(self, index):
		return (
			self.HEADER_SIZE +
			self.INDEX_SIZE +
			(index * self.DETAIL_RECORD_SIZE)
		)

	def _parseBody(self):
		f = self.raw

		index_format = '<' + ''.join([x[1] for x in self.INDEX_RECORD])

		transforms = {
			'pressure': lambda x: x * 10
		}

		index_item = 0
		while (True):
			f.seek(self.HEADER_SIZE + (index_item * self.INDEX_RECORD_SIZE))
			index_item += 1

			item = f.read(self.INDEX_RECORD_SIZE)

			if item[0:2] == '\xFF\xFF':
				break

			(timestamp, index, count) = unpack(index_format, item)
			timestamp = self._parseTimestamp(timestamp)

			for i in range(count):
				# move file pointer to right spot.
				f.seek(self._detailPointer(index + i))

				values = self._parseRecord(
					self.DETAIL_RECORD,
					f.read(self.DETAIL_RECORD_SIZE),
					transforms
				)
				self.records.append(self.DetailRecord._make([timestamp] + values))





