from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def is_element_text_equal(self, how, what, expected_text):
        try:
            element = self.browser.find_element(how, what)
            return element.text == expected_text
        except (NoSuchElementException):
            return False
        
    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_link.click()

    def should_be_empty_basket_on_header(self):
        # сделал эту проверку, т.к. не понял задание, но её можно использовать
        basket = self.browser.find_element(*BasePageLocators.BASKET_HEADER)
        assert "0,00 £" in basket.text, "Basket is not empty, but should be"

    def should_be_empty_basket(self):
        basket_text = self.browser.find_element(*BasePageLocators.BASKET_EMPTY_TEXT)
        assert "Ваша корзина пуста" in basket_text.text, "Basket is not empty, but should be"