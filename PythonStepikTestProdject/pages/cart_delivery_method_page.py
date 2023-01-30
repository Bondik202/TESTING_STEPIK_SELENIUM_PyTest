from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base


class DeliveryMethod(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    next = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[2]/button'


    """Методы запросы"""

    def get_next_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.next)))

    """Методы действия"""

    def click_next_delivery(self):
        self.get_next_delivery().click()
        print('Клик по кнопке, продолжить')

    """Метод бизнес логика"""

    def cart_finish_delivery(self):
        self.get_current_url()
        self.driver.execute_script('window.scrollTo(0, 2000)')
        self.click_next_delivery()
