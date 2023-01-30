import datetime


class Base:
    """базовый метод"""

    def __init__(self, driver):
        self.driver = driver

    """метод для получения URL и его вывода"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Фактический URL {get_url}')

    """метод для скпиншота"""

    def screenshot(self):
        now_data = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screen = 'screenshot' + now_data + '.png'
        self.driver.save_screenshot('C:\\Users\\A_V_B\\PycharmProjects\\PythonStepikTestProdject\\screen\\' + name_screen)
        print('Скриншот сделан')
