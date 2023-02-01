import allure

from base.base_class import Base
from logs.logger import Logger


class OrderConfirmation(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Метод бизнес логика"""

    def cart_order_confirmation(self):
        with allure.step('cart_order_confirmation'):
            Logger.add_start_step(method='cart_order_confirmation')
            self.get_current_url()
            self.driver.execute_script('window.scrollTo(0, 1500)')
            Logger.add_end_step(url=self.driver.current_url, method='cart_order_confirmation')