from src.pom.home_page import HomePage
from src.tests.base_test_case import BaseTestCase


class HomePageTestCase(BaseTestCase):

    def test_title_verification(self):
        home_page_pom = HomePage(self.web_driver)
        home_page_title = home_page_pom.get_title()
        print(home_page_title)
        self.assertIsNotNone(home_page_title)

    def test_links_functionality(self):
        home_page_pom = HomePage(self.web_driver)
        home_page_pom.click_skill_link()
        current_page_url = home_page_pom.driver.get_current_page_url()
        self.assertEqual(current_page_url, 'https://www.ioet.com/technologies')