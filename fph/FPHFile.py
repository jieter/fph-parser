# Fisher and Paykel CPAP .FPH file parser.
#
# Jan Pieter Waagmeester <jieter@jieter.nl>
#
# File format source:
# http://sourceforge.net/apps/mediawiki/sleepyhead/index.php?title=Icon

from struct import calcsize, unpack
from collections import namedtuple
from datetime import datetime

class FPHFile:
	FPH_MAGIC_NUMBER = '0201'

	HEADER_SIZE = 0x200
	HEADER_SEPARATOR = '\r'
	# Header (field name, offset) tuples
	HEADER_OFFSETS = [
		('version', 1),
		('filename', 2),
		('serialnumber', 3),
		('series', 4),
		('model', 5)
	]

	END_OF_DATA = '\xFE\xFA'

	Header = namedtuple('Header', [x[0] for x in HEADER_OFFSETS])

	CSV_SEPARATOR = ';'

	records = []

	def __init__(self, filename):
		with open(filename, 'rb') as f:
			self.raw = f
			self.header = self._parseHeader(self.raw)

			self._parseBody()

	def _parseBody(self):
		pass

	def _parseHeader(self, f):
		fields = f.read(self.HEADER_SIZE).split(self.HEADER_SEPARATOR)

		if (fields[0] != self.FPH_MAGIC_NUMBER):
			raise self.FPH_MAGIC_NUMBER + " magic number not found"

		# last byte (fields[6][-1]) contains a checksum,
		#
		# TODO implement checksum
		# https://github.com/kearygriffin/sleepyhead/blob/master/SleepLib/loader_plugins/icon_loader.cpp#L658
		#
		return self.Header._make(
			[fields[offset] for name, offset in self.HEADER_OFFSETS]
		)

	def _parseTimestamp(self, raw):
		dateword, timeword = unpack('<HH', raw)

		year = 2000 + ((dateword >> 9) & 0x7f)
		month = (dateword >> 5) & 0x0f
		day = dateword & 0x1f

		hour = (timeword >> 11) & 0x1f
		minute = (timeword >> 5) & 0x3f
		second = (timeword & 0x1f) * 2

		return datetime(year, month, day, hour, minute, second)

	def _parseDuration(self, raw):
		return raw * 360

	def _parseRecord(self, format_tuple, record, transforms={}):
		offset = 0
		values = []
		for (name, format) in format_tuple:
			format = '<' + format
			size = calcsize(format)
			raw = record[offset:(offset + size)]

			if (name != '_'):
				value = unpack(format, raw)[0]
				if name in transforms:
					value = transforms[name](value)

				values.append(value)

			offset += size

		return values

	def toCSV(self):
		if (self.records):
			return records2csv(self.records)


	def __str__(self):
		ret = str(self.header) + '\n'
		ret += self.toCSV()
		return ret


def records2csv(it, separator = ';'):
	csv = ''
	if (len(it) > 0):
		csv += separator.join(it[0]._fields) + '\n'
		csv += '\n'.join([separator.join(map(str, r)) for r in it])

	return csv