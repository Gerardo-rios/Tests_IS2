from typing import Optional
from src.test_utils.driver_wrapper import DriverWrapper
from src.utils.enums.urls import PagesUrls
from src.test_utils.locator import xpath


class LoginPage:
    USERNAME = xpath("//input[@id=\'user-name\']")
    PASSWORD = xpath("//input[@id=\'password\']")
    LOGIN_BUTTON = xpath("//input[@id=\'login-button\']")
    MENU_BUTTON = xpath("//button[@id=\'react-burger-menu-btn\']")
    LOGOUT_LINK = xpath("//a[@id='logout_sidebar_link']")
    ERROR_LOGIN = xpath("//div[@id='login_button_container']/div/form/div[3]/h3")
    
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)
        self.driver.visit_page(PagesUrls.INIT_PAGE)

    def fill_login_form(self, login_data):
        self.driver.write(self.USERNAME, login_data['username'])
        self.driver.write(self.PASSWORD, login_data['password'])

    def click_login(self):
        self.driver.click(self.LOGIN_BUTTON)
    
    def click_logout(self):
        self.driver.click(self.LOGOUT_LINK)
    
    def open_menu(self):
        self.driver.wait_element(self.MENU_BUTTON)
        self.driver.click(self.MENU_BUTTON)

    def get_logout_text(self) -> Optional[str]:
        self.driver.wait_element(self.LOGOUT_LINK)
        logout_text = self.driver.get_element_text(self.LOGOUT_LINK)
        return logout_text

    def get_error_text(self) -> Optional[str]:
        error_text = self.driver.get_element_text(self.ERROR_LOGIN)
        return error_text    
    

