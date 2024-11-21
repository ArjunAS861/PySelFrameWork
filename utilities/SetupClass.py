import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class SetupClass:
    driver: WebDriver
    def validatePresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        return element