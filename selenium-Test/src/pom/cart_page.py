from typing import Optional
from src.test_utils.driver_wrapper import DriverWrapper
from src.utils.enums.urls import PagesUrls
from src.test_utils.locator import xpath


class CartPage:
    CHECKOUT_BUTTON = xpath('//button[@id="checkout"]')
    CHECKOUT1_FORM_FIRST_NAME = xpath('//input[@id="first-name"]')
    CHECKOUT1_FORM_LAST_NAME = xpath('//input[@id="last-name"]')
    CHECKOUT1_FORM_POSTAL_CODE = xpath('//input[@id="postal-code"]')
    CHECKOUT1_CONTINUE_BUTTON = xpath('//input[@id="continue"]')
    CHECKOUT2_FINISH = xpath('//button[@id="finish"]')
    CHECKOUT2_PARCIAL_TOTAL = xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
    CHECKOUT2_TAX = xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    CHECKOUT2_TOTAL = xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
    CHECKOUT3_MSG_TITLE_COMPLETE = xpath('//*[@id="checkout_complete_container"]/h2')
    CHECKOUT3_MSG_SUBTITLE_COMPLETE = xpath('//*[@id="checkout_complete_container"]/div')


    def __init__(self, driver):
        self.driver = DriverWrapper(driver)
        self.driver.visit_page(PagesUrls.CART_PAGE_URL)
    
    def send_checkout(self,data):
        self.driver.write(self.CHECKOUT1_FORM_FIRST_NAME, data['first-name'])
        self.driver.write(self.CHECKOUT1_FORM_LAST_NAME, data['last-name'])
        self.driver.write(self.CHECKOUT1_FORM_POSTAL_CODE, data['postal-code'])
        self.driver.click(self.CHECKOUT1_CONTINUE_BUTTON)
    

    def confirm_checkout(self):
        self.driver.click(self.CHECKOUT_BUTTON)

    def get_parcial_total(self):
        text_parcial_total = self.driver.get_element_text(self.CHECKOUT2_PARCIAL_TOTAL)
        return text_parcial_total

    def get_total(self):
        text_total = self.driver.get_element_text(self.CHECKOUT2_TOTAL)
        return text_total

    def get_tax(self):
        text_tax = self.driver.get_element_text(self.CHECKOUT2_TAX)
        return text_tax  

    def get_checkout_complete_title(self):
        text_complete_title = self.driver.get_element_text(self.CHECKOUT3_MSG_TITLE_COMPLETE)
        return text_complete_title  

    def get_checkout_complete_subtitle(self):
        text_complete_subtitle = self.driver.get_element_text(self.CHECKOUT3_MSG_SUBTITLE_COMPLETE)
        return text_complete_subtitle 

    def finish_checkout(self):
        self.driver.wait_element(self.CHECKOUT2_FINISH)
        self.driver.click(self.CHECKOUT2_FINISH)


