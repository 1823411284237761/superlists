from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_duplicate_items(self):
		# Jenna goes to the home page and starts a new list
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy wellies')

		# She accidentally tries to enter a duplicate item
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)

		# She sees a helpful error message
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You've already got this in your list"
		))

	def test_cannot_add_empty_list_items(self):
		# Jenna goes to the home pafe and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys(Keys.ENTER)

		# The browser intercepts the request, and does not load the
		# list page
		self.wait_for(lambda: self.browser.find_elements_by_css_selector(
			'#id_text:invalid'
		))

		# She starts typing some text for the new item and the error disappears
		self.get_item_input_box().send_keys('Buy milk')
		self.wait_for(lambda: self.browser.find_elements_by_css_selector(
			'#id_text:valid'
		))

		# And she can submit it successfully
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')	

		# Perversely, she now decides to submit a second blank list item
		self.get_item_input_box().send_keys(Keys.ENTER)

		# Again, the browser will not comply
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for(lambda: self.browser.find_elements_by_css_selector(
			'#id_text:invalid'
		))

		# And she can correct it by filling some text in
		self.get_item_input_box().send_keys('Make tea')
		self.wait_for(lambda: self.browser.find_elements_by_css_selector(
			'#id_text:valid'
		))
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')
