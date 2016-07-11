import requests

# Hotel search in expedia.com

def all_hotels():

	Link = 'http://terminal2.expedia.com/x/mhotels/'

	Api_key ='HjylZS1ThqOQ4eduHDjrcO4FacL9r7Bd'

	# format: yyyy-mm-dd
	InDate = '2016-08-01'
	# format: yyyy-mm-dd
	OutDate = '2016-08-03'
	# format: UPPERCASE
	City = 'LVIV'
	"""
	Return list of all carriers (anytime, anywhere).
	Parameters:
	- city: a city for department, default - 'DNK'(Dnipro, Ukraine);
	- apy_key: your API key on the SkyScanner;
	"""
	link = '{0}search?city={1}&checkInDate={2}&checkOutDate={3}&room1=2&apikey={4}'.format(
		Link, City, InDate, OutDate, Api_key
		)

	response = requests.get(link)
	if response.status_code==200:
		data = response.json()
		print 'totalHotelCount: ', data['totalHotelCount']
		print 'availableHotelCount: ', data['availableHotelCount']
	else:
		print 'Error'
	return 


			