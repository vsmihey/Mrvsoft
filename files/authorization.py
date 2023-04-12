import datetime
import time
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
# chrome_options.add_argument("--headless")  # запуск в скрытом режиме
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

# scroll page
# driver.execute_script("window.scrollTo(0, 1080)")

'''authorization'''
# type of authorization
type_of = driver.find_element(By.CSS_SELECTOR, ".m-ui-paper.m-ui-select__paper")
type_of.click()
type_of_change = driver.find_element(By.XPATH, "//option[@type='EMBEDDED']")
type_of_change.click()
# correct
username = 'm.andrey'
password = '980417f5'
# incorrect
inc_username = 'm.andre'
inc_password = '980417f'


'''incorrect login and correct password'''
login = driver.find_element(By.NAME, "username")
# time.sleep(1)
login.send_keys(inc_username)
passwd = driver.find_element(By.NAME, "password")
passwd.send_keys(password)
input_button = driver.find_element(By.XPATH, "//button[@type='submit']")
input_button.click()
incorrect_login = driver.find_element(By.XPATH, "//div[text()='Неверный логин']")
incorrect_password = driver.find_element(By.XPATH, "//div[text()='Неверный пароль']")
# check
incorrect_login_value = incorrect_login.text
incorrect_password_value = incorrect_password.text
assert incorrect_login_value == 'Неверный логин'
assert incorrect_password_value == 'Неверный пароль'
print('incorrect login and correct password PASSED')

'''incorrect login and incorrect password'''
driver.refresh()
type_of = driver.find_element(By.CSS_SELECTOR, ".m-ui-paper.m-ui-select__paper")
type_of.click()
type_of_change = driver.find_element(By.XPATH, "//option[@type='EMBEDDED']")
type_of_change.click()


login = driver.find_element(By.NAME, "username")
# time.sleep(1)
login.send_keys(inc_username)
passwd = driver.find_element(By.NAME, "password")
passwd.send_keys(inc_password)
input_button = driver.find_element(By.XPATH, "//button[@type='submit']")
input_button.click()
incorrect_login = driver.find_element(By.XPATH, "//div[text()='Неверный логин']")
incorrect_password = driver.find_element(By.XPATH, "//div[text()='Неверный пароль']")
# check
incorrect_login_value = incorrect_login.text
incorrect_password_value = incorrect_password.text
assert incorrect_login_value == 'Неверный логин'
assert incorrect_password_value == 'Неверный пароль'
print('incorrect login and incorrect password PASSED')

'''correct login and incorrect password'''
driver.refresh()
type_of = driver.find_element(By.CSS_SELECTOR, ".m-ui-paper.m-ui-select__paper")
type_of.click()
type_of_change = driver.find_element(By.XPATH, "//option[@type='EMBEDDED']")
type_of_change.click()


login = driver.find_element(By.NAME, "username")
# time.sleep(1)
login.send_keys(username)
passwd = driver.find_element(By.NAME, "password")
passwd.send_keys(inc_password)
input_button = driver.find_element(By.XPATH, "//button[@type='submit']")
input_button.click()
incorrect_login = driver.find_element(By.XPATH, "//div[text()='Неверный логин']")
incorrect_password = driver.find_element(By.XPATH, "//div[text()='Неверный пароль']")
# check
incorrect_login_value = incorrect_login.text
incorrect_password_value = incorrect_password.text
assert incorrect_login_value == 'Неверный логин'
assert incorrect_password_value == 'Неверный пароль'
print('correct login and incorrect password PASSED')

'''restore'''
# incorrect login
restore_access = driver.find_element(By.XPATH, "//span[text()='Восстановить доступ']")
restore_access.click()
login = driver.find_element(By.NAME, "username")
login.send_keys(inc_username)
restore_access_button = driver.find_element(By.XPATH, "//button[@type='submit']")
restore_access_button.click()
incorrect_login = driver.find_element(By.XPATH, "//div[text()='Неверный логин']")
incorrect_login_value = incorrect_login.text
assert incorrect_login_value == 'Неверный логин'
print('---restore---')
print('restore incorrect login PASSED')

# correct login
login = driver.find_element(By.NAME, "username")
login.send_keys(username)
restore_access_button = driver.find_element(By.XPATH, "//button[@type='submit']")
restore_access_button.click()
time.sleep(1)
restore_access_button.click()
time.sleep(1)
screenshoot()
print('restore correct login PASSED')

# open screenshot
# path = 'C:\\Users\\User\\PycharmProjects\\Minervasoft\\screen\\screenshot.png2023.04.11.08.46.24.png'
# os.startfile(path)

# i remember
remember = driver.find_element(By.XPATH, "//span[text()='я помню пароль']")
remember.click()
# check input page
input_page = driver.find_element(By.XPATH, "//h1[text()='Вход в систему']")
input_page_value = input_page.text
assert input_page_value == 'Вход в систему'
print('---remember---')
print('input page opened PASSED')


driver.quit()



