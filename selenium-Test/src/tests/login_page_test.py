from src.pom.login_page import LoginPage
from src.tests.base_test_case import BaseTestCase
from src.tests.mixins.login_form import LoginPageMixin
import pdb


class LoginPageTestCase(BaseTestCase, LoginPageMixin):

    def test_login_fail(self):
        login_page_pom = LoginPage(self.web_driver)
        loginPath = login_page_pom.driver.get_current_path()
        login_page_pom.fill_login_form(self.get_login_form_data(username="testFailed", password="failedtest"))
        self.assertEqual(loginPath, '/')
        login_page_pom.click_login()
        error_msg = login_page_pom.get_error_text()
        self.assertEqual('Epic sadface: Username and password do not match any user in this service', error_msg)

    def test_login_success(self):
        login_page_pom = LoginPage(self.web_driver)
        login_page_pom.fill_login_form(self.get_login_form_data())
        login_page_pom.click_login()
        homePath = login_page_pom.driver.get_current_path()
        self.assertEqual(homePath, '/inventory.html')
        login_page_pom.open_menu()
        logout_text = login_page_pom.get_logout_text()
        self.assertEqual(logout_text,'LOGOUT')
        login_page_pom.click_logout()
        loginPath = login_page_pom.driver.get_current_path()
        self.assertEqual(loginPath,'/')
        
        



