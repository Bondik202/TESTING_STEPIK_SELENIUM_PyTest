from base.base_class import Base


class OrderConfirmation(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Метод бизнес логика"""

    def cart_order_confirmation(self):
        self.get_current_url()
        self.driver.execute_script('window.scrollTo(0, 1500)')
