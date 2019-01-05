from __future__ import print_function
import requests

CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'

class CPIData(object):
	"""Abstraction of the CPI data.
	
	This stores internally only one value per year.
	
	"""
	def __init__(self):
		self.year_cpi = {}
		self.last_year = None
		self.first_year = None
		
	def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url.

        The downloaded file can also be saved into a location for later
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.

        """
		fp = requests.get(url, stream=True, headers={'Accept-Encoding':None}).raw
		
		if save_as_file is None:
			return self.load_from_file(fp)
		
		with open(save_as_file, 'wb+') as out:
			while True:
				buffer = fp.read(81920)
				if not buffer:
					break
				out.write(buffer)
		with open(save_as_file) as fp:
			return self.load_from_file(fp)
			
	def load_from_file(self, fp):
		"""Loads CPI data from a given file-like object."""
		

	def get_adjusted_price(self, price, year, current_year=None):
		"""Returns the adapted price from a given year compared to what current
		year has been specified.

		"""

def main():
	# Grab CPI/Inflation data
	
	# Grab API/game platform data
	
	# Generate a plot/bar graph for the adjusted price data
	
	# Generate a CSV file to save for the adjusted price data