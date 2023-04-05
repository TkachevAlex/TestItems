from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = None
    price = None

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def save_product_name_and_price(self):
        ProductPage.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        ProductPage.price = self.browser.find_element(*ProductPageLocators.PRICE).text

    def click_to_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_alerts_about_add_product(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), "Alert Product is not presented"
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE), "Alert Price is not presented"

    def check_product_name_and_price_in_basket(self):
        assert ProductPage.product_name in \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text, \
               "Product '{}' doesn't add".format(ProductPage.product_name)
        assert ProductPage.price in self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text, \
               "Product '{}' add with incorrect price '{}'".format(ProductPage.product_name, ProductPage.price)


