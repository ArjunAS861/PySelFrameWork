from enum import CONFORM

import pytest

from pageObjects.HomePage import HomePage
from utilities.SetupClass import SetupClass
from selenium.webdriver.remote.webdriver import WebDriver


class TestOne(SetupClass):
    driver : WebDriver

    def test_e2e(self):

        print(self.driver.current_url)

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()

        wishList = ["Nokia Edge", "Blackberry"]

        productElements = checkoutPage.getProducts()

        for ele in productElements:
            print(ele.get_attribute("outerHTML"))
            title = checkoutPage.getProductTitle(ele).text
            print(title)
            if title in set(wishList):
                checkoutPage.getProductCheckout(ele).click()

        checkoutPage.getCheckoutOption().click()
        confirmPage = checkoutPage.getConfirmCheckout()

        confirmPage.getCountryOption().send_keys("Ind")

        country = self.validatePresence("India")

        print(country.get_attribute("outerHTML"))
        country.click()

        confirmPage.getAgreeOption().click()
        confirmPage.getPurchaseOption().click()

        successMsg = confirmPage.getMsg().text
        print(self.driver.title)
        assert "Thank you" in successMsg
