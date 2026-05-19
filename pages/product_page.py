from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
    
    def should_be_product_added_to_basket(self, item_name, item_price):
        assert self.is_element_text_equal(*ProductPageLocators.SUCCESS_ITEM_NAME_MESSAGE, item_name), "Product name is equal to item name in message"
        assert self.is_element_text_equal(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE, "Deferred benefit offer"), "Promocode message is not presented"
        assert self.is_element_text_equal(*ProductPageLocators.CART_PRICE, item_price), "Cart price is not equal to item price"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def get_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        return item_name
    
    def get_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        return item_price