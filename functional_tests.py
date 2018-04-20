#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rmachuca <rmachuca@rmachuca-desk>

"""Basic functional testing laboratory with selenium."""

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """Tests main page."""

    def setUp(self):
        """Set up test environment."""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Tear down test environment."""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test to-do list."""
        # Edith has heard about a cool new online to-do app
        # She goes to check its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention 'to-do' lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders wheter the site will remember het list.
        # Then she sees that the site has generated a unique URL for her
        # There is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
