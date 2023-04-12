import datetime
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

# driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
# download webdriver
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# no close browser

chrome_options = Options()
chrome_options.add_argument("--headless")  # запуск в скрытом режиме
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
# browser.set_page_load_timeout()
url = "https://test2.minervasoft.ru/login?from=%2F"
driver.get(url)
driver.maximize_window()
# screenshot
def screenshoot():
    offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
    now_date = datetime.datetime.now(offset)
    now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
    # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
    name_screenshot = 'screenshot.png' + now_date + '.png'
    driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\Minervasoft\\screen\\' + name_screenshot)

# correct
username = 'm.andrey'
password = '980417f5'
# incorrect
inc_username = 'm.andre'
inc_password = '980417f'

def type_of_auth():
    """type_of_authorization"""
    type_of = driver.find_element(By.CSS_SELECTOR, ".m-ui-paper.m-ui-select__paper")
    type_of.click()
    type_of_change = driver.find_element(By.XPATH, "//option[@type='EMBEDDED']")
    type_of_change.click()
    print("type of authorization changed")


def test_restore():
    """incorrect login"""
    type_of_auth()
    login = driver.find_element(By.NAME, "username")
    login.send_keys(username)
    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys(inc_password)
    input_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    input_button.click()

    restore_access = driver.find_element(By.CSS_SELECTOR, ".m-ui-typography.m-ui-typography--bold.m-ui-typography--14x14")
    restore_access.click()
    login = driver.find_element(By.NAME, "username")
    login.send_keys(inc_username)
    restore_access_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    restore_access_button.click()
    incorrect_login = driver.find_element(By.XPATH, "//div[@class='m-ui-typography m-ui-typography--14x14']")
    incorrect_login_value = incorrect_login.text
    assert incorrect_login_value == 'Неверный логин'
    print('restore incorrect login PASSED')

    """correct login"""
    login = driver.find_element(By.NAME, "username")
    login.send_keys(username)
    restore_access_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    restore_access_button.click()
    time.sleep(1)
    restore_access_button.click()
    time.sleep(1)
    screenshoot()
    print('restore correct login PASSED')

    remember = driver.find_element(By.XPATH, "//span[text()='я помню пароль']")
    remember.click()
    # check input page
    input_page = driver.find_element(By.XPATH, "//h1[text()='Вход в систему']")
    input_page_value = input_page.text
    assert input_page_value == 'Вход в систему'
    print('input page opened PASSED')
