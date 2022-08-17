from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from Utilities import configreader
import logging
from Utilities.logger import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, section, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configreader.read_config(section, locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configreader.read_config(section, locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configreader.read_config(section, locator)).click()
        log.logger.info("Click " + locator)

    def key(self, section, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configreader.read_config(section, locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configreader.read_config(section, locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configreader.read_config(section, locator)).send_keys(value)
        log.logger.info("send keys to " + locator + " with " + value)

    def select(self, section, locator, value):
        select_item = WebElement

        if str(locator).endswith("_XPATH"):
            select_item = self.driver.find_element(By.XPATH, configreader.read_config(section,locator))
        elif str(locator).endswith("_ID"):
            select_item = self.driver.find_element(By.ID, configreader.read_config(section, locator))
        elif str(locator).endswith("_NAME"):
            select_item = self.driver.find_element(By.NAME, configreader.read_config(section, locator))

        select = Select(select_item)
        select.select_by_visible_text(value)
        log.logger.info("Select a dropdown box " + locator + " with " + value)

    def move(self, section, locator):
        item = WebElement

        if str(locator).endswith("_XPATH"):
            item = self.driver.find_element(By.XPATH, configreader.read_config(section,locator))
        elif str(locator).endswith("_ID"):
            item = self.driver.find_element(By.ID, configreader.read_config(section, locator))
        elif str(locator).endswith("_NAME"):
            item = self.driver.find_element(By.NAME, configreader.read_config(section, locator))

        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()

        log.logger.info("Action - Move to " + locator)