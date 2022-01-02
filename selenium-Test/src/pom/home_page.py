from typing import Optional
from src.test_utils.driver_wrapper import DriverWrapper
from src.utils.enums.urls import PagesUrls
from src.test_utils.locator import xpath


class HomePage:
    TITLE = xpath('//span[.="A DIVERSE PORTFOLIO OF SOFTWARE ENGINEERING EXPERTISE"]')
    SKILL_AND_TECHNOLOGIES_LINK = xpath('//span[.="SKILLS AND TECHNOLOGIES"]/..')

    def __init__(self, driver):
        self.driver = DriverWrapper(driver)
        self.driver.visit_page(PagesUrls.HOME_PAGE_URL)

    def get_title(self) -> Optional[str]:
        title = self.driver.get_element_text(self.TITLE)
        return title

    def click_skill_link(self):
        self.driver.click(self.SKILL_AND_TECHNOLOGIES_LINK)
