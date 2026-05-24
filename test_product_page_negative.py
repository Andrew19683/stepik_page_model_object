from .pages.product_page import ProductPageLocators
from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.xfail(reason="Success message is presented, but should not be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is presented, but should not be"

@pytest.mark.xfail(reason="Success message is disappeared, but should not be")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_PROMOCODE_MESSAGE), "Success message is not disappeared, but should be"
