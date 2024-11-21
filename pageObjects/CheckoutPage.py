from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    product = (By.XPATH, "//app-card")
    partialProductTitle = (By.XPATH, ".//h4/a")
    partialProductCheckout = (By.XPATH, ".//button")

    checkoutOption = (By.XPATH, "//a[contains(text(), 'Checkout')]")
    confirmCheckout = (By.XPATH, "//button[normalize-space()='Checkout']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.product)

    def getProductTitle(self, product: WebElement):
        return product.find_element(*CheckoutPage.partialProductTitle)

    def getProductCheckout(self, product: WebElement):
        return product.find_element(*CheckoutPage.partialProductCheckout)

    def getCheckoutOption(self):
        return self.driver.find_element(*CheckoutPage.checkoutOption)

    def getConfirmCheckout(self):
        self.driver.find_element(*CheckoutPage.confirmCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage




