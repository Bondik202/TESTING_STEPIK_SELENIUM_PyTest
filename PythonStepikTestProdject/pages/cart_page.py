import allure
from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base
from logs.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    cart_link = '/html/body/div[1]/div/div[3]/div[1]/a'
    arrange = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/a[1]'

    """Методы запросы"""

    def get_cart_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_link)))

    def get_arrange(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrange)))  # получение локатора секция


    """Методы действия"""

    def click_cart_link(self):
        self.get_cart_link().click()
        print('Клик по корзине')

    def click_arrange(self):
        self.get_arrange().click()
        print('Клик покнопке, оформить заказ')

    """Метод бизнес логика"""

    def cart_finish(self):
        with allure.step('cart_finish'):
            Logger.add_start_step(method='cart_finish')
            self.get_current_url()
            self.click_cart_link()
            self.driver.execute_script('window.scrollTo(0, 2000)')
            self.click_arrange()
            Logger.add_end_step(url=self.driver.current_url, method='cart_finish')