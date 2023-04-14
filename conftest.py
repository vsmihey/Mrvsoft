import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # prefs = {"profile.default_content_setting_values.notifications": 1}
    # chrome_options.add_experimental_option("prefs", prefs)
    # # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # driver.maximize_window()
    yield driver
    driver.quit()
