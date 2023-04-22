import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    # driver_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # запуск в скрытом режиме (без браузера)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    prefs = {"profile.default_content_setting_values.notifications": 1}  # принять уведомление всплывающее
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--window-size=1920,1080")  # в скрытом режиме запускать в полный размер
    chrome_options.add_argument('--enable-javascript')

    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--allow-running-insecure-content')
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # # chrome_options.add_experimental_option("detach", True)
    # driver.minimize_window() # свернуть браузер

    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # driver.maximize_window()
    yield driver
    driver.quit()
