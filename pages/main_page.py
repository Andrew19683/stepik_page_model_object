from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket_link.click()

    def should_be_empty_basket_on_header(self):
        # сделал эту проверку, т.к. не понял задание, но её можно использовать
        basket = self.browser.find_element(*MainPageLocators.BASKET_HEADER)
        assert "0,00 £" in basket.text, "Basket is not empty, but should be"

    def should_be_empty_basket(self):
        basket_text = self.browser.find_element(*MainPageLocators.BASKET_EMPTY_TEXT)
        assert "Ваша корзина пуста" in basket_text.text, "Basket is not empty, but should be"