from selenium import webdriver
import data_login_password

# Настройки браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


class MainPage:

    def __init__(self, browser=driver, url=data_login_password.url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_actual_url(self):
        return self.browser.current_url
