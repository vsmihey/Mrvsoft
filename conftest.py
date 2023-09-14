import time
from datetime import datetime
from urllib import request
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType


# from pages.data_login_password import *

# scope='session'
# @pytest.fixture(scope='function') @pytest.fixture(scope='session')

@pytest.fixture(scope='session')
def driver():
    # driver_service = Service(ChromeDriverManager().install())  # включить для загрузки новой версии дров
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # запуск в скрытом режиме (без браузера)
    # chrome_options.headless = True
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
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
    # chrome_options.add_argument("--lang=ru")
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # chrome_options.add_argument('--allow-insecure-localhost')
    # chrome_options.add_argument('--allow-running-insecure-content')
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled') # отключения режима автоматизации ПО
    # chrome_options.add_argument = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    driver = webdriver.Chrome(
        options=chrome_options)  # добавить service=driver_service для загрузки новых дров браузера
    driver.maximize_window()
    # driver.implicitly_wait(1)
    # driver.get(url)
    # # chrome_options.add_experimental_option("detach", True)
    # driver.minimize_window() # свернуть браузер
    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # driver.maximize_window()
    yield driver

    # """allure - прикрепление скриншота в отчете"""
    # attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


# Добавляем хук pytest_exception_interact, который вызывается при возникновении ошибки в тесте
def pytest_exception_interact(node, call, report):
    if report.failed:
        # Получаем доступ к драйверу (предполагая, что используется фикстура 'driver')
        driver = node.funcargs['driver']
        time.sleep(1)
        # Создаем скриншот и прикрепляем его к отчету Allure
        allure.attach(
            driver.get_screenshot_as_png(),
            # name="screenshot",
            name=f"Screenshot {datetime.today()}",
            attachment_type=AttachmentType.PNG
        )


def pytest_configure(config):
    """Функция по созданию пользовательских меток,
    формат записи: прописывается над нужным тестом @pytest.mark.smoke,
    где smoke имя пользовательской метки"""
    config.addinivalue_line(
        # сюда добавляем метки:
        # пример: "markers", "имя_метки: описание метки"
        "markers", "smoke: метка для смок тестов"


    )