import allure
from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base
from logs.logger import Logger


class MenuBurgerPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    catalog = '/html/body/div[2]/nav/div/ul/li[2]/a'  # локатор Каталога
    section = '/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/a'  # локатор секции Зимняя рыбалка
    category = '/html/body/div[2]/div/div/div[2]/div/div/section/div[4]/div[1]/div[2]/a'  # локатор категории Зимние удочки и хлыстики

    """Методы запросы"""

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog)))  # получение локатора каталог

    def get_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.section)))  # получение локатора секция

    def get_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.category)))  # получение локатора категория

    """Методы действия"""

    def click_catalog(self):  # Клмк по выбранному элементу
        self.get_catalog().click()
        print('Клик по каталогу')

    def click_section(self):  # # Клмк по выбранному элементу
        self.get_section().click()
        print('Клик по секции')

    def click_category(self):  # # Клмк по выбранному элементу
        self.get_category().click()
        print('Клик по категории')

    """Метод бизнес логика"""

    def select_filter(self):  # управляющая конструкция
        with allure.step('select_filter'):
            Logger.add_start_step(method='select_filter')
            self.get_current_url()
            self.click_catalog()
            self.driver.execute_script('window.scrollTo(0, 500)')  # Скролим экран вниз
            self.click_section()
            self.driver.execute_script('window.scrollTo(0, 200)')  # Скролим укран вниз
            self.click_category()
            Logger.add_end_step(url=self.driver.current_url, method='select_filter')