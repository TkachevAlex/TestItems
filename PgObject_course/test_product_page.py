import time

from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)               # инициализируем Page Object
    page.open()                                     # открываем страницу
    page.should_be_add_button()                     # проверяем наличие кнопки Добавить в корзину
    page.save_product_name_and_price()              # запоминаем имя товара и его цену
    page.click_to_add_button()                      # кликаем на кнопку Добавить в корзину
    page.solve_quiz_and_get_code()                  # вводим код для степика
    page.should_be_alerts_about_add_product()       # проверяем появление алертов об успешном добавлении в корзину
    page.check_product_name_and_price_in_basket()   # проверяем что в корзине товар с верным наименованием и ценой



