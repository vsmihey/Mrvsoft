import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# from pages.data_login_password import *

# scope='session'
# @pytest.fixture(scope='function') @pytest.fixture(scope='session')


@pytest.fixture(scope='session')
def driver():
    # driver_service = Service(ChromeDriverManager().install())  # вкючить для загрузки новой версии дров
    chrome_options = Options()
    chrome_options.add_argument("--headless")   # запуск в скрытом режиме (без браузера)
    # chrome_options.headless = True
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # prefs = {"profile.default_content_setting_values.notifications": 1}  # принять уведомление всплывающее
    # chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument('--allow-silent-push')
    chrome_options.add_argument('--disable-notifications')
    # chrome_options.add_argument("--lang = en")
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--incognito") # принудительный режим инкогнито
    # chrome_options.add_argument("--user-data-dir") # выключение режима инкогнито
    # chrome_options.add_argument("--window-size=1280,800")  # в скрытом режиме запускать в полный размер
    chrome_options.add_argument("--window-size=1920,1080")  # в скрытом режиме запускать в полный размер
    # chrome_options.add_argument('--enable-javascript')
    # chrome_options.add_argument("disable-infobars")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--lang=ru")
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # chrome_options.add_argument('--allow-insecure-localhost')
    # chrome_options.add_argument('--allow-running-insecure-content')
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled') # отключения режима автоматизации ПО
    # chrome_options.add_argument = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    driver = webdriver.Chrome(
        options=chrome_options)  # добавить service=driver_service для загрузки новых дров браузера
    driver.maximize_window()
    # driver.get(url)
    # # chrome_options.add_experimental_option("detach", True)
    # driver.minimize_window() # свернуть браузер
    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # driver.maximize_window()
    yield driver
    driver.quit()
