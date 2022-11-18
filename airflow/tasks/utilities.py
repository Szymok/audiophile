import csv


def convert_to_csv(device_data: list, device_type: str,
                   data_level: str) -> None:
	'''
	Converts a list of dicts to a csv file 

 	Args:
		device_data: (list[dict]): List of dicts containing each device
		device_type (str): String specyfying the type of device
		data_level (str): Signifies the level of data
 	'''

	with open(f'/tmp/{device_type}--{data_level}.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=device_data[0].keys())
		writer.writeheader()
		writer.writerows(device_data)
