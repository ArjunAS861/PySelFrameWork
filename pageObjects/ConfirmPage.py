from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class ConfirmPage:

    countryOption = (By.XPATH, "//input[@id='country']")

    agreeOption = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseOption = (By.XPATH, "//input[@value='Purchase']")

    msg = (By.XPATH, "//div[contains(@class, 'alert')]")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def getCountryOption(self):
        return self.driver.find_element(*ConfirmPage.countryOption)



    def getAgreeOption(self):
        return self.driver.find_element(*ConfirmPage.agreeOption)

    def getPurchaseOption(self):
        return self.driver.find_element(*ConfirmPage.purchaseOption)

    def getMsg(self):
        return self.driver.find_element(*ConfirmPage.msg)


    def getIndiaOption(self):
        return ConfirmPage.indiaOption
    indiaOption = (By.LINK_TEXT, "India")