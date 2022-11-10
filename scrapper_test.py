import unittest
from unittest import TestCase
from scrapper import Scraper
from unittest.mock import Mock, patch
import settings


class TestScrapper(TestCase):
    def setUp(self):
        self.obj_scraper = Scraper()
        return super().setUp()

    @patch('selenium.webdriver.remote.webdriver.WebDriver.find_element')
    def test_accept_cookies(self,
        mock_find_element:Mock):
        self.obj_scraper.accept_cookies()
        mock_find_element.assert_called_once_with(by='xpath', value= settings.COOKIES_URL)
      
    @patch('selenium.webdriver.remote.webdriver.WebDriver.find_elements')
    def test_get_ftse250_table(self, 
        mock_find_element:Mock):
        self.obj_scraper.accept_cookies()
        self.obj_scraper.get_ftse250_table()
        mock_find_element.assert_called_with(by='xpath', value= settings.TABLE_ROW_PATH)

    def test_get_comp_name(self):
        self.obj_scraper.get_comp_name()
        assert isinstance(self.obj_scraper.get_comp_name(), (list, tuple)) 

    def test_page_crawler(self):
        self.obj_scraper.page_crawler()
        assert isinstance(self.obj_scraper.page_crawler(), (list, tuple)) 

    def tearDown(self):
        del self.obj_scraper
        
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=True)
