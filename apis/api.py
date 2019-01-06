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
		current_year = None
		year_cpi = []
		for line in fp:
			while not line.startswith("DATE "):
				pass
			data = line.rstrip().split()
			year = int(data[0].split("-")[0])
			cpi = float(data[1])
			if self.first_year is None:
				self.first_year = year
			self.last_year = year
			# when we reach a new year, we have to reset the CPI data
			# calculate average CPI of the current_year
			if current_year != year:
				if current_year is not None:
					self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
				year_cpi = []
				current_year = year
			year_cpi.append(cpi)
			# we have to do the calculation once again for the last year
			if current_year is not None and current_year not in self.year_cpi:
				self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
		

	def get_adjusted_price(self, price, year, current_year=None):
		"""Returns the adapted price from a given year compared to what current
		year has been specified.

		This essentially is the calculated inflation for an item.
		
		"""
		# Currently there is no CPI data for 2019
		if current_year is None or current_year > 2018:
			current_year = 2018
		# If our data range doesn't provide a CPI for the given year, use
		# the edge data.
		if year < self.first_year:
			year = self.first_year
		elif year > self.last_year:
			year = self.last_year

		year_cpi = self.year_cpi[year]
		current_cpi = self.year_cpi[current_year]

		return float(price) / year_cpi * current_cpi

		
class GiantbombAPI(object):
    """
    Very simple implementation of the Giantbomb API that only offers the
    GET /platforms/ call as a generator.

    Note that this implementation only exposes of the API what we really need.
    """

    base_url = 'http://www.giantbomb.com/api'

    def __init__(self, api_key):
        self.api_key = api_key

	def get_platforms(self, sort=None, filter=None, field_list=None):
        """Generator yielding platforms matching the given criteria. If no
        limit is specified, this will return *all* platforms.

        """

        # The API itself allows us to filter the data returned either
        # by requesting only a subset of data elements or a subset with each
        # data element (like only the name, the price and the release date).
        #
        # The following lines also do value-format conversions from what's
        # common in Python (lists, dictionaries) into what the API requires.
        # This is especially apparent with the filter-parameter where we
        # need to convert a dictionary of criteria into a comma-seperated
        # list of key:value pairs.
        params = {}
        if sort is not None:
            params['sort'] = sort
        if field_list is not None:
            params['field_list'] = ','.join(field_list)
        if filter is not None:
            params['filter'] = filter
            parsed_filters = []
            for key, value in filter.iteritems():
                parsed_filters.append('{0}:{1}'.format(key, value))
            params['filter'] = ','.join(parsed_filters)

        params['api_key'] = self.api_key
        params['format'] = 'json'

        incomplete_result = True
        num_total_results = None
        num_fetched_results = 0
        counter = 0

        while incomplete_result:
            # Giantbomb's limit for items in a result set for this API is 100
            # items. But given that there are more than 100 platforms in their
            # database we will have to fetch them in more than one call.
            #
            # Most APIs that have such limits (and most do) offer a way to
            # page through result sets using either a "page" or (as is here
            # the case) an "offset" parameter which allows you to "skip" a
            # certain number of items.
            params['offset'] = num_fetched_results
            result = requests.get(self.base_url + '/platforms/',
                                  params=params)
            result = result.json()
            if num_total_results is None:
                num_total_results = int(result['number_of_total_results'])
            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                incomplete_result = False
            for item in result['results']:
                logging.debug("Yielding platform {0} of {1}".format(
                    counter + 1,
                    num_total_results))

                # Since this is supposed to be an abstraction, we also convert
                # values here into a more useful format where appropriate.
                if 'original_price' in item and item['original_price']:
                    item['original_price'] = float(item['original_price'])

                # The "yield" keyword is what makes this a generator.
                # Implementing this method as generator has the advantage
                # that we can stop fetching of further data from the server
                # dynamically from the outside by simply stop iterating over
                # the generator.
                yield item
                counter += 1
		
def main():
	# Grab CPI/Inflation data
	
	# Grab API/game platform data
	
	# Generate a plot/bar graph for the adjusted price data
	
	# Generate a CSV file to save for the adjusted price data