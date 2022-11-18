import re
import pandas as pd
from typing import DictReader
from pydantic import ValidationError
from utilities import convert_to_csv
from scraper_extract.models import InEarMonitor, Headphone

def read_csv_as_dicts(filename: str) -> List[dict]:
	'''
 	Returns a list of dictionaries read from specified csv
	
 	Args:
 		filename (str): name of file to be read
	 
	Returns:
 		List[dict]
	'''
	try:
		with open(filename, 'r') as file:
			reader = DictReader(file)
			return list(reader)
	except OSError as exception:
		print(f'{filename} - {exception}'})

def sanitize_data(data: List[dict]) -> List[dict]:
	'''
 	Performs rudimentary sanitizations on bronze data
	
 	Args:
 		data (List[dict]): list of IEMs/Headphones
	 
	Returns:
 		List[dict]: Sanitized data
	'''
	df = pd.DataFrame(data)

	columns_to_drop = [
		'comments',
		'based_on',
		'note_weight',
		'pricesort',
		'techsort',
		'tonesort',
		'ranksort'
	]

	df = df.drop(columns_to_drop, axis=1)

	# Some signatures have quotes around them, unneeded
	df['signature'] = df['signature'].str.replace('"', "")

	for index, row in df.iterrows():
		# Replace doscontinued devices with no price with -1
		if re.search('Discount', str(row['price'])):
			row['price'] = -1

		# Replace ? device prices with -1
		if re.search('\\?', str(row['price'])):
			row['price'] = -1
			
		# Some prices have models embedded to them
		if re.search('[a-zA-Z]', str(row['price'])):
			row['price'] = list(filter(None, re.split(r'(\d+)', str(row['price']))))[0]
			
			# Some are still text
			if re.search('[a-zA-Z]', str(row['price'])):
				row['price'] = -1
				
    # Replace star text
		row['value_rating'] = len(row['value_rating']) if row['value_rating'] else -1

	return df.to_dict('records')

if __name__ == '__main__':
	headphone_file = '/tmp/headphones_bronze.csv'
	iems_file = '/tmp/iems-bronze.csv'
	iems_list = read_csv_as_dicts(iems_file)
	headphones_list = read_csv_as_dicts(headphones_file)

	# Sanitize both CSV files with similar parameters
	iems_list_sanitized = sanitize_data(iems_list)
	headphones_list_sanitized = sanitize_data(headphones_list)
	# Validates all headphones/iems in a list based on the validators
	# defined in the respective PyDantic models
	try:
			iems_list = [InEarMonitor.parse_obj(iem) for iem in iems_list_sanitized]
	except ValidationError as exception:
			print(f"IEM - {exception}")

	try:
			headphones_list = [
					Headphone.parse_obj(headphone) for headphone in headphones_list_sanitized
			]
	except ValidationError as exception:
			print(f"Headphone - {exception}")

	convert_to_csv(device_data=iems_list_sanitized, device_type="iems", data_level="silver")
	convert_to_csv(
			device_data=headphones_list_sanitized, device_type="headphones", data_level="silver"
	)
