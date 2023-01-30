from pages.buy_product_page import BuyProductPage
from pages.cart_delivery_method_page import DeliveryMethod
from pages.cart_order_confirmation_page import OrderConfirmation
from pages.cart_page import CartPage
from pages.cart_payment_method_page import PaymentMethod
from pages.filter_categorie_page import FilterPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
import time
from selenium import webdriver
from pages.main_filter_page import MenuBurgerPage
from pages.person_page import PersonPage


def test_select_product1(set_up, set_group):
    driver = webdriver.Firefox(executable_path='/driwer/geckodriver.exe')

    print('Начало теста 1')

    login = LoginPage(driver)
    login.avtorizations()

    main_filter = MenuBurgerPage(driver)
    main_filter.select_filter()

    filter_categorie = FilterPage(driver)
    filter_categorie.result()

    buy_product = BuyProductPage(driver)
    buy_product.buy_product()

    cart = CartPage(driver)
    cart.cart_finish()

    cart_person = PersonPage(driver)
    cart_person.cart_person()

    cart_delivery_method = DeliveryMethod(driver)
    cart_delivery_method.cart_finish_delivery()

    cart_payment_method = PaymentMethod(driver)
    cart_payment_method.cart_finish_payment()

    cart_order_confirmation = OrderConfirmation(driver)
    cart_order_confirmation.cart_order_confirmation()

    screen = FinishPage(driver)
    screen.finish()

    time.sleep(5)
    driver.close()
    print("Тест 1 закончен")
