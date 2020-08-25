from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_listNand_retrieve_it_later(self):
		# online to-do app homepage for Jenna
		self.browser.get('http://localhost:8000')
		
		# She notices to-do it in title
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		
		# She is invited to enter a to-do item straight away
		
		# She types "Buy peacock feathers" into a text box (Jenna's hobby
		# is tying fly fishing lures)
		
		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		
		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Jenna is very methodical)
		
		# The page updates again, and now shows both items on her list
		
		# Jenna wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some 
		# explanatory text to that effect.
		
		# She visists that URL - her to-do list is still there.
		
		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
