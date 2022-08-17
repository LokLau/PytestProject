import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.basePage import BasePage
from Pages.newCarPage import NewCarPage
from Utilities import configreader

class CarHomePage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def go_to_car(self):
        self.move("carsales locator","new_cars_XPATH")

    def go_to_new_car(self):

        locator= configreader.read_config("carsales locator", "find_new_car_XPATH")
        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((By.XPATH, locator)))
        time.sleep(3)
        self.click("carsales locator", "find_new_car_XPATH")
        return NewCarPage(self.driver)



