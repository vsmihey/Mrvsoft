import functools
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import data_login_password

# Настройки браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(12)


class MainPage:

    def __init__(self, browser=driver, url=None):
        self.browser = browser
        if url is None:
            self.url = data_login_password.url
        else:
            self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_actual_url(self):
        return self.browser.current_url

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))