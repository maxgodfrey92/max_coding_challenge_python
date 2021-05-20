import config
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def start_driver() -> WebDriver:
    browser = config.BROWSER.lower()

    if browser == 'firefox':
        driver_path = config.FIREFOX_DRIVER_PATH
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        driver_path = config.CHROME_DRIVER_PATH
        driver = webdriver.Chrome(driver_path)

    driver.maximize_window()
    return driver
