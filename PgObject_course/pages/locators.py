from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert")
