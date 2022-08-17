import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from Utilities import configreader

import os

os.environ['GH_TOKEN'] = "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"


@pytest.fixture(params=["chrome", "edge"], scope="function")
def driver_setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    if request.param == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    driver.get(configreader.read_config("basic info", "test_url"))
    driver.maximize_window()
    driver.implicitly_wait(3)

    request.cls.driver = driver

    yield
    driver.quit()
