import allure
from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base
from logs.logger import Logger


class BuyProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    product_1 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[4]/div[4]/div[3]/a[1]'
    product_2 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[4]/div[4]/div[4]/a[1]'
    product_3 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[4]/div[4]/div[5]/a[1]'
    btn_product_1 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[1]/div[5]/a'
    btn_buy_product_1 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[3]/table/tbody/tr/td[5]/form/button'
    btn_product_2 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[1]/div[5]/a'
    btn_buy_product_2 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[5]/table/tbody/tr/td[5]/form/button'
    btn_product_3 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[1]/div[5]/a'
    btn_buy_product_3 = '/html/body/div[2]/div/div/div[2]/div/div/section/div[1]/div[3]/table/tbody/tr/td[5]/form/button'

    """Методы запросы обьектов"""

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))

    """Методы действия"""

    def clic_buy_product_1(self):
        self.get_product_1().click()
        print('Клик по продукту 1')
        self.get_current_url()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_product_1))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_buy_product_1))).click()
        print('Продукт № 1 добавлен в корзину')
        self.driver.back()

    def clic_buy_product_2(self):
        self.get_product_2().click()
        print('Клик по продукту 2')
        self.get_current_url()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_product_2))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_buy_product_2))).click()
        print('Продукт № 2 добавлен в корзину')
        self.driver.back()

    def clic_buy_product_3(self):
        self.get_product_3().click()
        print('Клик по продукту 3')
        self.get_current_url()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_product_3))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_buy_product_3))).click()
        print('Продукт № 3 добавлен в корзину')
        self.driver.back()

    """Метод бизнес логика"""

    def buy_product(self):
        with allure.step('buy_product'):
            Logger.add_start_step(method='buy_product')
            self.get_current_url()
            self.clic_buy_product_1()
            self.clic_buy_product_2()
            self.clic_buy_product_3()
            Logger.add_end_step(url=self.driver.current_url, method='buy_product')