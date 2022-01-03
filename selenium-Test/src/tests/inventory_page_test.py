from src.pom.inventory_page import InventoryPage
from src.pom.login_page import LoginPage
from src.tests.base_test_case import BaseTestCase
from src.tests.mixins.inventory import InventoryPageMixin 
from src.tests.mixins.login_form import LoginPageMixin
from src.tests.mixins.checkout import CheckoutPageMixin
import pdb


class InventoryPageTestCase(BaseTestCase, InventoryPageMixin,LoginPageMixin, CheckoutPageMixin):

    def test_add_item(self):
        login_page_pom = LoginPage(self.web_driver)
        login_page_pom.fill_login_form(self.get_login_form_data())
        login_page_pom.click_login()
        inventory_page_pom = InventoryPage(self.web_driver)
        item = self.ITEMS[0]
        inventory_page_pom.add_cart(item['name'])
        text_items_cart = inventory_page_pom.get_items_on_cart()
        self.assertEqual(text_items_cart, '1')




