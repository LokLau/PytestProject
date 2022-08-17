import time

from selenium.webdriver.common.by import By

from Pages.basePage import BasePage
from Utilities import configreader


class CarBrandPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def check_title(self, title, brand):
        # grab page title
        return brand in title.lower()

    def print_car(self):
        car_items =  self.driver.find_elements(By.XPATH,configreader.read_config("brand locator","car_title_group_XPATH"))

        for car in car_items:
            print (car.text)