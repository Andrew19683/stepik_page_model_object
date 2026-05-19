from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ITEM_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    SUCCESS_PROMOCODE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(2) .alertinner strong")
    CART_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")