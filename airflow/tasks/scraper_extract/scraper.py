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
 	'''