from src.pom.cart_page import CartPage 
from src.pom.inventory_page import InventoryPage 
from src.pom.login_page import LoginPage
from src.tests.base_test_case import BaseTestCase
from src.tests.mixins.inventory import InventoryPageMixin 
from src.tests.mixins.login_form import LoginPageMixin
from src.tests.mixins.checkout import CheckoutPageMixin
import pdb


class CartPageTestCase(BaseTestCase, InventoryPageMixin, LoginPageMixin, CheckoutPageMixin ):

    def test_process_checkout(self):
        login_page_pom = LoginPage(self.web_driver)
        login_page_pom.fill_login_form(self.get_login_form_data())
        login_page_pom.click_login()
        inventory_page_pom = InventoryPage(self.web_driver)
        item = self.ITEMS[0]
        inventory_page_pom.add_cart(item['name'])
        cart_page_pom = CartPage(self.web_driver)
        cart_page_pom.confirm_checkout()
        cart_page_pom.send_checkout(self.get_checkout_data())
        parcial_total_text= cart_page_pom.get_parcial_total()
        tax_text= cart_page_pom.get_tax()
        total_text = cart_page_pom.get_total()
        tax = round(item["price"]*0.08,2)
        price = tax+item["price"]
        assert_parcial_total_text = "Item total: $"+str(item['price'])
        assert_tax = f'Tax: ${tax:.2f}'
        assert_total = f'Total: ${price:.2f}'
        self.assertEqual(assert_parcial_total_text, parcial_total_text)
        self.assertEqual(assert_tax, tax_text)
        self.assertEqual(assert_total, total_text)
        pdb.set_trace()
        cart_page_pom.finish_checkout()
        finish_title_text = cart_page_pom.get_checkout_complete_title()
        finish_subtitle_text = cart_page_pom.get_checkout_complete_subtitle()
        self.assertEqual("THANK YOU FOR YOUR ORDER", finish_title_text)
        self.assertEqual("Your order has been dispatched, and will arrive just as fast as the pony can get there!", finish_subtitle_text)


        
        