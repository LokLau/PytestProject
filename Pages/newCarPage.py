import time

from Pages.basePage import BasePage


class NewCarPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def click_new_car_brand(self, section, locator):
        self.click(section, locator)
        time.sleep(3)

