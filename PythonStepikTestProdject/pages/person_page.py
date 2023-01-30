from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base


class PersonPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    next = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[7]/button'

    """Методы запросы"""

    def get_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next)))

    """Методы действия"""

    def click_next(self):
        self.get_next().click()
        print('Клик по кнопке, продолжить')

    """Метод бизнес логика"""

    def cart_person(self):
        self.get_current_url()
        self.driver.execute_script("scrollBy(0, -300);")
        self.click_next()

