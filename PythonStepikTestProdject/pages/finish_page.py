import allure

from base.base_class import Base
from logs.logger import Logger


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def finish(self):
        with allure.step('finish'):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='finish')