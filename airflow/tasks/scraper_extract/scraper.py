import re
import csv
import pprint
import pathlib
import logging
import requests
from bs4 import BeautifulSoup

script_path = pathlib.Path(__file__).parent.resolve()

logging.basicConfig(filename='logs.log', level=logging.INFO)

with open('logs.log', 'w'):
	pass


class Scraper:
	'''
 	Encapsulates all the logic for scraper
 	'''

	def __init__(self) -> None:
		self.base_url = 'https://crinacle.com/ranking'

	def clean_headers(self, headers: list) -> list:
		'''
		Formats the table headers in snake case, code friendly format

 		Args:
	 		headers (list): Contains the unformatted dirty table headers

		Returns:
			list: Returns properly, well formatted table headers
		'''
		clean_headers = []

		for header in headers:
			# Remove unnecesary terms
			if "(" in header or "/" in header:
			header = header.split(" ")[0]

			# Rename header for conformity between both IEMS and headphones
			if "Setup" == header:
				header = "driver_type"

			# Convert to snake case
			clean.headers.append(
				re.sub(r"(?<=[a-z])(?=[A-Z])|[^a-zA-Z]", " ", header).replace(" ", "_").lower()
			)

		return clean_headers