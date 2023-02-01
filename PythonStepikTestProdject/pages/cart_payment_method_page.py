import allure
from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base
from logs.logger import Logger


class PaymentMethod(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    next = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[2]/button'
    option1 = '/html/body/div[2]/div/div/div[2]/div/div/section/form/table/tbody/tr[2]/td[2]/label/input'
    option2 = '/html/body/div[2]/div/div/div[2]/div/div/section/form/table/tbody/tr[4]/td[2]/label/input'

    """Методы запросы"""

    def get_next_payment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.next)))

    def get_next_option1(self):
        return self.driver.find_element(By.XPATH, self.option1)

    def get_next_option2(self):
        return self.driver.find_element(By.XPATH, self.option2)
    """Методы действия"""

    def click_next_payment(self):
        self.get_next_payment().click()
        print('Клик по кнопке, продолжить')

    def click_next_option(self):
        try:
            self.get_next_option1().click()
            print('Клик по кнопке, оплатить с помощью карты при получении')
        except:
            self.get_next_option2().click()
            print('Клик по кнопке, онлайн-оплата на сайте.')

    """Метод бизнес логика"""

    def cart_finish_payment(self):
        with allure.step('cart_finish_payment'):
            Logger.add_start_step(method='cart_finish_payment')
            self.get_current_url()
            self.driver.execute_script('window.scrollTo(0, 650)')
            self.click_next_option()
            self.click_next_payment()
            Logger.add_end_step(url=self.driver.current_url, method='cart_finish_payment')