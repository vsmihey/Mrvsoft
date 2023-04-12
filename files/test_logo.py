import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
# download webdriver
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# no close browser
chrome_options = Options()
chrome_options.add_argument("--headless") # запуск в скрытом режиме
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
# browser.set_page_load_timeout()
url = "https://test2.minervasoft.ru/login?from=%2F"
driver.get(url)
driver.maximize_window()
def screenshoot():
    offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
    now_date = datetime.datetime.now(offset)
    now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
    # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
    name_screenshot = 'screenshot.png' + now_date + '.png'
    driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\Minervasoft\\screen\\' + name_screenshot)


def test_logo():
    logo_auth = driver.find_element(By.XPATH, "//img[@alt='Minervasoft']")
    logo_auth_text = driver.find_element(By.XPATH, "//span[text()='Minervasoft']")
    logo_auth_text_value =logo_auth_text.text
    assert logo_auth_text_value == 'Minervasoft'
    time.sleep(1)
    screenshoot()
