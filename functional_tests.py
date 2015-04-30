from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome('/Users/zeulb/Dropbox/Programming/TDDPython/chromedriver')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):		

		# Budi has created a cool to-do app
		# Budi invite anduk to visit it.
		self.browser.get('http://localhost:8000')

		# Anduk notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# He is invited to enter a to-do item straight away

		# He types "Buy anduk" into a text box

		# When he hits enter, the page updates, and now the page lists
		#  "1: Buy anduk" as an item in a to do list

		# There is stil a text box inviting her to add another item. She
		# enter "Sell anduk"

		# The page updates again, now shows both items in her to do list

		# Anduk refreshes that url - his to do list is still there.

		# Satisfied, she goes back to sleep


if __name__ == '__main__':
	unittest.main(warnings='ignore')
