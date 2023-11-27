import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a Selenium WebDriver for Google
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")

    def tearDown(self):
        # Close the browser after each test case
        self.driver.quit()

    def test_search_for_virus(self):
        # Test searching for "virus" on Google
        search_input = self.driver.find_element("name", "q")
        search_input.send_keys("DC WRLD")
        search_input.send_keys(Keys.RETURN)

        # Add a sleep to wait for the results to load
        time.sleep(2)

        # Assert that search results are displayed
        self.assertTrue(self.driver.find_element("id", "search"))

class YouTubeTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a Selenium WebDriver for YouTube
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com")

    def tearDown(self):
        # Close the browser after each test case
        self.driver.quit()

    def test_open_youtube_and_close(self):
        # No need to interact with YouTube, just sleep for a short time and close the browser
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
