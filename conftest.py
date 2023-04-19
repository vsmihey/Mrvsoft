import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    # driver_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # chrome_options.add_argument("--headless")   # запуск в скрытом режиме (без браузера)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    prefs = {"profile.default_content_setting_values.notifications": 1}  # принять уведомление всплывающее
    chrome_options.add_experimental_option("prefs", prefs)
    # # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver.minimize_window() # свернуть браузер

    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # driver.maximize_window()
    yield driver
    driver.quit()
