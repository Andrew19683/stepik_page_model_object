from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.product_page import ProductPageLocators
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.positive
def test_guest_can_add_product_to_basket_promo_new_year(browser):
    page = ProductPage(browser, link)
    page.open()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(item_name, item_price)
    
@pytest.mark.positive
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrized
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(item_name, item_price)

@pytest.mark.negative
@pytest.mark.xfail(reason="Success message is presented, but should not be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is presented, but should not be"

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is presented, but should not be"

@pytest.mark.negative
@pytest.mark.xfail(reason="Success message is disappeared, but should not be")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is not disappeared, but should be"

def test_guest_cant_see_product_in_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()