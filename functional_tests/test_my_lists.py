from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore

from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session

class MyListsTest(FunctionalTest):

	def create_pre_authenticated_session(self, email):
		if self.against_staging:
			session_key = create_session_on_server(self.server_host, email)
		else:
			session_key = create_pre_authenticated_session(email)
		## to set a cookie we need to first visit the domain.
		## 404 pages load the quickest!
		self.browser.get(self.server_url + "/404_no_such_url/")
		self.browser.add_cookie(dict(
			name=settings.SESSION_COOKIE_NAME,
			value=session_key,
			path='/',
		))

	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		email = 'edith@example.com'

		self.browser.get(self.server_url)
		self.wait_to_be_logged_out(email)
		# Edith is a logged-in user
		self.create_pre_authenticated_session(email)

		self.browser.get(self.server_url)
		self.wait_to_be_logged_in(email)

	def test_logged_in_users_are_saved_as_my_lists(self):
		# Edith is a logged-in user
		self.create_pre_authenticated_session('edith@example.com')

		# She goes to the home page and starts a list
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Reticulate splines\n')
		self.get_item_input_box().send_keys('Immanentize eschaton\n')
		first_list_url = self.browser.current_url

		# She notices a "My lists" link, for the first time.
		self.browser.find_element_by_link_text('My lists').click()

		# She sees that her list is in there, named according to its first list item
		self.browser.find_element_by_link_text('Reticulate splines').click()
		self.wait_for(
			lambda: self.assertEqual(self.browser.current_url, first_list_url)
		)

		# She decides to start another list, just to see
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Click cows\n')
		second_list_url = self.browser.current_url

		# Under "my lists", her new list appears
		self.browser.find_element_by_link_text('My lists').click()
		self.browser.find_element_by_link_text('Click cows').click()
		self.assertEqual(self.browser.current_url, second_list_url)

		# She logs out. The "My lists" option dissapears
		self.browser.find_element_by_id('id_logout').click()
		self.assertEqual(
			self.browser.find_elements_by_link_text('My lists'),
			[]
		)
