import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.brandPage import CarBrandPage
from Utilities import dataProvider
from Pages.carHomePage import CarHomePage
from TestCases.BaseTest import BaseTest
import time


class Test_CarHomePage(BaseTest):

    @pytest.mark.parametrize("brand", dataProvider.data_provider("NewCars"))
    def test_navigate_to_new_car(self, brand):
        car_home_page = CarHomePage(self.driver)
        car_home_page.go_to_car()

        section = "newcar locator"
        locator = brand[0] + "_XPATH"
        car_home_page.go_to_new_car().click_new_car_brand(section, locator)


        WebDriverWait(self.driver,28).until(EC.presence_of_element_located((By.TAG_NAME,"title")))
        page_title=self.driver.title
        brand_page=CarBrandPage(self.driver)
        assert brand_page.check_title(page_title,brand[0]), "Land on the wrong page!!"

        brand_page.print_car()