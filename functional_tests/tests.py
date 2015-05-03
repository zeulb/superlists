from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome('/Users/zeulb/Dropbox/Programming/TDDPython/chromedriver')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Budi has created a cool to-do app
		# Budi invite anduk to visit it.
		self.browser.get(self.live_server_url)

		# Anduk notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# He types "Buy anduk" into a text box
		inputbox.send_keys('Buy anduk')

		# When he hits enter, the page updates, and now the page lists
		#  "1: Buy anduk" as an item in a to do list
		inputbox.send_keys(Keys.ENTER)

		inputbox = self.browser.find_element_by_id('id_new_item')

		# He types "Buy bola" into a text box
		inputbox.send_keys('Buy bola')

		# When he hits enter, the page updates, and now the page lists
		#  "1: Buy anduk" as an item in a to do list
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Buy anduk')
		self.check_for_row_in_list_table('2: Buy bola')
		# There is stil a text box inviting her to add another item. She
		# enter "Sell anduk"
		self.fail('Finish the test!')

		# The page updates again, now shows both items in her to do list

		# Anduk refreshes that url - his to do list is still there.

		# Satisfied, she goes back to sleep
