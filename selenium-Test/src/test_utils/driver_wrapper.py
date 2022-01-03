from typing import Tuple
from typing import Optional

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DriverWrapper:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5000)

    def find_elements(self, locator: Tuple[str, str]):
        elements = self.driver.find_elements(*locator)
        return elements

    def find_element(self, locator: Tuple[str, str]):
        element = self.driver.find_element(*locator)
        return element

    def get_element_text(self, locator: Tuple[str, str]) -> Optional[str]:
        try:
            element = self.find_element(locator)
        except NoSuchElementException:
            return None
        return element.text

    def exists_element(self, locator: Tuple[str, str]) -> bool:
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def get_element_attribute(self, locator: Tuple[str, str], attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def open_tab(self):
        open_new_tab_command = 'window.open('');'
        self.driver.execute_script(open_new_tab_command)

    def get_current_path(self):
        get_window_path = 'return window.location.pathname'
        return self.driver.execute_script(get_window_path)

    def visit_page(self, page_link: str):
        self.driver.get(page_link)

    def close_current_page(self):
        self.driver.close()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def write(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_page_url(self):
        return self.driver.current_url

    def wait_element(self, locator):
        wait = WebDriverWait(self.driver, 50000)
        wait.until(expected_conditions.visibility_of_element_located(locator))
    
    '''
    def get_localStorage(self,item):
        return self.driver.execute_script(f"return window.localStorage[{item}];")
    '''