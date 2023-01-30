from selenium.webdriver.common.by import By  # импортирование модуля для поиска локаторов
from selenium.webdriver.support.wait import WebDriverWait  # импортирования модуля явное ожидание
from selenium.webdriver.support import \
    expected_conditions as EC  # импортирование модуля для явного ожидание и создание новой нонстанты под него(ЕС)
from base.base_class import Base


class LoginPage(Base):
    url = 'https://rybolov.org/shop/user/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Xpath"""

    enter_cabinet = '/html/body/div[1]/div/div[3]/div[3]/div[2]/a[1]'
    user_name = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[1]/label/input'
    password = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[2]/label/input'
    clic_batton = '/html/body/div[2]/div/div/div[2]/div/div/section/form/div[3]/label/button'

    """Методы запросы"""

    def get_enter_cabinet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_cabinet)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_clic_batton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clic_batton)))

    """Методы действия"""

    def clic_clic_enter_cabinet(self):
        self.get_enter_cabinet().click()
        print('Кликаем по личному кабинету')

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Пользователь введен')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Пароль введен')

    def clic_clic_batton(self):
        self.get_clic_batton().click()
        print('Клик по кнопке, войти')

    """Метод бизнес логика"""

    def avtorizations(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name('artem_test_stepik@rambler.ru')
        self.input_password('Qwer1234')
        self.clic_clic_batton()
