from typing import Optional
from src.test_utils.driver_wrapper import DriverWrapper
from src.utils.enums.urls import PagesUrls
from src.test_utils.locator import xpath


class InventoryPage:
    SPAN_CART = xpath('//*[@id="shopping_cart_container"]/a/span')

    def __init__(self, driver):
        self.driver = DriverWrapper(driver)
        self.driver.visit_page(PagesUrls.HOME_PAGE_URL)
    
    def add_cart(self, item):
        self.driver.click(xpath(f'//*[@id="add-to-cart-{item}"]'))

    def get_items_on_cart(self):
        self.driver.wait_element(self.SPAN_CART)
        items_cart_text = self.driver.get_element_text(self.SPAN_CART)
        return items_cart_text

