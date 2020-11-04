from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # online to-do app homepage for Jenna
        self.browser.get(self.live_server_url)

        # She notices to-do it in title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Jenna's hobby
        # is tying fly fishing lures)
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        self.add_list_item('Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Jenna is very methodical)
        self.add_list_item('Use peacock feathers to make a fly')

        # The page updates again, and now shows both items on her list		
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Jenna starts a new to-do list
        self.browser.get(self.live_server_url)
        self.add_list_item('Buy peacock feathers')

        # She notices that her list has a unqiue URL
        jenna_list_url = self.browser.current_url
        self.assertRegex(jenna_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site
	
        ## We use a new browser session to make sure that no information
        ## of Jenna's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        ## Francis visits the home page. There is no sign of Jenna's
        ## list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Jenna...
        self.add_list_item('Buy milk')

        # Again, there is no trace of Jenna's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied they both go back to sleep
