import pytest
from selenium import webdriver

from testData.HomePageData import HomePageData

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    url = "https://rahulshettyacademy.com/angularpractice/"
    browserName = request.config.getoption("browser")
    if browserName == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Edge()
    driver.implicitly_wait(4)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(params=HomePageData.data)
def data_provider(request):
    return request.param

