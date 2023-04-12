import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


# no close browser
chrome_options = Options()
# chrome_options.add_argument("--headless") # запуск в скрытом режиме
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
# browser.set_page_load_timeout()
url = "https://test2.minervasoft.ru/login?from=%2F"
driver.get(url)
driver.maximize_window()


type_of = driver.find_element(By.CSS_SELECTOR, ".m-ui-paper.m-ui-select__paper")
type_of.click()
type_of_change = driver.find_element(By.XPATH, "//option[@type='EMBEDDED']")
type_of_change.click()
username = 'm.andrey'
password = 'fc1c2adc'

def test_enter_correct():

    """ correct login and correct password"""
    login = driver.find_element(By.NAME, "username")
    # time.sleep(1)
    login.send_keys(username)
    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys(password)
    input_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    input_button.click()

    # check
    # description = driver.find_element(By.XPATH, "//h1[text()='Выберите проект']")
    # description_value = description.text
    # assert description_value == 'Выберите проект'
    print('enter')

# driver.quit()


