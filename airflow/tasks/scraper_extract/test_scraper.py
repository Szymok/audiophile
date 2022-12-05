from unittest.mock import NonCallableMock
import pytest
import requests
import unittest
from bs4 import BeautifulSoup


class TestScraper(unittest.TestCase):
	'''
 	Unittests to test the structure of the webpage being scraped
	'''

	def setup(self):
		headphone_url = 'https://crinacle.com/rankings/headphones'
		iem_url = 'https://crinacle.com/rankings/iems'

		self.headphone_response = requests.get(headphone_url)
		self.headphone_soup = BeautifulSoup(self.headphone_response.text,
		                                    'html.parser')

		self.iem_response = requests.get(iem_url)
		self.iem_soup = BeautifulSoup(self.iem_response.text, 'html.parser')

	def test_iem_response(self):
		'''
		Test if IEM url connection is successful
		'''
		self.assertEqual(self.iem_response.status_code, 200)

	def test_headphone_response(self):
		'''
		Test if Headphone url connection is successful
		'''
		self.assertEqual(self.headphone_response.status_code, 200)
