from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.XPATH,"//a[normalize-space()='Shop']")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage