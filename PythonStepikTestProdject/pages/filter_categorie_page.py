import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base
from logs.logger import Logger


class FilterPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)

    """Xpath"""

    price_min = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[2]/div[3]/span[2]/span[6]'
    price_max = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[2]/div[3]/span[2]/span[7]'
    chek_box = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[4]/div[3]/div/div[1]/label/span[1]/a'
    long_min = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[5]/div[3]/span/span[6]'
    long_max = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[5]/div[3]/span/span[7]'
    weight_min = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[6]/div[3]/span/span[6]'
    weight_max = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[6]/div[3]/span/span[7]'
    show_result = '/html/body/div[2]/div/div/div[2]/aside/div/div/div/form/div[8]/input'

    """Методы запросы"""

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_chek_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chek_box)))

    def get_long_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.long_min)))

    def get_long_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chek_box)))

    def get_weight_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.weight_min)))

    def get_weight_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.weight_max)))

    def get_show_result(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_result)))

    """Методы действия"""

    def input_price_min(self, action):
        action.click_and_hold(self.get_price_min()).move_by_offset(20, 0).release().perform()  # клик и удерживание ползунка
        print('Минемальная ценна введена')

    def input_price_max(self, action):
        action.click_and_hold(self.get_price_max()).move_by_offset(-20, 0).release().perform()  # клик и удерживание ползунка
        print('Максимальная ценна введена')

    def clic_chek_box(self):
        self.get_chek_box().click()
        print('Кликаем по чекбоксу')

    def input_long_min(self, action):
        action.click_and_hold(self.get_long_min()).move_by_offset(30, 0).release().perform()  # клик и удерживание ползунка
        print('Минемальная длинна введена')

    def input_long_max(self, action):
        action.click_and_hold(self.get_long_max()).move_by_offset(-40, 0).release().perform()  # клик и удерживание ползунка
        print('Максимальная длинна введена')

    def input_weight_min(self, action):
        action.click_and_hold(self.get_weight_min()).move_by_offset(20, 0).release().perform()  # клик и удерживание
        # ползунка
        print('Минемальный диаметр введен')

    def input_weight_max(self, action):
        action.click_and_hold(self.get_weight_max()).move_by_offset(-30, 0).release().perform()  # клик и удерживание
        # ползунка
        print('Максимальный диаметр введен')

    def clic_show_result(self):
        self.get_show_result().click()
        print('Кликаем по кнопке, показать результат')

    """Метод бизнес логика"""

    def result(self):
        with allure.step('result'):
            Logger.add_start_step(method='result')
            self.get_current_url()
            self.clic_chek_box()
            self.input_price_min(self.action)
            self.input_price_max(self.action)
            self.driver.execute_script('window.scrollTo(0, 500)')  # Скролим экран вниз
            self.input_long_min(self.action)
            self.input_long_max(self.action)
            self.input_weight_min(self.action)
            self.input_weight_min(self.action)
            self.clic_show_result()
            self.driver.execute_script('window.scrollTo(0, 500)')  # Скролим экран вниз
            Logger.add_end_step(url=self.driver.current_url, method='result')