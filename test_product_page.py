from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(item_name, item_price)
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()