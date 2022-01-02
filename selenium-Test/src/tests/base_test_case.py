import unittest
from unittest import TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class BaseTestCase(TestCase):

    def setUp(self) -> None:
        chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
        self.web_driver = chrome_driver

    def tearDown(self) -> None:
        self.web_driver.close()


if __name__ == '__main__':
    unittest.main()
