import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(".//webDrivers//chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(".//webDrivers//geckodriver.exe")
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E-Commerce Altron'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Umair Khan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
